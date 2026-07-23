parser grammar BatchParser;

options { tokenVocab = BatchLexer; }

@parser::members {
def _notForToken(self) -> bool:
    from BatchLexer import BatchLexer  # isort: skip
    return self._input.LA(1) != BatchLexer.FOR
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
      | genericCmd
      )
    ;

exitStmt
    : EXIT exitTail?
    ;

exitTail
    : SLASH WORD
    | NUMBER
    | token+
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

ifExistOperand
    : DQ_STRING
    | WORD
    | PERCENT_VAR
    | PERCENT_TILDE
    | PERCENT_ARG
    ;

ifPredicate
    : NOT? ifErrorlevelStmt
    | NOT? DEFINED argWord
    | NOT? EXIST ifExistOperand
    | comparison
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
    | argWord
    | NUMBER
    ;

forStmt
    : FOR forSlashMod* forFOptions? FOR_VAR IN LPAREN forList RPAREN DO forBody
    ;

forSlashMod
    : SLASH WORD
    ;

forFOptions
    : DQ_STRING
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
    | NUMBER
    ;

callStmt
    : CALL callTarget commandTail?
    ;

callTarget
    : COLON? EOF_KW
    | COLON? argWord
    | PERCENT_ARG
    | PERCENT_VAR
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
    : {self._notForToken()}? commandTail
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
    | CARET_ESCAPE
    | CARET
    | LPAREN
    | RPAREN
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
    ;

block
    : line*
    ;
