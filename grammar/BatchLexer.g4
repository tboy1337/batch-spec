lexer grammar BatchLexer;

@lexer::members {
def _atLineStart(self) -> bool:
    col = self.column
    if col == 0:
        return True
    start = self._input.index - col
    prefix = self._input.getText(start, self._input.index - 1)
    return prefix.strip() == ""

def _keywordTrailerOk(self) -> bool:
    # After matching the keyword text, reject glue to percent/bang/quotes.
    # Live cmd: IF%1, SET%x%, FOR%%i become non-keywords after expansion.
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
// Live cmd accepts letters, digits, and many punctuation chars as FOR vars.
// Exclude ~ (%%~ is FOR_VAR_TILDE), and operators that fail live: %|&=;<>|
fragment FOR_VAR_LETTER : [a-zA-Z0-9?#$@_`[\]{}+.\-\\!*():/] ;

LINE_COMMENT   : {self._atLineStart()}? '::' ~[\r\n]* -> skip ;
REM            : {self._atLineStart()}? [rR][eE][mM] ~[\r\n]* -> skip ;

// Live cmd: a label is a line beginning with ':' and the rest of the physical
// line is the label text (spaces and most punctuation allowed). LINE_COMMENT
// ('::...') is declared first and wins for double-colon remarks.
LABEL          : {self._atLineStart()}? ':' ~[\r\n]+ ;

AT             : '@' ;

FOR            : [fF][oO][rR] {self._keywordTrailerOk()}? ;
IF             : [iI][fF] {self._keywordTrailerOk()}? ;
CALL           : [cC][aA][lL][lL] {self._keywordTrailerOk()}? ;
GOTO           : [gG][oO][tT][oO] {self._keywordTrailerOk()}? ;
SET            : [sS][eE][tT] {self._keywordTrailerOk()}? ;
SETLOCAL       : [sS][eE][tT][lL][oO][cC][aA][lL] {self._keywordTrailerOk()}? ;
ENDLOCAL       : [eE][nN][dD][lL][oO][cC][aA][lL] {self._keywordTrailerOk()}? ;
DO             : [dD][oO] {self._keywordTrailerOk()}? ;
IN             : [iI][nN] {self._keywordTrailerOk()}? ;
EXIST          : [eE][xX][iI][sS][tT] {self._keywordTrailerOk()}? ;
DEFINED        : [dD][eE][fF][iI][nN][eE][dD] {self._keywordTrailerOk()}? ;
NOT            : [nN][oO][tT] {self._keywordTrailerOk()}? ;
ERRORLEVEL     : [eE][rR][rR][oO][rR][lL][eE][vV][eE][lL] {self._keywordTrailerOk()}? ;
CMDEXTVERSION  : [cC][mM][dD][eE][xX][tT][vV][eE][rR][sS][iI][oO][nN] {self._keywordTrailerOk()}? ;
ELSE           : [eE][lL][sS][eE] {self._keywordTrailerOk()}? ;
EXIT           : [eE][xX][iI][tT] {self._keywordTrailerOk()}? ;
SHIFT          : [sS][hH][iI][fF][tT] {self._keywordTrailerOk()}? ;
EOF_KW         : [eE][oO][fF] {self._keywordTrailerOk()}? ;

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
SEMICOLON      : ';' ;
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
// Single-character wildcard in file-set masks (FOR /?, DIR, IF EXIST, etc.).
// Distinct from FOR_VAR_LETTER '?' which only applies inside %%? forms.
QUESTION       : '?' ;

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

// Live cmd accepts a wide env-name charset inside %name% (spaces and most
// punctuation). Exclude '%' (terminator), '=' (SET forbids in names), and
// newlines. Substring/replace forms also exclude ':' in the name portion.
fragment ENV_NAME_CHAR : ~[%=\r\n] ;
fragment ENV_NAME_CHAR_NO_COLON : ~[%:=\r\n] ;

PERCENT_VAR_SUBSTRING
    : '%' ENV_NAME_CHAR_NO_COLON+ ':' '~' '-'? DIGIT+ (',' '-'? DIGIT*)? '%'
    ;

PERCENT_VAR_REPLACE
    : '%' ENV_NAME_CHAR_NO_COLON+ ':' (~'%' | '%%')+ '=' (~'%' | '%%')* '%'
    ;

PERCENT_VAR
    : '%' ENV_NAME_CHAR+ '%'
    ;

PERCENT_ARG
    : '%' [0-9*]
    ;

FOR_VAR_TILDE
    : '%%' '~' ([a-zA-Z]* '$' [a-zA-Z_][a-zA-Z0-9_]* ':' FOR_VAR_LETTER | [a-zA-Z]* FOR_VAR_LETTER)
    ;

FOR_VAR
    : '%%' FOR_VAR_LETTER
    ;

fragment DELAYED_NAME_CHAR : ~[!\r\n] ;
fragment DELAYED_NAME_CHAR_NO_COLON : ~[!:\r\n] ;

BANG_VAR_SUBSTRING
    : '!' DELAYED_NAME_CHAR_NO_COLON+ ':' '~' '-'? DIGIT+ (',' '-'? DIGIT*)? '!'
    ;

BANG_VAR_REPLACE
    : '!' DELAYED_NAME_CHAR_NO_COLON+ ':' (~[!\r\n] | '!!')+ '=' (~[!\r\n] | '!!')* '!'
    ;

BANG_VAR
    : '!' DELAYED_NAME_CHAR+ '!'
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

// Include [] (\u005B/\u005D) so blank-line forms like echo[ / echo] stay a
// single WORD token (live cmd accepts those ECHO blank-line spellings).
WORD           : [a-zA-Z_][a-zA-Z0-9_./\\:+\-\u005B\u005D]* ;
HEX_NUMBER     : '0' [xX] [0-9a-fA-F]+ ;
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
