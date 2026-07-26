parser grammar BatchParser;

options { tokenVocab = BatchLexer; }

@parser::members {
def _notForToken(self) -> bool:
    from BatchLexer import BatchLexer  # isort: skip
    return self._input.LA(1) != BatchLexer.FOR

def _laIf(self) -> bool:
    from BatchLexer import BatchLexer  # isort: skip
    return self._input.LA(1) == BatchLexer.IF

def _laFor(self) -> bool:
    from BatchLexer import BatchLexer  # isort: skip
    return self._input.LA(1) == BatchLexer.FOR

def _laElse(self) -> bool:
    from BatchLexer import BatchLexer  # isort: skip
    return self._input.LA(1) == BatchLexer.ELSE

def _laRem(self) -> bool:
    from BatchLexer import BatchLexer  # isort: skip
    return self._input.LA(1) == BatchLexer.REM

def _genericCmdStartOk(self) -> bool:
    # Do not let genericCmd absorb IF/FOR/ELSE/REM; those have dedicated rules
    # so invalid IF predicates surface as syntax errors (live cmd) and REM
    # remarks through EOL (including after & / && / ||).
    return not (self._laIf() or self._laFor() or self._laElse() or self._laRem())

def _notLonelyParen(self) -> bool:
    from BatchLexer import BatchLexer  # isort: skip
    la1 = self._input.LA(1)
    if la1 != BatchLexer.RPAREN:
        return True
    # Lonely ')' closes a paren block; do not absorb into genericCmd.
    # ELSE must be lonely so ") ELSE" builds elseClause (IF /? form).
    la2 = self._input.LA(2)
    return la2 not in (
        BatchLexer.NEWLINE,
        BatchLexer.AMP,
        BatchLexer.PIPE,
        BatchLexer.AMPAMP,
        BatchLexer.PIPEPIPE,
        BatchLexer.ELSE,
        -1,
    )

def _enterThenStmt(self) -> None:
    self._thenStmtDepth = getattr(self, "_thenStmtDepth", 0) + 1

def _exitThenStmt(self) -> None:
    self._thenStmtDepth = getattr(self, "_thenStmtDepth", 0) - 1

def _elseAsArgAllowed(self) -> bool:
    # Inside IF then-statement (non-paren), bare ELSE starts elseClause.
    return getattr(self, "_thenStmtDepth", 0) == 0

def _notOpenParenThen(self) -> bool:
    from BatchLexer import BatchLexer  # isort: skip
    # Same-line '(' after the predicate starts a paren block (IF /?).
    return self._input.LA(1) != BatchLexer.LPAREN

def _expandedPredicateOk(self) -> bool:
    # After %var% / %1 / !var! as a full expanded predicate, another operand
    # without a compare-op is a live syntax error (IF %ERRORLEVEL% 1).
    from BatchLexer import BatchLexer  # isort: skip
    return self._input.LA(1) not in (
        BatchLexer.NUMBER,
        BatchLexer.HEX_NUMBER,
        BatchLexer.PERCENT_VAR,
        BatchLexer.PERCENT_VAR_SUBSTRING,
        BatchLexer.PERCENT_VAR_REPLACE,
        BatchLexer.PERCENT_ARG,
        BatchLexer.PERCENT_TILDE,
        BatchLexer.BANG_VAR,
        BatchLexer.BANG_VAR_SUBSTRING,
        BatchLexer.BANG_VAR_REPLACE,
        BatchLexer.DQ_STRING,
        BatchLexer.MINUS,
    )

def _forFOptionsOk(self, text: str) -> bool:
    # Live cmd accepts only one eol= comment character; eol=#x and similar
    # multi-character values are syntax errors ("x" was unexpected...).
    import re  # isort: skip

    body = text[1:-1] if len(text) >= 2 and text[0] == '"' else text
    for match in re.finditer(r"(?i)\beol=(\S*)", body):
        value = match.group(1)
        # Stop at next option-like token boundary inside the value.
        value = re.split(r"(?i)\b(?:skip|delims|tokens|usebackq|useback)=", value, maxsplit=1)[
            0
        ]
        if len(value) > 1:
            self.notifyErrorListeners(
                f"FOR /F eol= accepts one character; got {value!r}"
            )
            return False
    return True

def _gapHasSpaceOrTab(self, after_token, before_token) -> bool:
    # Lexer skips WS, so inspect the underlying char stream between tokens.
    start = after_token.stop + 1
    stop = before_token.start - 1
    if stop < start:
        return False
    gap = self._input.tokenSource.inputStream.getText(start, stop)
    return any(ch in " \t" for ch in gap)

def _tokenOf(self, node_or_token):
    # ctx.LPAREN()/RPAREN() yield TerminalNode; compareOperand.start/stop are Tokens.
    symbol = getattr(node_or_token, "symbol", None)
    return symbol if symbol is not None else node_or_token

def _parenCompareInteriorOk(self, ctx) -> bool:
    # When both outer parens wrap a comparison, live cmd fatals if space/tab
    # sits immediately inside either paren (if ( 1==1 ) / if( 1==1) /
    # if(1==1 )). Glued forms and spaces around the compare-op remain
    # silent-false. Single-sided paren forms stay accepted (paren absorbed).
    lparen = ctx.LPAREN()
    rparen = ctx.RPAREN()
    if lparen is None or rparen is None:
        return True
    operands = ctx.compareOperand()
    if len(operands) < 2:
        return True
    left_start = operands[0].start
    right_stop = operands[1].stop
    ltok = self._tokenOf(lparen)
    rtok = self._tokenOf(rparen)
    if self._gapHasSpaceOrTab(ltok, left_start) or self._gapHasSpaceOrTab(
        right_stop, rtok
    ):
        self.notifyErrorListeners(
            "IF paren-wrapped comparison rejects interior space/tab "
            "immediately inside '(' or ')'"
        )
        return False
    return True
}

script
    : line* EOF
    ;

line
    : label
    | commandLine
    | NEWLINE
    ;

label
    : LABEL NEWLINE?
    ;

commandLine
    : statement ( (AMP | PIPE | AMPAMP | PIPEPIPE) statement )* NEWLINE?
    ;

statement
    : AT? (
        // Commit on IF/FOR so invalid predicates report syntax errors instead
        // of silently falling through to genericCmd (live cmd syntax rejects).
        {self._laIf()}? ifStmt
      | {self._laFor()}? forStmt
      // REM remarks out the rest of the physical line (live cmd), including
      // after & / && / ||; remStmt (~NEWLINE)* absorbs separators so they are
      // not chained as separate statements.
      | {self._laRem()}? remStmt
      | callStmt
      | gotoStmt
      | setStmt
      | setlocalStmt
      | endlocalStmt
      | exitStmt
      | shiftStmt
      // Newline-detached ELSE is not IF's elseClause: live cmd treats it as an
      // unknown command, and a following (block) still runs as a group.
      | detachedElseStmt
      | groupStmt
      | genericCmd
      )
    ;

// REM as command verb: remainder of the physical line is remark text (REM /?).
remStmt
    : REM (~NEWLINE)*
    ;

// Detached ELSE (not same-line elseClause). Matches `else echo`, `else if ...`,
// and `else ( ... )` so orphan paren groups parse like live cmd.
detachedElseStmt
    : ELSE (groupStmt | commandTail)?
    ;

exitStmt
    : EXIT exitTail?
    ;

exitTail
    : SLASH WORD NUMBER?
    | NUMBER
    | token+
    ;

groupStmt
    : LPAREN block RPAREN commandTail?
    ;

shiftStmt
    : SHIFT token*
    ;

ifStmt
    : IF ifIOpt? ifBody
    ;

ifIOpt
    : SLASH WORD
    ;

ifBody
    : ifPredicate LPAREN block RPAREN elseClause?
    | ifPredicate {self._notOpenParenThen()}? {self._enterThenStmt()} statement {self._exitThenStmt()} elseClause?
    ;

elseClause
    : ELSE LPAREN block RPAREN
    | ELSE statement
    ;

// Live cmd: IF ERRORLEVEL accepts a literal (optional leading minus), or a
// percent/bang/FOR expansion that yields digits after the percent pass
// (IF ERRORLEVEL %n% / !n!). Same shape for CMDEXTVERSION.
ifErrorlevelStmt
    : ERRORLEVEL MINUS? NUMBER
    | ERRORLEVEL PERCENT_VAR
    | ERRORLEVEL PERCENT_ARG
    | ERRORLEVEL PERCENT_TILDE
    | ERRORLEVEL BANG_VAR
    | ERRORLEVEL FOR_VAR
    ;

ifCmdextversionStmt
    : CMDEXTVERSION MINUS? NUMBER
    | CMDEXTVERSION PERCENT_VAR
    | CMDEXTVERSION PERCENT_ARG
    | CMDEXTVERSION PERCENT_TILDE
    | CMDEXTVERSION BANG_VAR
    | CMDEXTVERSION FOR_VAR
    ;

ifExistOperand
    : DQ_STRING
    | WORD
    | ASTERISK (DOT argWord)?
    | QUESTION+ (DOT argWord)?
    | PERCENT_VAR
    | PERCENT_TILDE
    | PERCENT_ARG
    | FOR_VAR
    | FOR_VAR_TILDE
    | BANG_VAR_SUBSTRING
    | BANG_VAR_REPLACE
    | BANG_VAR
    ;

ifDefinedOperand
    : argWord
    | PERCENT_VAR
    | FOR_VAR
    | FOR_VAR_TILDE
    | BANG_VAR
    ;

ifPredicate
    : NOT? ifErrorlevelStmt
    | NOT? ifCmdextversionStmt
    | NOT? DEFINED ifDefinedOperand
    | NOT? EXIST ifExistOperand
    | NOT? comparison
    // Expanded predicate forms (e.g. if %b% when b=a==a). Reject when another
    // operand follows without a compare-op (IF %ERRORLEVEL% 1).
    | PERCENT_VAR {self._expandedPredicateOk()}?
    | PERCENT_VAR_SUBSTRING {self._expandedPredicateOk()}?
    | PERCENT_VAR_REPLACE {self._expandedPredicateOk()}?
    | PERCENT_ARG {self._expandedPredicateOk()}?
    | PERCENT_TILDE {self._expandedPredicateOk()}?
    | BANG_VAR {self._expandedPredicateOk()}?
    | BANG_VAR_SUBSTRING {self._expandedPredicateOk()}?
    | BANG_VAR_REPLACE {self._expandedPredicateOk()}?
    | DQ_STRING {self._expandedPredicateOk()}?
    ;

// Optional outer parentheses around a comparison are accepted at parse time
// so forms like if(1==1) / if (1==1) do not hard-error. Live cmd typically
// absorbs those parens into the operand text (silent false) rather than
// treating them as C-style grouping -- see if_forms.paren_wrapped_predicate.
// Interior space/tab immediately inside both wrapping parens is a live syntax
// error (if ( 1==1 )); the predicate inspects the char stream because WS is
// skipped by the lexer -- see if_forms.paren_interior_space_fatal.
comparison
    : LPAREN? compareOperand compareOp compareOperand RPAREN?
      {self._parenCompareInteriorOk($ctx)}?
    ;

compareOp
    : EQ
    | EQU
    | NEQ
    | LSS
    | LEQ
    | GTR
    | GEQ
    ;

// One IF compare side. Allow stacked atoms so classic padding forms such as
// .%EMPTY%.==.. tokenize/parse (DOT + PERCENT_VAR + DOT). Exclude compareOp
// tokens so `a EQU b` does not swallow the operator into the left operand.
compareOperand
    : compareOperandPart+
    ;

compareOperandPart
    : DQ_STRING
    | PERCENT_TILDE
    | INVALID_PERCENT_TILDE
    | PERCENT_VAR_SUBSTRING
    | PERCENT_VAR_REPLACE
    | PERCENT_VAR
    | PERCENT_ARG
    | FOR_VAR
    | FOR_VAR_TILDE
    | BANG_VAR_SUBSTRING
    | BANG_VAR_REPLACE
    | BANG_VAR
    | WORD
    | NUMBER
    | HEX_NUMBER
    | DOT
    | MINUS
    | PLUS
    | ASTERISK
    | QUESTION
    | TILDE
    | HASH
    | DOLLAR
    | AT
    | CARET_ESCAPE
    ;

forStmt
    : FOR forSlashMod* forFOptions? forPath? FOR_VAR IN LPAREN forList RPAREN DO forBody
    ;

forPath
    : argWord
    | DQ_STRING
    ;

forSlashMod
    : SLASH WORD
    ;

forFOptions
    : DQ_STRING {self._forFOptionsOk($DQ_STRING.text)}?
    | forFOptionAnchor forFOptionExtra*
    ;

forFOptionAnchor
    : argWord CARET_ESCAPE
    | CARET_ESCAPE
    ;

forFOptionExtra
    : argWord CARET_ESCAPE
    | CARET_ESCAPE
    | NUMBER
    | COMMA
    | ASTERISK
    | QUESTION
    | MINUS
    | PLUS
    | PERCENT
    | argWord
    ;

forBody
    : LPAREN block RPAREN
    | statement
    ;

// Classic FOR set members split on space/tab (token gaps) and on comma,
// semicolon, and equals (same delimiters as batch args; see expansion
// for_forms.set_member_delimiters). Consecutive separators collapse.
// Empty sets ( ) and separator-only sets (,,) are valid and iterate zero
// times on live cmd. forListItem+ covers space/tab-separated members
// (WS is skipped by the lexer).
forList
    : forListItem (forListSep+ forListItem)* forListSep*
    | forListItem+ forListSep*
    | forListSep+
    |
    ;

forListSep
    : COMMA
    | SEMICOLON
    | EQUALS
    ;

forListItem
    : SQ_STRING
    | DQ_STRING
    | BACKTICK_STRING
    | PERCENT_VAR
    | PERCENT_TILDE
    | PERCENT_ARG
    | ASTERISK (DOT argWord)?
    // ???.txt is QUESTION+ then DOT argWord via forListItem+; a?.txt is
    // argWord then QUESTION then DOT argWord. Trailing ? may match fewer
    // characters at runtime (see expansion for_forms.wildcard_question_trailing).
    | QUESTION+ (DOT argWord)?
    | DOT argWord?
    | argWord
    | MINUS? NUMBER
    | MINUS? HEX_NUMBER
    ;

callStmt
    // Bare CALL / (CALL) / (CALL ) are valid and set ERRORLEVEL (see
    // expansion.yaml errorlevel.call_empty_*). Target is optional.
    : CALL callTarget? commandTail?
    ;

callTarget
    : COLON? EOF_KW
    | COLON? argWord
    | COLON? PERCENT_ARG
    | COLON? PERCENT_VAR
    | COLON? BANG_VAR
    | DQ_STRING
    ;

// GOTO takes the remainder of the statement as the target (spaces allowed).
// CALL keeps callTarget as the first word/token and commandTail as arguments.
gotoStmt
    : GOTO callTarget commandTail?
    ;

setStmt
    : SET setMode? setAssign?
    ;

setMode
    : SLASH WORD
    ;

setAssign
    : DQ_STRING
    | setTarget EQUALS setRest?
    | setTarget
    ;

setlocalStmt
    : SETLOCAL setlocalRest?
    ;

setlocalRest
    : token+
    ;

endlocalStmt
    : ENDLOCAL commandTail?
    ;

// Unquoted SET names may include punctuation that the lexer emits as
// separate tokens (~ @ # $ ; , ( ) * + ? . - and digits). Keep consuming
// name parts until EQUALS / chain / newline so `set a~b=1` and `set var@x=3`
// remain a single setStmt (live cmd; see expansion environment_variable_names).
setTarget
    : setNamePart+
    | PERCENT_VAR
    ;

setNamePart
    : argWord
    | NUMBER
    | HEX_NUMBER
    | TILDE
    | AT
    | HASH
    | DOLLAR
    | SEMICOLON
    | COMMA
    | DOT
    | PLUS
    | MINUS
    | ASTERISK
    | QUESTION
    | LPAREN
    | RPAREN
    ;

setRest
    : token+
    ;

genericCmd
    : {self._notForToken() and self._notLonelyParen() and self._genericCmdStartOk()}? commandTail
    ;

commandTail
    : token+
    ;

argWord
    : WORD
    | FOR
    | IF
    | SET
    | DO
    | IN
    | EXIST
    | DEFINED
    | NOT
    | ERRORLEVEL
    | CMDEXTVERSION
    | EXIT
    | SHIFT
    | CALL
    | GOTO
    | ENDLOCAL
    | SETLOCAL
    | REM
    | {self._elseAsArgAllowed()}? ELSE
    | EQU
    | NEQ
    | LSS
    | LEQ
    | GTR
    | GEQ
    ;

token
    : DQ_STRING
    | SQ_STRING
    | BACKTICK_STRING
    | PERCENT_TILDE
    | INVALID_PERCENT_TILDE
    | PERCENT_VAR_SUBSTRING
    | PERCENT_VAR_REPLACE
    | PERCENT_VAR
    | PERCENT_ARG
    | FOR_VAR
    | FOR_VAR_TILDE
    | BANG_VAR_SUBSTRING
    | BANG_VAR_REPLACE
    | BANG_VAR
    | BANG
    | TILDE
    | AT
    | HASH
    | DOLLAR
    | CARET_ESCAPE
    | CARET
    | ASTERISK
    | QUESTION
    | LPAREN
    | {self._notLonelyParen()}? RPAREN
    | APPEND
    | DUP_OUT
    | DUP_IN
    | GT
    | LT
    | DOT
    | BACKSLASH
    | PLUS
    | MINUS
    | COMMA
    | SEMICOLON
    | EQUALS
    | EQ
    | SLASH
    | COLON
    | PERCENT
    | argWord
    | NUMBER
    | HEX_NUMBER
    | UNMATCHED_DQ
    | UNMATCHED_SQ
    | UNMATCHED_BACKTICK
    ;

block
    : line*
    ;
