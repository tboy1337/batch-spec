lexer grammar BatchLexer;

@lexer::members {
def _atLineStart(self) -> bool:
    col = self.column
    if col == 0:
        return True
    start = self._input.index - col
    prefix = self._input.getText(start, self._input.index - 1)
    return prefix.strip() == ""
}

fragment DIGIT : [0-9] ;

LINE_COMMENT   : {self._atLineStart()}? '::' ~[\r\n]* -> skip ;
REM            : {self._atLineStart()}? [rR][eE][mM] ~[\r\n]* -> skip ;

LABEL          : {self._atLineStart()}? ':' ~[ \t\r\n(]+ ;

AT             : '@' ;

FOR            : [fF][oO][rR] ;
IF             : [iI][fF] ;
CALL           : [cC][aA][lL][lL] ;
GOTO           : [gG][oO][tT][oO] ;
SET            : [sS][eE][tT] ;
SETLOCAL       : [sS][eE][tT][lL][oO][cC][aA][lL] ;
ENDLOCAL       : [eE][nN][dD][lL][oO][cC][aA][lL] ;
DO             : [dD][oO] ;
IN             : [iI][nN] ;
EXIST          : [eE][xX][iI][sS][tT] ;
DEFINED        : [dD][eE][fF][iI][nN][eE][dD] ;
NOT            : [nN][oO][tT] ;
ERRORLEVEL     : [eE][rR][rR][oO][rR][lL][eE][vV][eE][lL] ;
ELSE           : [eE][lL][sS][eE] ;
EXIT           : [eE][xX][iI][tT] ;
SHIFT          : [sS][hH][iI][fF][tT] ;
EOF_KW         : [eE][oO][fF] ;

LPAREN         : '(' ;
RPAREN         : ')' ;
AMP            : '&' ;
PIPE           : '|' ;
AMPAMP         : '&&' ;
PIPEPIPE       : '||' ;
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
    : '%' '~' ('$' [a-zA-Z_][a-zA-Z0-9_]* ':' [0-9a-zA-Z*] | [a-zA-Z]* [0-9a-zA-Z*])
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
    : '%%' '~' ([a-zA-Z$]+ [a-zA-Z]? | '$' [a-zA-Z_][a-zA-Z0-9_]* ':' [0-9a-zA-Z*])
    ;

BANG_VAR
    : '!' [a-zA-Z_][a-zA-Z0-9_]* '!'
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
