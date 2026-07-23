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
    la2 = self._input.LA(2)
    return la2 not in (
        BatchLexer.NEWLINE,
        BatchLexer.AMP,
        BatchLexer.PIPE,
        BatchLexer.AMPAMP,
        BatchLexer.PIPEPIPE,
        -1,
    )
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
    | ifPredicate statement
    ;

elseClause
    : ELSE ifBody
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
    | PERCENT_VAR NUMBER
    | DQ_STRING
    | PERCENT_TILDE
    | PERCENT_VAR
    | PERCENT_ARG
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
    | BANG_VAR
    | argWord
    | NUMBER
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
    | argWord
    | MINUS? NUMBER
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
    : SET setMode? setAssign
    ;

setMode
    : SLASH WORD
    ;

setAssign
    : DQ_STRING
    | setTarget EQUALS setRest?
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
    | ELSE
    | EXIT
    | SHIFT
    | CALL
    | GOTO
    | ENDLOCAL
    | SETLOCAL
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
    | BANG_VAR
    | BANG
    | TILDE
    | CARET_ESCAPE
    | CARET
    | ASTERISK
    | LPAREN
    | RPAREN
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
    | SLASH
    | PERCENT
    | argWord
    | NUMBER
    | UNMATCHED_DQ
    | UNMATCHED_SQ
    | UNMATCHED_BACKTICK
    ;

block
    : line*
    ;
