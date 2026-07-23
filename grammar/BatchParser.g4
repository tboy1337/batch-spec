parser grammar BatchParser;

options { tokenVocab = BatchLexer; }

@parser::members {
def _notForToken(self) -> bool:
    from BatchLexer import BatchLexer  # isort: skip
    return self._input.LA(1) != BatchLexer.FOR

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
        ifStmt
      | forStmt
      | callStmt
      | gotoStmt
      | setStmt
      | setlocalStmt
      | endlocalStmt
      | exitStmt
      | shiftStmt
      | groupStmt
      | genericCmd
      )
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

ifErrorlevelStmt
    : ERRORLEVEL NUMBER
    ;

ifCmdextversionStmt
    : CMDEXTVERSION NUMBER
    ;

ifExistOperand
    : DQ_STRING
    | WORD
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
    | DQ_STRING
    | PERCENT_TILDE
    | argWord
    ;

comparison
    : compareOperand compareOp compareOperand
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

compareOperand
    : DQ_STRING
    | PERCENT_TILDE
    | PERCENT_VAR_SUBSTRING
    | PERCENT_VAR_REPLACE
    | PERCENT_VAR
    | PERCENT_ARG
    | FOR_VAR
    | FOR_VAR_TILDE
    | BANG_VAR_SUBSTRING
    | BANG_VAR_REPLACE
    | BANG_VAR
    | argWord
    | MINUS? NUMBER
    | MINUS? HEX_NUMBER
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
    : DQ_STRING
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
    | MINUS
    | PLUS
    | PERCENT
    | argWord
    ;

forBody
    : LPAREN block RPAREN
    | statement
    ;

forList
    : forListItem (COMMA forListItem)*
    | forListItem+
    ;

forListItem
    : SQ_STRING
    | DQ_STRING
    | BACKTICK_STRING
    | PERCENT_VAR
    | PERCENT_TILDE
    | PERCENT_ARG
    | ASTERISK (DOT argWord)?
    | DOT argWord?
    | argWord
    | MINUS? NUMBER
    | MINUS? HEX_NUMBER
    ;

callStmt
    : CALL callTarget commandTail?
    ;

callTarget
    : COLON? EOF_KW
    | COLON? argWord
    | COLON? PERCENT_ARG
    | COLON? PERCENT_VAR
    | COLON? BANG_VAR
    | DQ_STRING
    ;

gotoStmt
    : GOTO callTarget
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

setTarget
    : argWord
    | PERCENT_VAR
    ;

setRest
    : token+
    ;

genericCmd
    : {self._notForToken() and self._notLonelyParen()}? commandTail
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
    | CARET_ESCAPE
    | CARET
    | ASTERISK
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
    | EQUALS
    | EQ
    | SLASH
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
