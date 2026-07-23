# Generated from C:/Users/Laptop/Documents/Git/batch-spec/grammar/BatchParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,64,380,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        1,0,5,0,82,8,0,10,0,12,0,85,9,0,1,0,1,0,1,1,1,1,1,1,3,1,92,8,1,1,
        2,1,2,3,2,96,8,2,1,3,1,3,1,3,5,3,101,8,3,10,3,12,3,104,9,3,1,3,3,
        3,107,8,3,1,4,3,4,110,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,3,4,122,8,4,1,5,1,5,3,5,126,8,5,1,6,1,6,1,6,1,6,4,6,132,8,6,11,
        6,12,6,133,3,6,136,8,6,1,7,1,7,5,7,140,8,7,10,7,12,7,143,9,7,1,8,
        1,8,3,8,147,8,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,
        159,8,10,1,10,1,10,1,10,3,10,164,8,10,1,11,1,11,1,11,1,12,1,12,1,
        12,1,13,1,13,1,14,3,14,175,8,14,1,14,1,14,3,14,179,8,14,1,14,1,14,
        1,14,3,14,184,8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,3,14,196,8,14,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,3,17,212,8,17,1,18,1,18,5,18,216,8,18,10,
        18,12,18,219,9,18,1,18,3,18,222,8,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,21,1,21,3,
        21,242,8,21,1,22,1,22,1,22,5,22,247,8,22,10,22,12,22,250,9,22,1,
        22,4,22,253,8,22,11,22,12,22,254,3,22,257,8,22,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,3,23,268,8,23,1,23,1,23,3,23,272,8,23,
        1,24,1,24,1,24,3,24,277,8,24,1,25,3,25,280,8,25,1,25,1,25,3,25,284,
        8,25,1,25,1,25,1,25,1,25,3,25,290,8,25,1,26,1,26,1,26,1,27,1,27,
        3,27,297,8,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,29,3,29,
        308,8,29,3,29,310,8,29,1,30,1,30,3,30,314,8,30,1,31,4,31,317,8,31,
        11,31,12,31,318,1,32,1,32,3,32,323,8,32,1,33,1,33,3,33,327,8,33,
        1,34,4,34,330,8,34,11,34,12,34,331,1,35,1,35,1,35,1,36,4,36,338,
        8,36,11,36,12,36,339,1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,372,8,38,1,39,5,39,
        375,8,39,10,39,12,39,378,9,39,1,39,0,0,40,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,0,4,1,0,24,27,4,0,48,48,51,51,54,55,60,
        60,2,0,30,30,39,44,2,0,5,20,60,60,441,0,83,1,0,0,0,2,91,1,0,0,0,
        4,93,1,0,0,0,6,97,1,0,0,0,8,109,1,0,0,0,10,123,1,0,0,0,12,135,1,
        0,0,0,14,137,1,0,0,0,16,144,1,0,0,0,18,150,1,0,0,0,20,163,1,0,0,
        0,22,165,1,0,0,0,24,168,1,0,0,0,26,171,1,0,0,0,28,195,1,0,0,0,30,
        197,1,0,0,0,32,201,1,0,0,0,34,211,1,0,0,0,36,213,1,0,0,0,38,231,
        1,0,0,0,40,234,1,0,0,0,42,241,1,0,0,0,44,256,1,0,0,0,46,271,1,0,
        0,0,48,273,1,0,0,0,50,289,1,0,0,0,52,291,1,0,0,0,54,294,1,0,0,0,
        56,300,1,0,0,0,58,309,1,0,0,0,60,311,1,0,0,0,62,316,1,0,0,0,64,320,
        1,0,0,0,66,326,1,0,0,0,68,329,1,0,0,0,70,333,1,0,0,0,72,337,1,0,
        0,0,74,341,1,0,0,0,76,371,1,0,0,0,78,376,1,0,0,0,80,82,3,2,1,0,81,
        80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,
        0,85,83,1,0,0,0,86,87,5,0,0,1,87,1,1,0,0,0,88,92,3,4,2,0,89,92,3,
        6,3,0,90,92,5,63,0,0,91,88,1,0,0,0,91,89,1,0,0,0,91,90,1,0,0,0,92,
        3,1,0,0,0,93,95,5,3,0,0,94,96,5,63,0,0,95,94,1,0,0,0,95,96,1,0,0,
        0,96,5,1,0,0,0,97,102,3,8,4,0,98,99,7,0,0,0,99,101,3,8,4,0,100,98,
        1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,106,
        1,0,0,0,104,102,1,0,0,0,105,107,5,63,0,0,106,105,1,0,0,0,106,107,
        1,0,0,0,107,7,1,0,0,0,108,110,5,4,0,0,109,108,1,0,0,0,109,110,1,
        0,0,0,110,121,1,0,0,0,111,122,3,16,8,0,112,122,3,36,18,0,113,122,
        3,48,24,0,114,122,3,52,26,0,115,122,3,54,27,0,116,122,3,60,30,0,
        117,122,3,64,32,0,118,122,3,10,5,0,119,122,3,14,7,0,120,122,3,70,
        35,0,121,111,1,0,0,0,121,112,1,0,0,0,121,113,1,0,0,0,121,114,1,0,
        0,0,121,115,1,0,0,0,121,116,1,0,0,0,121,117,1,0,0,0,121,118,1,0,
        0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,9,1,0,0,0,123,125,5,19,0,
        0,124,126,3,12,6,0,125,124,1,0,0,0,125,126,1,0,0,0,126,11,1,0,0,
        0,127,128,5,32,0,0,128,136,5,60,0,0,129,136,5,61,0,0,130,132,3,76,
        38,0,131,130,1,0,0,0,132,133,1,0,0,0,133,131,1,0,0,0,133,134,1,0,
        0,0,134,136,1,0,0,0,135,127,1,0,0,0,135,129,1,0,0,0,135,131,1,0,
        0,0,136,13,1,0,0,0,137,141,5,20,0,0,138,140,3,76,38,0,139,138,1,
        0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,15,1,0,
        0,0,143,141,1,0,0,0,144,146,5,6,0,0,145,147,3,18,9,0,146,145,1,0,
        0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,3,20,10,0,149,17,1,0,
        0,0,150,151,5,32,0,0,151,152,5,60,0,0,152,19,1,0,0,0,153,154,3,28,
        14,0,154,155,5,22,0,0,155,156,3,78,39,0,156,158,5,23,0,0,157,159,
        3,22,11,0,158,157,1,0,0,0,158,159,1,0,0,0,159,164,1,0,0,0,160,161,
        3,28,14,0,161,162,3,8,4,0,162,164,1,0,0,0,163,153,1,0,0,0,163,160,
        1,0,0,0,164,21,1,0,0,0,165,166,5,18,0,0,166,167,3,20,10,0,167,23,
        1,0,0,0,168,169,5,17,0,0,169,170,5,61,0,0,170,25,1,0,0,0,171,172,
        7,1,0,0,172,27,1,0,0,0,173,175,5,16,0,0,174,173,1,0,0,0,174,175,
        1,0,0,0,175,176,1,0,0,0,176,196,3,24,12,0,177,179,5,16,0,0,178,177,
        1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,181,5,15,0,0,181,196,
        3,74,37,0,182,184,5,16,0,0,183,182,1,0,0,0,183,184,1,0,0,0,184,185,
        1,0,0,0,185,186,5,14,0,0,186,196,3,26,13,0,187,196,3,30,15,0,188,
        189,5,54,0,0,189,196,5,61,0,0,190,196,5,48,0,0,191,196,5,51,0,0,
        192,196,5,54,0,0,193,196,5,55,0,0,194,196,3,74,37,0,195,174,1,0,
        0,0,195,178,1,0,0,0,195,183,1,0,0,0,195,187,1,0,0,0,195,188,1,0,
        0,0,195,190,1,0,0,0,195,191,1,0,0,0,195,192,1,0,0,0,195,193,1,0,
        0,0,195,194,1,0,0,0,196,29,1,0,0,0,197,198,3,34,17,0,198,199,3,32,
        16,0,199,200,3,34,17,0,200,31,1,0,0,0,201,202,7,2,0,0,202,33,1,0,
        0,0,203,212,5,48,0,0,204,212,5,51,0,0,205,212,5,52,0,0,206,212,5,
        53,0,0,207,212,5,54,0,0,208,212,5,55,0,0,209,212,3,74,37,0,210,212,
        5,61,0,0,211,203,1,0,0,0,211,204,1,0,0,0,211,205,1,0,0,0,211,206,
        1,0,0,0,211,207,1,0,0,0,211,208,1,0,0,0,211,209,1,0,0,0,211,210,
        1,0,0,0,212,35,1,0,0,0,213,217,5,5,0,0,214,216,3,38,19,0,215,214,
        1,0,0,0,216,219,1,0,0,0,217,215,1,0,0,0,217,218,1,0,0,0,218,221,
        1,0,0,0,219,217,1,0,0,0,220,222,3,40,20,0,221,220,1,0,0,0,221,222,
        1,0,0,0,222,223,1,0,0,0,223,224,5,56,0,0,224,225,5,13,0,0,225,226,
        5,22,0,0,226,227,3,44,22,0,227,228,5,23,0,0,228,229,5,12,0,0,229,
        230,3,42,21,0,230,37,1,0,0,0,231,232,5,32,0,0,232,233,5,60,0,0,233,
        39,1,0,0,0,234,235,5,48,0,0,235,41,1,0,0,0,236,237,5,22,0,0,237,
        238,3,78,39,0,238,239,5,23,0,0,239,242,1,0,0,0,240,242,3,8,4,0,241,
        236,1,0,0,0,241,240,1,0,0,0,242,43,1,0,0,0,243,248,3,46,23,0,244,
        245,5,34,0,0,245,247,3,46,23,0,246,244,1,0,0,0,247,250,1,0,0,0,248,
        246,1,0,0,0,248,249,1,0,0,0,249,257,1,0,0,0,250,248,1,0,0,0,251,
        253,3,46,23,0,252,251,1,0,0,0,253,254,1,0,0,0,254,252,1,0,0,0,254,
        255,1,0,0,0,255,257,1,0,0,0,256,243,1,0,0,0,256,252,1,0,0,0,257,
        45,1,0,0,0,258,272,5,49,0,0,259,272,5,48,0,0,260,272,5,50,0,0,261,
        272,5,54,0,0,262,272,5,51,0,0,263,272,5,55,0,0,264,267,5,46,0,0,
        265,266,5,35,0,0,266,268,3,74,37,0,267,265,1,0,0,0,267,268,1,0,0,
        0,268,272,1,0,0,0,269,272,3,74,37,0,270,272,5,61,0,0,271,258,1,0,
        0,0,271,259,1,0,0,0,271,260,1,0,0,0,271,261,1,0,0,0,271,262,1,0,
        0,0,271,263,1,0,0,0,271,264,1,0,0,0,271,269,1,0,0,0,271,270,1,0,
        0,0,272,47,1,0,0,0,273,274,5,7,0,0,274,276,3,50,25,0,275,277,3,72,
        36,0,276,275,1,0,0,0,276,277,1,0,0,0,277,49,1,0,0,0,278,280,5,31,
        0,0,279,278,1,0,0,0,279,280,1,0,0,0,280,281,1,0,0,0,281,290,5,21,
        0,0,282,284,5,31,0,0,283,282,1,0,0,0,283,284,1,0,0,0,284,285,1,0,
        0,0,285,290,3,74,37,0,286,290,5,55,0,0,287,290,5,54,0,0,288,290,
        5,48,0,0,289,279,1,0,0,0,289,283,1,0,0,0,289,286,1,0,0,0,289,287,
        1,0,0,0,289,288,1,0,0,0,290,51,1,0,0,0,291,292,5,8,0,0,292,293,3,
        50,25,0,293,53,1,0,0,0,294,296,5,9,0,0,295,297,3,56,28,0,296,295,
        1,0,0,0,296,297,1,0,0,0,297,298,1,0,0,0,298,299,3,58,29,0,299,55,
        1,0,0,0,300,301,5,32,0,0,301,302,5,60,0,0,302,57,1,0,0,0,303,310,
        5,48,0,0,304,305,3,66,33,0,305,307,5,33,0,0,306,308,3,68,34,0,307,
        306,1,0,0,0,307,308,1,0,0,0,308,310,1,0,0,0,309,303,1,0,0,0,309,
        304,1,0,0,0,310,59,1,0,0,0,311,313,5,10,0,0,312,314,3,62,31,0,313,
        312,1,0,0,0,313,314,1,0,0,0,314,61,1,0,0,0,315,317,3,76,38,0,316,
        315,1,0,0,0,317,318,1,0,0,0,318,316,1,0,0,0,318,319,1,0,0,0,319,
        63,1,0,0,0,320,322,5,11,0,0,321,323,3,72,36,0,322,321,1,0,0,0,322,
        323,1,0,0,0,323,65,1,0,0,0,324,327,3,74,37,0,325,327,5,54,0,0,326,
        324,1,0,0,0,326,325,1,0,0,0,327,67,1,0,0,0,328,330,3,76,38,0,329,
        328,1,0,0,0,330,331,1,0,0,0,331,329,1,0,0,0,331,332,1,0,0,0,332,
        69,1,0,0,0,333,334,4,35,0,0,334,335,3,72,36,0,335,71,1,0,0,0,336,
        338,3,76,38,0,337,336,1,0,0,0,338,339,1,0,0,0,339,337,1,0,0,0,339,
        340,1,0,0,0,340,73,1,0,0,0,341,342,7,3,0,0,342,75,1,0,0,0,343,372,
        5,48,0,0,344,372,5,49,0,0,345,372,5,50,0,0,346,372,5,51,0,0,347,
        372,5,52,0,0,348,372,5,53,0,0,349,372,5,54,0,0,350,372,5,55,0,0,
        351,372,5,56,0,0,352,372,5,57,0,0,353,372,5,58,0,0,354,372,5,47,
        0,0,355,372,5,45,0,0,356,372,5,22,0,0,357,372,5,23,0,0,358,372,5,
        28,0,0,359,372,5,29,0,0,360,372,5,35,0,0,361,372,5,36,0,0,362,372,
        5,37,0,0,363,372,5,38,0,0,364,372,5,34,0,0,365,372,5,33,0,0,366,
        372,5,32,0,0,367,372,5,59,0,0,368,372,3,74,37,0,369,372,5,61,0,0,
        370,372,5,64,0,0,371,343,1,0,0,0,371,344,1,0,0,0,371,345,1,0,0,0,
        371,346,1,0,0,0,371,347,1,0,0,0,371,348,1,0,0,0,371,349,1,0,0,0,
        371,350,1,0,0,0,371,351,1,0,0,0,371,352,1,0,0,0,371,353,1,0,0,0,
        371,354,1,0,0,0,371,355,1,0,0,0,371,356,1,0,0,0,371,357,1,0,0,0,
        371,358,1,0,0,0,371,359,1,0,0,0,371,360,1,0,0,0,371,361,1,0,0,0,
        371,362,1,0,0,0,371,363,1,0,0,0,371,364,1,0,0,0,371,365,1,0,0,0,
        371,366,1,0,0,0,371,367,1,0,0,0,371,368,1,0,0,0,371,369,1,0,0,0,
        371,370,1,0,0,0,372,77,1,0,0,0,373,375,3,2,1,0,374,373,1,0,0,0,375,
        378,1,0,0,0,376,374,1,0,0,0,376,377,1,0,0,0,377,79,1,0,0,0,378,376,
        1,0,0,0,42,83,91,95,102,106,109,121,125,133,135,141,146,158,163,
        174,178,183,195,211,217,221,241,248,254,256,267,271,276,279,283,
        289,296,307,309,313,318,322,326,331,339,371,376
    ]

class BatchParser ( Parser ):

    grammarFileName = "BatchParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'@'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'&'", "'|'", "'&&'", "'||'", 
                     "'>'", "'<'", "'=='", "':'", "'/'", "'='", "','", "'.'", 
                     "'\\'", "'+'", "'-'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'^'", "'*'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'%'" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "REM", "LABEL", "AT", 
                      "FOR", "IF", "CALL", "GOTO", "SET", "SETLOCAL", "ENDLOCAL", 
                      "DO", "IN", "EXIST", "DEFINED", "NOT", "ERRORLEVEL", 
                      "ELSE", "EXIT", "SHIFT", "EOF_KW", "LPAREN", "RPAREN", 
                      "AMP", "PIPE", "AMPAMP", "PIPEPIPE", "GT", "LT", "EQ", 
                      "COLON", "SLASH", "EQUALS", "COMMA", "DOT", "BACKSLASH", 
                      "PLUS", "MINUS", "EQU", "NEQ", "LSS", "LEQ", "GTR", 
                      "GEQ", "CARET", "ASTERISK", "CARET_ESCAPE", "DQ_STRING", 
                      "SQ_STRING", "BACKTICK_STRING", "PERCENT_TILDE", "PERCENT_VAR_SUBSTRING", 
                      "PERCENT_VAR_REPLACE", "PERCENT_VAR", "PERCENT_ARG", 
                      "FOR_VAR", "FOR_VAR_TILDE", "BANG_VAR", "PERCENT", 
                      "WORD", "NUMBER", "WS", "NEWLINE", "UNMATCHED_DQ" ]

    RULE_script = 0
    RULE_line = 1
    RULE_label = 2
    RULE_commandLine = 3
    RULE_statement = 4
    RULE_exitStmt = 5
    RULE_exitTail = 6
    RULE_shiftStmt = 7
    RULE_ifStmt = 8
    RULE_ifIOpt = 9
    RULE_ifBody = 10
    RULE_elseClause = 11
    RULE_ifErrorlevelStmt = 12
    RULE_ifExistOperand = 13
    RULE_ifPredicate = 14
    RULE_comparison = 15
    RULE_compareOp = 16
    RULE_compareOperand = 17
    RULE_forStmt = 18
    RULE_forSlashMod = 19
    RULE_forFOptions = 20
    RULE_forBody = 21
    RULE_forList = 22
    RULE_forListItem = 23
    RULE_callStmt = 24
    RULE_callTarget = 25
    RULE_gotoStmt = 26
    RULE_setStmt = 27
    RULE_setMode = 28
    RULE_setAssign = 29
    RULE_setlocalStmt = 30
    RULE_setlocalRest = 31
    RULE_endlocalStmt = 32
    RULE_setTarget = 33
    RULE_setRest = 34
    RULE_genericCmd = 35
    RULE_commandTail = 36
    RULE_argWord = 37
    RULE_token = 38
    RULE_block = 39

    ruleNames =  [ "script", "line", "label", "commandLine", "statement", 
                   "exitStmt", "exitTail", "shiftStmt", "ifStmt", "ifIOpt", 
                   "ifBody", "elseClause", "ifErrorlevelStmt", "ifExistOperand", 
                   "ifPredicate", "comparison", "compareOp", "compareOperand", 
                   "forStmt", "forSlashMod", "forFOptions", "forBody", "forList", 
                   "forListItem", "callStmt", "callTarget", "gotoStmt", 
                   "setStmt", "setMode", "setAssign", "setlocalStmt", "setlocalRest", 
                   "endlocalStmt", "setTarget", "setRest", "genericCmd", 
                   "commandTail", "argWord", "token", "block" ]

    EOF = Token.EOF
    LINE_COMMENT=1
    REM=2
    LABEL=3
    AT=4
    FOR=5
    IF=6
    CALL=7
    GOTO=8
    SET=9
    SETLOCAL=10
    ENDLOCAL=11
    DO=12
    IN=13
    EXIST=14
    DEFINED=15
    NOT=16
    ERRORLEVEL=17
    ELSE=18
    EXIT=19
    SHIFT=20
    EOF_KW=21
    LPAREN=22
    RPAREN=23
    AMP=24
    PIPE=25
    AMPAMP=26
    PIPEPIPE=27
    GT=28
    LT=29
    EQ=30
    COLON=31
    SLASH=32
    EQUALS=33
    COMMA=34
    DOT=35
    BACKSLASH=36
    PLUS=37
    MINUS=38
    EQU=39
    NEQ=40
    LSS=41
    LEQ=42
    GTR=43
    GEQ=44
    CARET=45
    ASTERISK=46
    CARET_ESCAPE=47
    DQ_STRING=48
    SQ_STRING=49
    BACKTICK_STRING=50
    PERCENT_TILDE=51
    PERCENT_VAR_SUBSTRING=52
    PERCENT_VAR_REPLACE=53
    PERCENT_VAR=54
    PERCENT_ARG=55
    FOR_VAR=56
    FOR_VAR_TILDE=57
    BANG_VAR=58
    PERCENT=59
    WORD=60
    NUMBER=61
    WS=62
    NEWLINE=63
    UNMATCHED_DQ=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    def _notForToken(self) -> bool:
        from BatchLexer import BatchLexer  # isort: skip
        return self._input.LA(1) != BatchLexer.FOR



    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BatchParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.LineContext)
            else:
                return self.getTypedRuleContext(BatchParser.LineContext,i)


        def getRuleIndex(self):
            return BatchParser.RULE_script

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = BatchParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 80
                    self.line() 
                self.state = 85
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 86
            self.match(BatchParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def label(self):
            return self.getTypedRuleContext(BatchParser.LabelContext,0)


        def commandLine(self):
            return self.getTypedRuleContext(BatchParser.CommandLineContext,0)


        def NEWLINE(self):
            return self.getToken(BatchParser.NEWLINE, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = BatchParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.label()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.commandLine()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.match(BatchParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL(self):
            return self.getToken(BatchParser.LABEL, 0)

        def NEWLINE(self):
            return self.getToken(BatchParser.NEWLINE, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = BatchParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(BatchParser.LABEL)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 94
                self.match(BatchParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.StatementContext)
            else:
                return self.getTypedRuleContext(BatchParser.StatementContext,i)


        def NEWLINE(self):
            return self.getToken(BatchParser.NEWLINE, 0)

        def AMP(self, i:int=None):
            if i is None:
                return self.getTokens(BatchParser.AMP)
            else:
                return self.getToken(BatchParser.AMP, i)

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(BatchParser.PIPE)
            else:
                return self.getToken(BatchParser.PIPE, i)

        def AMPAMP(self, i:int=None):
            if i is None:
                return self.getTokens(BatchParser.AMPAMP)
            else:
                return self.getToken(BatchParser.AMPAMP, i)

        def PIPEPIPE(self, i:int=None):
            if i is None:
                return self.getTokens(BatchParser.PIPEPIPE)
            else:
                return self.getToken(BatchParser.PIPEPIPE, i)

        def getRuleIndex(self):
            return BatchParser.RULE_commandLine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandLine" ):
                return visitor.visitCommandLine(self)
            else:
                return visitor.visitChildren(self)




    def commandLine(self):

        localctx = BatchParser.CommandLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_commandLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.statement()
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658240) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 99
                    self.statement() 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 105
                self.match(BatchParser.NEWLINE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStmt(self):
            return self.getTypedRuleContext(BatchParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BatchParser.ForStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(BatchParser.CallStmtContext,0)


        def gotoStmt(self):
            return self.getTypedRuleContext(BatchParser.GotoStmtContext,0)


        def setStmt(self):
            return self.getTypedRuleContext(BatchParser.SetStmtContext,0)


        def setlocalStmt(self):
            return self.getTypedRuleContext(BatchParser.SetlocalStmtContext,0)


        def endlocalStmt(self):
            return self.getTypedRuleContext(BatchParser.EndlocalStmtContext,0)


        def exitStmt(self):
            return self.getTypedRuleContext(BatchParser.ExitStmtContext,0)


        def shiftStmt(self):
            return self.getTypedRuleContext(BatchParser.ShiftStmtContext,0)


        def genericCmd(self):
            return self.getTypedRuleContext(BatchParser.GenericCmdContext,0)


        def AT(self):
            return self.getToken(BatchParser.AT, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BatchParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 108
                self.match(BatchParser.AT)


            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 111
                self.ifStmt()
                pass

            elif la_ == 2:
                self.state = 112
                self.forStmt()
                pass

            elif la_ == 3:
                self.state = 113
                self.callStmt()
                pass

            elif la_ == 4:
                self.state = 114
                self.gotoStmt()
                pass

            elif la_ == 5:
                self.state = 115
                self.setStmt()
                pass

            elif la_ == 6:
                self.state = 116
                self.setlocalStmt()
                pass

            elif la_ == 7:
                self.state = 117
                self.endlocalStmt()
                pass

            elif la_ == 8:
                self.state = 118
                self.exitStmt()
                pass

            elif la_ == 9:
                self.state = 119
                self.shiftStmt()
                pass

            elif la_ == 10:
                self.state = 120
                self.genericCmd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExitStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXIT(self):
            return self.getToken(BatchParser.EXIT, 0)

        def exitTail(self):
            return self.getTypedRuleContext(BatchParser.ExitTailContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_exitStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExitStmt" ):
                return visitor.visitExitStmt(self)
            else:
                return visitor.visitChildren(self)




    def exitStmt(self):

        localctx = BatchParser.ExitStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exitStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(BatchParser.EXIT)
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 124
                self.exitTail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExitTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(BatchParser.SLASH, 0)

        def WORD(self):
            return self.getToken(BatchParser.WORD, 0)

        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def token(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.TokenContext)
            else:
                return self.getTypedRuleContext(BatchParser.TokenContext,i)


        def getRuleIndex(self):
            return BatchParser.RULE_exitTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExitTail" ):
                return visitor.visitExitTail(self)
            else:
                return visitor.visitChildren(self)




    def exitTail(self):

        localctx = BatchParser.ExitTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exitTail)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(BatchParser.SLASH)
                self.state = 128
                self.match(BatchParser.WORD)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 131 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 130
                        self.token()

                    else:
                        raise NoViableAltException(self)
                    self.state = 133 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShiftStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHIFT(self):
            return self.getToken(BatchParser.SHIFT, 0)

        def token(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.TokenContext)
            else:
                return self.getTypedRuleContext(BatchParser.TokenContext,i)


        def getRuleIndex(self):
            return BatchParser.RULE_shiftStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftStmt" ):
                return visitor.visitShiftStmt(self)
            else:
                return visitor.visitChildren(self)




    def shiftStmt(self):

        localctx = BatchParser.ShiftStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_shiftStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BatchParser.SHIFT)
            self.state = 141
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 138
                    self.token() 
                self.state = 143
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BatchParser.IF, 0)

        def ifBody(self):
            return self.getTypedRuleContext(BatchParser.IfBodyContext,0)


        def ifIOpt(self):
            return self.getTypedRuleContext(BatchParser.IfIOptContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = BatchParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(BatchParser.IF)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 145
                self.ifIOpt()


            self.state = 148
            self.ifBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfIOptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(BatchParser.SLASH, 0)

        def WORD(self):
            return self.getToken(BatchParser.WORD, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_ifIOpt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfIOpt" ):
                return visitor.visitIfIOpt(self)
            else:
                return visitor.visitChildren(self)




    def ifIOpt(self):

        localctx = BatchParser.IfIOptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifIOpt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(BatchParser.SLASH)
            self.state = 151
            self.match(BatchParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifPredicate(self):
            return self.getTypedRuleContext(BatchParser.IfPredicateContext,0)


        def LPAREN(self):
            return self.getToken(BatchParser.LPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(BatchParser.BlockContext,0)


        def RPAREN(self):
            return self.getToken(BatchParser.RPAREN, 0)

        def elseClause(self):
            return self.getTypedRuleContext(BatchParser.ElseClauseContext,0)


        def statement(self):
            return self.getTypedRuleContext(BatchParser.StatementContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_ifBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBody" ):
                return visitor.visitIfBody(self)
            else:
                return visitor.visitChildren(self)




    def ifBody(self):

        localctx = BatchParser.IfBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifBody)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.ifPredicate()
                self.state = 154
                self.match(BatchParser.LPAREN)
                self.state = 155
                self.block()
                self.state = 156
                self.match(BatchParser.RPAREN)
                self.state = 158
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 157
                    self.elseClause()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.ifPredicate()
                self.state = 161
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BatchParser.ELSE, 0)

        def ifBody(self):
            return self.getTypedRuleContext(BatchParser.IfBodyContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_elseClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseClause" ):
                return visitor.visitElseClause(self)
            else:
                return visitor.visitChildren(self)




    def elseClause(self):

        localctx = BatchParser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(BatchParser.ELSE)
            self.state = 166
            self.ifBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfErrorlevelStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ERRORLEVEL(self):
            return self.getToken(BatchParser.ERRORLEVEL, 0)

        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_ifErrorlevelStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfErrorlevelStmt" ):
                return visitor.visitIfErrorlevelStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifErrorlevelStmt(self):

        localctx = BatchParser.IfErrorlevelStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifErrorlevelStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(BatchParser.ERRORLEVEL)
            self.state = 169
            self.match(BatchParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfExistOperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQ_STRING(self):
            return self.getToken(BatchParser.DQ_STRING, 0)

        def WORD(self):
            return self.getToken(BatchParser.WORD, 0)

        def PERCENT_VAR(self):
            return self.getToken(BatchParser.PERCENT_VAR, 0)

        def PERCENT_TILDE(self):
            return self.getToken(BatchParser.PERCENT_TILDE, 0)

        def PERCENT_ARG(self):
            return self.getToken(BatchParser.PERCENT_ARG, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_ifExistOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExistOperand" ):
                return visitor.visitIfExistOperand(self)
            else:
                return visitor.visitChildren(self)




    def ifExistOperand(self):

        localctx = BatchParser.IfExistOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifExistOperand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1209497974925688832) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfPredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifErrorlevelStmt(self):
            return self.getTypedRuleContext(BatchParser.IfErrorlevelStmtContext,0)


        def NOT(self):
            return self.getToken(BatchParser.NOT, 0)

        def DEFINED(self):
            return self.getToken(BatchParser.DEFINED, 0)

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def EXIST(self):
            return self.getToken(BatchParser.EXIST, 0)

        def ifExistOperand(self):
            return self.getTypedRuleContext(BatchParser.IfExistOperandContext,0)


        def comparison(self):
            return self.getTypedRuleContext(BatchParser.ComparisonContext,0)


        def PERCENT_VAR(self):
            return self.getToken(BatchParser.PERCENT_VAR, 0)

        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def DQ_STRING(self):
            return self.getToken(BatchParser.DQ_STRING, 0)

        def PERCENT_TILDE(self):
            return self.getToken(BatchParser.PERCENT_TILDE, 0)

        def PERCENT_ARG(self):
            return self.getToken(BatchParser.PERCENT_ARG, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_ifPredicate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfPredicate" ):
                return visitor.visitIfPredicate(self)
            else:
                return visitor.visitChildren(self)




    def ifPredicate(self):

        localctx = BatchParser.IfPredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifPredicate)
        self._la = 0 # Token type
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 173
                    self.match(BatchParser.NOT)


                self.state = 176
                self.ifErrorlevelStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 177
                    self.match(BatchParser.NOT)


                self.state = 180
                self.match(BatchParser.DEFINED)
                self.state = 181
                self.argWord()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 182
                    self.match(BatchParser.NOT)


                self.state = 185
                self.match(BatchParser.EXIST)
                self.state = 186
                self.ifExistOperand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.comparison()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 188
                self.match(BatchParser.PERCENT_VAR)
                self.state = 189
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.match(BatchParser.DQ_STRING)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 191
                self.match(BatchParser.PERCENT_TILDE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 192
                self.match(BatchParser.PERCENT_VAR)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 193
                self.match(BatchParser.PERCENT_ARG)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 194
                self.argWord()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compareOperand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.CompareOperandContext)
            else:
                return self.getTypedRuleContext(BatchParser.CompareOperandContext,i)


        def compareOp(self):
            return self.getTypedRuleContext(BatchParser.CompareOpContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = BatchParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.compareOperand()
            self.state = 198
            self.compareOp()
            self.state = 199
            self.compareOperand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(BatchParser.EQ, 0)

        def EQU(self):
            return self.getToken(BatchParser.EQU, 0)

        def NEQ(self):
            return self.getToken(BatchParser.NEQ, 0)

        def LSS(self):
            return self.getToken(BatchParser.LSS, 0)

        def LEQ(self):
            return self.getToken(BatchParser.LEQ, 0)

        def GTR(self):
            return self.getToken(BatchParser.GTR, 0)

        def GEQ(self):
            return self.getToken(BatchParser.GEQ, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_compareOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareOp" ):
                return visitor.visitCompareOp(self)
            else:
                return visitor.visitChildren(self)




    def compareOp(self):

        localctx = BatchParser.CompareOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_compareOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34635690016768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareOperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQ_STRING(self):
            return self.getToken(BatchParser.DQ_STRING, 0)

        def PERCENT_TILDE(self):
            return self.getToken(BatchParser.PERCENT_TILDE, 0)

        def PERCENT_VAR_SUBSTRING(self):
            return self.getToken(BatchParser.PERCENT_VAR_SUBSTRING, 0)

        def PERCENT_VAR_REPLACE(self):
            return self.getToken(BatchParser.PERCENT_VAR_REPLACE, 0)

        def PERCENT_VAR(self):
            return self.getToken(BatchParser.PERCENT_VAR, 0)

        def PERCENT_ARG(self):
            return self.getToken(BatchParser.PERCENT_ARG, 0)

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_compareOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareOperand" ):
                return visitor.visitCompareOperand(self)
            else:
                return visitor.visitChildren(self)




    def compareOperand(self):

        localctx = BatchParser.CompareOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_compareOperand)
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(BatchParser.DQ_STRING)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(BatchParser.PERCENT_TILDE)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.match(BatchParser.PERCENT_VAR_SUBSTRING)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 4)
                self.state = 206
                self.match(BatchParser.PERCENT_VAR_REPLACE)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 5)
                self.state = 207
                self.match(BatchParser.PERCENT_VAR)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 6)
                self.state = 208
                self.match(BatchParser.PERCENT_ARG)
                pass
            elif token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 60]:
                self.enterOuterAlt(localctx, 7)
                self.state = 209
                self.argWord()
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 8)
                self.state = 210
                self.match(BatchParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BatchParser.FOR, 0)

        def FOR_VAR(self):
            return self.getToken(BatchParser.FOR_VAR, 0)

        def IN(self):
            return self.getToken(BatchParser.IN, 0)

        def LPAREN(self):
            return self.getToken(BatchParser.LPAREN, 0)

        def forList(self):
            return self.getTypedRuleContext(BatchParser.ForListContext,0)


        def RPAREN(self):
            return self.getToken(BatchParser.RPAREN, 0)

        def DO(self):
            return self.getToken(BatchParser.DO, 0)

        def forBody(self):
            return self.getTypedRuleContext(BatchParser.ForBodyContext,0)


        def forSlashMod(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.ForSlashModContext)
            else:
                return self.getTypedRuleContext(BatchParser.ForSlashModContext,i)


        def forFOptions(self):
            return self.getTypedRuleContext(BatchParser.ForFOptionsContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BatchParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(BatchParser.FOR)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 214
                self.forSlashMod()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 220
                self.forFOptions()


            self.state = 223
            self.match(BatchParser.FOR_VAR)
            self.state = 224
            self.match(BatchParser.IN)
            self.state = 225
            self.match(BatchParser.LPAREN)
            self.state = 226
            self.forList()
            self.state = 227
            self.match(BatchParser.RPAREN)
            self.state = 228
            self.match(BatchParser.DO)
            self.state = 229
            self.forBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForSlashModContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(BatchParser.SLASH, 0)

        def WORD(self):
            return self.getToken(BatchParser.WORD, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_forSlashMod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForSlashMod" ):
                return visitor.visitForSlashMod(self)
            else:
                return visitor.visitChildren(self)




    def forSlashMod(self):

        localctx = BatchParser.ForSlashModContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_forSlashMod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(BatchParser.SLASH)
            self.state = 232
            self.match(BatchParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForFOptionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQ_STRING(self):
            return self.getToken(BatchParser.DQ_STRING, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_forFOptions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForFOptions" ):
                return visitor.visitForFOptions(self)
            else:
                return visitor.visitChildren(self)




    def forFOptions(self):

        localctx = BatchParser.ForFOptionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_forFOptions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BatchParser.DQ_STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BatchParser.LPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(BatchParser.BlockContext,0)


        def RPAREN(self):
            return self.getToken(BatchParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(BatchParser.StatementContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_forBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForBody" ):
                return visitor.visitForBody(self)
            else:
                return visitor.visitChildren(self)




    def forBody(self):

        localctx = BatchParser.ForBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_forBody)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(BatchParser.LPAREN)
                self.state = 237
                self.block()
                self.state = 238
                self.match(BatchParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forListItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.ForListItemContext)
            else:
                return self.getTypedRuleContext(BatchParser.ForListItemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BatchParser.COMMA)
            else:
                return self.getToken(BatchParser.COMMA, i)

        def getRuleIndex(self):
            return BatchParser.RULE_forList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForList" ):
                return visitor.visitForList(self)
            else:
                return visitor.visitChildren(self)




    def forList(self):

        localctx = BatchParser.ForListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forList)
        self._la = 0 # Token type
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.forListItem()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 244
                    self.match(BatchParser.COMMA)
                    self.state = 245
                    self.forListItem()
                    self.state = 250
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 251
                    self.forListItem()
                    self.state = 254 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3517100202745921504) != 0)):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForListItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_STRING(self):
            return self.getToken(BatchParser.SQ_STRING, 0)

        def DQ_STRING(self):
            return self.getToken(BatchParser.DQ_STRING, 0)

        def BACKTICK_STRING(self):
            return self.getToken(BatchParser.BACKTICK_STRING, 0)

        def PERCENT_VAR(self):
            return self.getToken(BatchParser.PERCENT_VAR, 0)

        def PERCENT_TILDE(self):
            return self.getToken(BatchParser.PERCENT_TILDE, 0)

        def PERCENT_ARG(self):
            return self.getToken(BatchParser.PERCENT_ARG, 0)

        def ASTERISK(self):
            return self.getToken(BatchParser.ASTERISK, 0)

        def DOT(self):
            return self.getToken(BatchParser.DOT, 0)

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_forListItem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForListItem" ):
                return visitor.visitForListItem(self)
            else:
                return visitor.visitChildren(self)




    def forListItem(self):

        localctx = BatchParser.ForListItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forListItem)
        self._la = 0 # Token type
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(BatchParser.SQ_STRING)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(BatchParser.DQ_STRING)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
                self.match(BatchParser.BACKTICK_STRING)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 4)
                self.state = 261
                self.match(BatchParser.PERCENT_VAR)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 5)
                self.state = 262
                self.match(BatchParser.PERCENT_TILDE)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 6)
                self.state = 263
                self.match(BatchParser.PERCENT_ARG)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 7)
                self.state = 264
                self.match(BatchParser.ASTERISK)
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 265
                    self.match(BatchParser.DOT)
                    self.state = 266
                    self.argWord()


                pass
            elif token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 60]:
                self.enterOuterAlt(localctx, 8)
                self.state = 269
                self.argWord()
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 9)
                self.state = 270
                self.match(BatchParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL(self):
            return self.getToken(BatchParser.CALL, 0)

        def callTarget(self):
            return self.getTypedRuleContext(BatchParser.CallTargetContext,0)


        def commandTail(self):
            return self.getTypedRuleContext(BatchParser.CommandTailContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_callStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStmt" ):
                return visitor.visitCallStmt(self)
            else:
                return visitor.visitChildren(self)




    def callStmt(self):

        localctx = BatchParser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_callStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(BatchParser.CALL)
            self.state = 274
            self.callTarget()
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 275
                self.commandTail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF_KW(self):
            return self.getToken(BatchParser.EOF_KW, 0)

        def COLON(self):
            return self.getToken(BatchParser.COLON, 0)

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def PERCENT_ARG(self):
            return self.getToken(BatchParser.PERCENT_ARG, 0)

        def PERCENT_VAR(self):
            return self.getToken(BatchParser.PERCENT_VAR, 0)

        def DQ_STRING(self):
            return self.getToken(BatchParser.DQ_STRING, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_callTarget

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallTarget" ):
                return visitor.visitCallTarget(self)
            else:
                return visitor.visitChildren(self)




    def callTarget(self):

        localctx = BatchParser.CallTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_callTarget)
        self._la = 0 # Token type
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 278
                    self.match(BatchParser.COLON)


                self.state = 281
                self.match(BatchParser.EOF_KW)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31:
                    self.state = 282
                    self.match(BatchParser.COLON)


                self.state = 285
                self.argWord()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.match(BatchParser.PERCENT_ARG)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 287
                self.match(BatchParser.PERCENT_VAR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 288
                self.match(BatchParser.DQ_STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GOTO(self):
            return self.getToken(BatchParser.GOTO, 0)

        def callTarget(self):
            return self.getTypedRuleContext(BatchParser.CallTargetContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_gotoStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGotoStmt" ):
                return visitor.visitGotoStmt(self)
            else:
                return visitor.visitChildren(self)




    def gotoStmt(self):

        localctx = BatchParser.GotoStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_gotoStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(BatchParser.GOTO)
            self.state = 292
            self.callTarget()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(BatchParser.SET, 0)

        def setAssign(self):
            return self.getTypedRuleContext(BatchParser.SetAssignContext,0)


        def setMode(self):
            return self.getTypedRuleContext(BatchParser.SetModeContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_setStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetStmt" ):
                return visitor.visitSetStmt(self)
            else:
                return visitor.visitChildren(self)




    def setStmt(self):

        localctx = BatchParser.SetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_setStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(BatchParser.SET)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 295
                self.setMode()


            self.state = 298
            self.setAssign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetModeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(BatchParser.SLASH, 0)

        def WORD(self):
            return self.getToken(BatchParser.WORD, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_setMode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetMode" ):
                return visitor.visitSetMode(self)
            else:
                return visitor.visitChildren(self)




    def setMode(self):

        localctx = BatchParser.SetModeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_setMode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(BatchParser.SLASH)
            self.state = 301
            self.match(BatchParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQ_STRING(self):
            return self.getToken(BatchParser.DQ_STRING, 0)

        def setTarget(self):
            return self.getTypedRuleContext(BatchParser.SetTargetContext,0)


        def EQUALS(self):
            return self.getToken(BatchParser.EQUALS, 0)

        def setRest(self):
            return self.getTypedRuleContext(BatchParser.SetRestContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_setAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetAssign" ):
                return visitor.visitSetAssign(self)
            else:
                return visitor.visitChildren(self)




    def setAssign(self):

        localctx = BatchParser.SetAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_setAssign)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(BatchParser.DQ_STRING)
                pass
            elif token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 54, 60]:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.setTarget()
                self.state = 305
                self.match(BatchParser.EQUALS)
                self.state = 307
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 306
                    self.setRest()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetlocalStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SETLOCAL(self):
            return self.getToken(BatchParser.SETLOCAL, 0)

        def setlocalRest(self):
            return self.getTypedRuleContext(BatchParser.SetlocalRestContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_setlocalStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetlocalStmt" ):
                return visitor.visitSetlocalStmt(self)
            else:
                return visitor.visitChildren(self)




    def setlocalStmt(self):

        localctx = BatchParser.SetlocalStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_setlocalStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(BatchParser.SETLOCAL)
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 312
                self.setlocalRest()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetlocalRestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def token(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.TokenContext)
            else:
                return self.getTypedRuleContext(BatchParser.TokenContext,i)


        def getRuleIndex(self):
            return BatchParser.RULE_setlocalRest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetlocalRest" ):
                return visitor.visitSetlocalRest(self)
            else:
                return visitor.visitChildren(self)




    def setlocalRest(self):

        localctx = BatchParser.SetlocalRestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_setlocalRest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 315
                    self.token()

                else:
                    raise NoViableAltException(self)
                self.state = 318 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndlocalStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENDLOCAL(self):
            return self.getToken(BatchParser.ENDLOCAL, 0)

        def commandTail(self):
            return self.getTypedRuleContext(BatchParser.CommandTailContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_endlocalStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndlocalStmt" ):
                return visitor.visitEndlocalStmt(self)
            else:
                return visitor.visitChildren(self)




    def endlocalStmt(self):

        localctx = BatchParser.EndlocalStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_endlocalStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(BatchParser.ENDLOCAL)
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 321
                self.commandTail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetTargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def PERCENT_VAR(self):
            return self.getToken(BatchParser.PERCENT_VAR, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_setTarget

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetTarget" ):
                return visitor.visitSetTarget(self)
            else:
                return visitor.visitChildren(self)




    def setTarget(self):

        localctx = BatchParser.SetTargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_setTarget)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 60]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                self.argWord()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(BatchParser.PERCENT_VAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetRestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def token(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.TokenContext)
            else:
                return self.getTypedRuleContext(BatchParser.TokenContext,i)


        def getRuleIndex(self):
            return BatchParser.RULE_setRest

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetRest" ):
                return visitor.visitSetRest(self)
            else:
                return visitor.visitChildren(self)




    def setRest(self):

        localctx = BatchParser.SetRestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_setRest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 328
                    self.token()

                else:
                    raise NoViableAltException(self)
                self.state = 331 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenericCmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commandTail(self):
            return self.getTypedRuleContext(BatchParser.CommandTailContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_genericCmd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenericCmd" ):
                return visitor.visitGenericCmd(self)
            else:
                return visitor.visitChildren(self)




    def genericCmd(self):

        localctx = BatchParser.GenericCmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_genericCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            if not self._notForToken():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._notForToken()")
            self.state = 334
            self.commandTail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def token(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.TokenContext)
            else:
                return self.getTypedRuleContext(BatchParser.TokenContext,i)


        def getRuleIndex(self):
            return BatchParser.RULE_commandTail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandTail" ):
                return visitor.visitCommandTail(self)
            else:
                return visitor.visitChildren(self)




    def commandTail(self):

        localctx = BatchParser.CommandTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_commandTail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 336
                    self.token()

                else:
                    raise NoViableAltException(self)
                self.state = 339 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(BatchParser.WORD, 0)

        def FOR(self):
            return self.getToken(BatchParser.FOR, 0)

        def IF(self):
            return self.getToken(BatchParser.IF, 0)

        def SET(self):
            return self.getToken(BatchParser.SET, 0)

        def DO(self):
            return self.getToken(BatchParser.DO, 0)

        def IN(self):
            return self.getToken(BatchParser.IN, 0)

        def EXIST(self):
            return self.getToken(BatchParser.EXIST, 0)

        def DEFINED(self):
            return self.getToken(BatchParser.DEFINED, 0)

        def NOT(self):
            return self.getToken(BatchParser.NOT, 0)

        def ERRORLEVEL(self):
            return self.getToken(BatchParser.ERRORLEVEL, 0)

        def ELSE(self):
            return self.getToken(BatchParser.ELSE, 0)

        def EXIT(self):
            return self.getToken(BatchParser.EXIT, 0)

        def SHIFT(self):
            return self.getToken(BatchParser.SHIFT, 0)

        def CALL(self):
            return self.getToken(BatchParser.CALL, 0)

        def GOTO(self):
            return self.getToken(BatchParser.GOTO, 0)

        def ENDLOCAL(self):
            return self.getToken(BatchParser.ENDLOCAL, 0)

        def SETLOCAL(self):
            return self.getToken(BatchParser.SETLOCAL, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_argWord

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgWord" ):
                return visitor.visitArgWord(self)
            else:
                return visitor.visitChildren(self)




    def argWord(self):

        localctx = BatchParser.ArgWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_argWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1152921504608944096) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQ_STRING(self):
            return self.getToken(BatchParser.DQ_STRING, 0)

        def SQ_STRING(self):
            return self.getToken(BatchParser.SQ_STRING, 0)

        def BACKTICK_STRING(self):
            return self.getToken(BatchParser.BACKTICK_STRING, 0)

        def PERCENT_TILDE(self):
            return self.getToken(BatchParser.PERCENT_TILDE, 0)

        def PERCENT_VAR_SUBSTRING(self):
            return self.getToken(BatchParser.PERCENT_VAR_SUBSTRING, 0)

        def PERCENT_VAR_REPLACE(self):
            return self.getToken(BatchParser.PERCENT_VAR_REPLACE, 0)

        def PERCENT_VAR(self):
            return self.getToken(BatchParser.PERCENT_VAR, 0)

        def PERCENT_ARG(self):
            return self.getToken(BatchParser.PERCENT_ARG, 0)

        def FOR_VAR(self):
            return self.getToken(BatchParser.FOR_VAR, 0)

        def FOR_VAR_TILDE(self):
            return self.getToken(BatchParser.FOR_VAR_TILDE, 0)

        def BANG_VAR(self):
            return self.getToken(BatchParser.BANG_VAR, 0)

        def CARET_ESCAPE(self):
            return self.getToken(BatchParser.CARET_ESCAPE, 0)

        def CARET(self):
            return self.getToken(BatchParser.CARET, 0)

        def LPAREN(self):
            return self.getToken(BatchParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BatchParser.RPAREN, 0)

        def GT(self):
            return self.getToken(BatchParser.GT, 0)

        def LT(self):
            return self.getToken(BatchParser.LT, 0)

        def DOT(self):
            return self.getToken(BatchParser.DOT, 0)

        def BACKSLASH(self):
            return self.getToken(BatchParser.BACKSLASH, 0)

        def PLUS(self):
            return self.getToken(BatchParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(BatchParser.MINUS, 0)

        def COMMA(self):
            return self.getToken(BatchParser.COMMA, 0)

        def EQUALS(self):
            return self.getToken(BatchParser.EQUALS, 0)

        def SLASH(self):
            return self.getToken(BatchParser.SLASH, 0)

        def PERCENT(self):
            return self.getToken(BatchParser.PERCENT, 0)

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def UNMATCHED_DQ(self):
            return self.getToken(BatchParser.UNMATCHED_DQ, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_token

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToken" ):
                return visitor.visitToken(self)
            else:
                return visitor.visitChildren(self)




    def token(self):

        localctx = BatchParser.TokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_token)
        try:
            self.state = 371
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(BatchParser.DQ_STRING)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.match(BatchParser.SQ_STRING)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.match(BatchParser.BACKTICK_STRING)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 4)
                self.state = 346
                self.match(BatchParser.PERCENT_TILDE)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 5)
                self.state = 347
                self.match(BatchParser.PERCENT_VAR_SUBSTRING)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 6)
                self.state = 348
                self.match(BatchParser.PERCENT_VAR_REPLACE)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 7)
                self.state = 349
                self.match(BatchParser.PERCENT_VAR)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 8)
                self.state = 350
                self.match(BatchParser.PERCENT_ARG)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 9)
                self.state = 351
                self.match(BatchParser.FOR_VAR)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 10)
                self.state = 352
                self.match(BatchParser.FOR_VAR_TILDE)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 11)
                self.state = 353
                self.match(BatchParser.BANG_VAR)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 12)
                self.state = 354
                self.match(BatchParser.CARET_ESCAPE)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 13)
                self.state = 355
                self.match(BatchParser.CARET)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 14)
                self.state = 356
                self.match(BatchParser.LPAREN)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 15)
                self.state = 357
                self.match(BatchParser.RPAREN)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 16)
                self.state = 358
                self.match(BatchParser.GT)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 17)
                self.state = 359
                self.match(BatchParser.LT)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 18)
                self.state = 360
                self.match(BatchParser.DOT)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 19)
                self.state = 361
                self.match(BatchParser.BACKSLASH)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 20)
                self.state = 362
                self.match(BatchParser.PLUS)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 21)
                self.state = 363
                self.match(BatchParser.MINUS)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 22)
                self.state = 364
                self.match(BatchParser.COMMA)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 23)
                self.state = 365
                self.match(BatchParser.EQUALS)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 24)
                self.state = 366
                self.match(BatchParser.SLASH)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 25)
                self.state = 367
                self.match(BatchParser.PERCENT)
                pass
            elif token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 60]:
                self.enterOuterAlt(localctx, 26)
                self.state = 368
                self.argWord()
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 27)
                self.state = 369
                self.match(BatchParser.NUMBER)
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 28)
                self.state = 370
                self.match(BatchParser.UNMATCHED_DQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.LineContext)
            else:
                return self.getTypedRuleContext(BatchParser.LineContext,i)


        def getRuleIndex(self):
            return BatchParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = BatchParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 373
                    self.line() 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[35] = self.genericCmd_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def genericCmd_sempred(self, localctx:GenericCmdContext, predIndex:int):
            if predIndex == 0:
                return self._notForToken()
         




