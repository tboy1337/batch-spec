lexer grammar BatchLexer;

@lexer::members {
def _atLineStart(self) -> bool:
    col = self.column
    if col == 0:
        return True
    start = self._input.index - col
    prefix = self._input.getText(start, self._input.index - 1)
    return prefix.strip() == ""

def _notKeywordBoundary(self) -> bool:
    la = self._input.LA(1)
    return la not in (
        ord('%'),
        ord('!'),
        ord('"'),
        ord("'"),
        ord('`'),
    )
}

fragment DIGIT : [0-9] ;

LINE_COMMENT   : {self._atLineStart()}? '::' ~[\r\n]* -> skip ;
REM            : {self._atLineStart()}? [rR][eE][mM] ~[\r\n]* -> skip ;

LABEL          : {self._atLineStart()}? ':' ~[ \t\r\n(]+ ;

AT             : '@' ;

FOR            : {self._notKeywordBoundary()}? [fF][oO][rR] ;
IF             : {self._notKeywordBoundary()}? [iI][fF] ;
CALL           : {self._notKeywordBoundary()}? [cC][aA][lL][lL] ;
GOTO           : {self._notKeywordBoundary()}? [gG][oO][tT][oO] ;
SET            : {self._notKeywordBoundary()}? [sS][eE][tT] ;
SETLOCAL       : {self._notKeywordBoundary()}? [sS][eE][tT][lL][oO][cC][aA][lL] ;
ENDLOCAL       : {self._notKeywordBoundary()}? [eE][nN][dD][lL][oO][cC][aA][lL] ;
DO             : {self._notKeywordBoundary()}? [dD][oO] ;
IN             : {self._notKeywordBoundary()}? [iI][nN] ;
EXIST          : {self._notKeywordBoundary()}? [eE][xX][iI][sS][tT] ;
DEFINED        : {self._notKeywordBoundary()}? [dD][eE][fF][iI][nN][eE][dD] ;
NOT            : {self._notKeywordBoundary()}? [nN][oO][tT] ;
ERRORLEVEL     : {self._notKeywordBoundary()}? [eE][rR][rR][oO][rR][lL][eE][vV][eE][lL] ;
CMDEXTVERSION  : {self._notKeywordBoundary()}? [cC][mM][dD][eE][xX][tT][vV][eE][rR][sS][iI][oO][nN] ;
ELSE           : {self._notKeywordBoundary()}? [eE][lL][sS][eE] ;
EXIT           : {self._notKeywordBoundary()}? [eE][xX][iI][tT] ;
SHIFT          : {self._notKeywordBoundary()}? [sS][hH][iI][fF][tT] ;
EOF_KW         : {self._notKeywordBoundary()}? [eE][oO][fF] ;

LPAREN         : '(' ;
RPAREN         : ')' ;
AMP            : '&' ;
PIPE           : '|' ;
AMPAMP         : '&&' ;
PIPEPIPE       : '||' ;
APPEND         : '>>' ;
DUP_OUT        : '>&' ;
DUP_IN         : '<&' ;
GT             : '>' ;
LT             : '<' ;
EQ             : '==' ;
COLON          : ':' ;
SLASH          : '/' ;
EQUALS         : '=' ;
COMMA          : ',' ;
DOT            : '.' ;
BACKSLASH      : '\\' ;
PLUS           : '+' ;
MINUS          : '-' ;

EQU            : [eE][qQ][uU] ;
NEQ            : [nN][eE][qQ] ;
LSS            : [lL][sS][sS] ;
LEQ            : [lL][eE][qQ] ;
GTR            : [gG][tT][rR] ;
GEQ            : [gG][eE][qQ] ;
CARET          : '^' ;
ASTERISK       : '*' ;

LINE_CONTINUATION
    : '^' '\r'? '\n' -> skip
    ;

CARET_ESCAPE
    : '^' ~[\r\n]
    ;

DQ_STRING
    : '"' (~'"' | '""')* '"'
    ;

SQ_STRING
    : '\'' (~'\'' | '\'\'')* '\''
    ;

BACKTICK_STRING
    : '`' (~'`' | '``')* '`'
    ;

PERCENT_TILDE
    : '%' '~' ([a-zA-Z]* '$' [a-zA-Z_][a-zA-Z0-9_]* ':' [0-9a-zA-Z*] | [a-zA-Z]* [0-9a-zA-Z*])
    ;

PERCENT_VAR_SUBSTRING
    : '%' [a-zA-Z_][a-zA-Z0-9_]* ':' '~' '-'? DIGIT+ (',' '-'? DIGIT*)? '%'
    ;

PERCENT_VAR_REPLACE
    : '%' [a-zA-Z_][a-zA-Z0-9_]* ':' (~'%' | '%%')+ '=' (~'%' | '%%')* '%'
    ;

PERCENT_VAR
    : '%' [a-zA-Z_][a-zA-Z0-9_]* '%'
    ;

PERCENT_ARG
    : '%' [0-9*]
    ;

FOR_VAR
    : '%%' [a-zA-Z]
    ;

FOR_VAR_TILDE
    : '%%' '~' ([a-zA-Z]* '$' [a-zA-Z_][a-zA-Z0-9_]* ':' [a-zA-Z] | [a-zA-Z]* [a-zA-Z])
    ;

BANG_VAR
    : '!' [a-zA-Z_][a-zA-Z0-9_]* '!'
    ;

BANG
    : '!'
    ;

TILDE
    : '~'
    ;

PERCENT
    : '%'
    ;

WORD           : [a-zA-Z_][a-zA-Z0-9_./\\:+\-]* ;
NUMBER         : DIGIT+ ;

WS             : [ \t]+ -> skip ;
NEWLINE        : [\r\n]+ ;

UNMATCHED_DQ
    : '"' (~[\r\n"] | '""')*
    ;

UNMATCHED_SQ
    : '\'' (~[\r\n'] | '\'\'')*
    ;

UNMATCHED_BACKTICK
    : '`' (~[\r\n`'] | '``')*
    ;
