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
        4,1,74,486,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        5,0,94,8,0,10,0,12,0,97,9,0,1,0,1,0,1,1,1,1,1,1,3,1,104,8,1,1,2,
        1,2,3,2,108,8,2,1,3,1,3,1,3,5,3,113,8,3,10,3,12,3,116,9,3,1,3,3,
        3,119,8,3,1,4,3,4,122,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,135,8,4,1,5,1,5,3,5,139,8,5,1,6,1,6,1,6,3,6,144,8,6,1,
        6,1,6,4,6,148,8,6,11,6,12,6,149,3,6,152,8,6,1,7,1,7,1,7,1,7,3,7,
        158,8,7,1,8,1,8,5,8,162,8,8,10,8,12,8,165,9,8,1,9,1,9,3,9,169,8,
        9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,181,8,11,
        1,11,1,11,1,11,3,11,186,8,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,
        1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,16,204,8,16,1,17,
        3,17,207,8,17,1,17,1,17,3,17,211,8,17,1,17,1,17,3,17,215,8,17,1,
        17,1,17,1,17,3,17,220,8,17,1,17,1,17,1,17,3,17,225,8,17,1,17,1,17,
        1,17,1,17,3,17,231,8,17,1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,250,8,20,1,20,
        1,20,3,20,254,8,20,1,20,3,20,257,8,20,1,21,1,21,5,21,261,8,21,10,
        21,12,21,264,9,21,1,21,3,21,267,8,21,1,21,3,21,270,8,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,3,22,282,8,22,1,23,1,23,
        1,23,1,24,1,24,1,24,5,24,290,8,24,10,24,12,24,293,9,24,3,24,295,
        8,24,1,25,1,25,1,25,1,25,3,25,301,8,25,1,26,1,26,1,26,1,26,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,3,26,314,8,26,1,27,1,27,1,27,1,27,
        1,27,3,27,321,8,27,1,28,1,28,1,28,5,28,326,8,28,10,28,12,28,329,
        9,28,1,28,4,28,332,8,28,11,28,12,28,333,3,28,336,8,28,1,29,1,29,
        1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,347,8,29,1,29,1,29,3,29,
        351,8,29,1,29,1,29,3,29,355,8,29,1,29,3,29,358,8,29,1,30,1,30,1,
        30,3,30,363,8,30,1,31,3,31,366,8,31,1,31,1,31,3,31,370,8,31,1,31,
        1,31,3,31,374,8,31,1,31,1,31,3,31,378,8,31,1,31,1,31,3,31,382,8,
        31,1,31,1,31,3,31,386,8,31,1,32,1,32,1,32,1,33,1,33,3,33,393,8,33,
        1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,35,1,35,3,35,404,8,35,3,35,
        406,8,35,1,36,1,36,3,36,410,8,36,1,37,4,37,413,8,37,11,37,12,37,
        414,1,38,1,38,3,38,419,8,38,1,39,1,39,3,39,423,8,39,1,40,4,40,426,
        8,40,11,40,12,40,427,1,41,1,41,1,41,1,42,4,42,434,8,42,11,42,12,
        42,435,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,
        44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,
        44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,
        44,1,44,1,44,3,44,478,8,44,1,45,5,45,481,8,45,10,45,12,45,484,9,
        45,1,45,0,0,46,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,84,86,88,90,0,4,1,0,25,28,4,0,53,53,56,56,59,63,67,67,2,0,
        34,34,43,48,3,0,5,21,43,48,67,67,584,0,95,1,0,0,0,2,103,1,0,0,0,
        4,105,1,0,0,0,6,109,1,0,0,0,8,121,1,0,0,0,10,136,1,0,0,0,12,151,
        1,0,0,0,14,153,1,0,0,0,16,159,1,0,0,0,18,166,1,0,0,0,20,172,1,0,
        0,0,22,185,1,0,0,0,24,187,1,0,0,0,26,190,1,0,0,0,28,193,1,0,0,0,
        30,196,1,0,0,0,32,203,1,0,0,0,34,230,1,0,0,0,36,232,1,0,0,0,38,236,
        1,0,0,0,40,256,1,0,0,0,42,258,1,0,0,0,44,281,1,0,0,0,46,283,1,0,
        0,0,48,294,1,0,0,0,50,300,1,0,0,0,52,313,1,0,0,0,54,320,1,0,0,0,
        56,335,1,0,0,0,58,357,1,0,0,0,60,359,1,0,0,0,62,385,1,0,0,0,64,387,
        1,0,0,0,66,390,1,0,0,0,68,396,1,0,0,0,70,405,1,0,0,0,72,407,1,0,
        0,0,74,412,1,0,0,0,76,416,1,0,0,0,78,422,1,0,0,0,80,425,1,0,0,0,
        82,429,1,0,0,0,84,433,1,0,0,0,86,437,1,0,0,0,88,477,1,0,0,0,90,482,
        1,0,0,0,92,94,3,2,1,0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,
        95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,99,5,0,0,1,99,1,1,0,
        0,0,100,104,3,4,2,0,101,104,3,6,3,0,102,104,5,71,0,0,103,100,1,0,
        0,0,103,101,1,0,0,0,103,102,1,0,0,0,104,3,1,0,0,0,105,107,5,3,0,
        0,106,108,5,71,0,0,107,106,1,0,0,0,107,108,1,0,0,0,108,5,1,0,0,0,
        109,114,3,8,4,0,110,111,7,0,0,0,111,113,3,8,4,0,112,110,1,0,0,0,
        113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,118,1,0,0,0,
        116,114,1,0,0,0,117,119,5,71,0,0,118,117,1,0,0,0,118,119,1,0,0,0,
        119,7,1,0,0,0,120,122,5,4,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,
        134,1,0,0,0,123,135,3,18,9,0,124,135,3,42,21,0,125,135,3,60,30,0,
        126,135,3,64,32,0,127,135,3,66,33,0,128,135,3,72,36,0,129,135,3,
        76,38,0,130,135,3,10,5,0,131,135,3,16,8,0,132,135,3,14,7,0,133,135,
        3,82,41,0,134,123,1,0,0,0,134,124,1,0,0,0,134,125,1,0,0,0,134,126,
        1,0,0,0,134,127,1,0,0,0,134,128,1,0,0,0,134,129,1,0,0,0,134,130,
        1,0,0,0,134,131,1,0,0,0,134,132,1,0,0,0,134,133,1,0,0,0,135,9,1,
        0,0,0,136,138,5,20,0,0,137,139,3,12,6,0,138,137,1,0,0,0,138,139,
        1,0,0,0,139,11,1,0,0,0,140,141,5,36,0,0,141,143,5,67,0,0,142,144,
        5,69,0,0,143,142,1,0,0,0,143,144,1,0,0,0,144,152,1,0,0,0,145,152,
        5,69,0,0,146,148,3,88,44,0,147,146,1,0,0,0,148,149,1,0,0,0,149,147,
        1,0,0,0,149,150,1,0,0,0,150,152,1,0,0,0,151,140,1,0,0,0,151,145,
        1,0,0,0,151,147,1,0,0,0,152,13,1,0,0,0,153,154,5,23,0,0,154,155,
        3,90,45,0,155,157,5,24,0,0,156,158,3,84,42,0,157,156,1,0,0,0,157,
        158,1,0,0,0,158,15,1,0,0,0,159,163,5,21,0,0,160,162,3,88,44,0,161,
        160,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,
        17,1,0,0,0,165,163,1,0,0,0,166,168,5,6,0,0,167,169,3,20,10,0,168,
        167,1,0,0,0,168,169,1,0,0,0,169,170,1,0,0,0,170,171,3,22,11,0,171,
        19,1,0,0,0,172,173,5,36,0,0,173,174,5,67,0,0,174,21,1,0,0,0,175,
        176,3,34,17,0,176,177,5,23,0,0,177,178,3,90,45,0,178,180,5,24,0,
        0,179,181,3,24,12,0,180,179,1,0,0,0,180,181,1,0,0,0,181,186,1,0,
        0,0,182,183,3,34,17,0,183,184,3,8,4,0,184,186,1,0,0,0,185,175,1,
        0,0,0,185,182,1,0,0,0,186,23,1,0,0,0,187,188,5,19,0,0,188,189,3,
        22,11,0,189,25,1,0,0,0,190,191,5,17,0,0,191,192,5,69,0,0,192,27,
        1,0,0,0,193,194,5,18,0,0,194,195,5,69,0,0,195,29,1,0,0,0,196,197,
        7,1,0,0,197,31,1,0,0,0,198,204,3,86,43,0,199,204,5,59,0,0,200,204,
        5,61,0,0,201,204,5,62,0,0,202,204,5,63,0,0,203,198,1,0,0,0,203,199,
        1,0,0,0,203,200,1,0,0,0,203,201,1,0,0,0,203,202,1,0,0,0,204,33,1,
        0,0,0,205,207,5,16,0,0,206,205,1,0,0,0,206,207,1,0,0,0,207,208,1,
        0,0,0,208,231,3,26,13,0,209,211,5,16,0,0,210,209,1,0,0,0,210,211,
        1,0,0,0,211,212,1,0,0,0,212,231,3,28,14,0,213,215,5,16,0,0,214,213,
        1,0,0,0,214,215,1,0,0,0,215,216,1,0,0,0,216,217,5,15,0,0,217,231,
        3,32,16,0,218,220,5,16,0,0,219,218,1,0,0,0,219,220,1,0,0,0,220,221,
        1,0,0,0,221,222,5,14,0,0,222,231,3,30,15,0,223,225,5,16,0,0,224,
        223,1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,226,231,3,36,18,0,227,
        231,5,53,0,0,228,231,5,56,0,0,229,231,3,86,43,0,230,206,1,0,0,0,
        230,210,1,0,0,0,230,214,1,0,0,0,230,219,1,0,0,0,230,224,1,0,0,0,
        230,227,1,0,0,0,230,228,1,0,0,0,230,229,1,0,0,0,231,35,1,0,0,0,232,
        233,3,40,20,0,233,234,3,38,19,0,234,235,3,40,20,0,235,37,1,0,0,0,
        236,237,7,2,0,0,237,39,1,0,0,0,238,257,5,53,0,0,239,257,5,56,0,0,
        240,257,5,57,0,0,241,257,5,58,0,0,242,257,5,59,0,0,243,257,5,60,
        0,0,244,257,5,61,0,0,245,257,5,62,0,0,246,257,5,63,0,0,247,257,3,
        86,43,0,248,250,5,42,0,0,249,248,1,0,0,0,249,250,1,0,0,0,250,251,
        1,0,0,0,251,257,5,69,0,0,252,254,5,42,0,0,253,252,1,0,0,0,253,254,
        1,0,0,0,254,255,1,0,0,0,255,257,5,68,0,0,256,238,1,0,0,0,256,239,
        1,0,0,0,256,240,1,0,0,0,256,241,1,0,0,0,256,242,1,0,0,0,256,243,
        1,0,0,0,256,244,1,0,0,0,256,245,1,0,0,0,256,246,1,0,0,0,256,247,
        1,0,0,0,256,249,1,0,0,0,256,253,1,0,0,0,257,41,1,0,0,0,258,262,5,
        5,0,0,259,261,3,46,23,0,260,259,1,0,0,0,261,264,1,0,0,0,262,260,
        1,0,0,0,262,263,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,265,267,
        3,48,24,0,266,265,1,0,0,0,266,267,1,0,0,0,267,269,1,0,0,0,268,270,
        3,44,22,0,269,268,1,0,0,0,269,270,1,0,0,0,270,271,1,0,0,0,271,272,
        5,61,0,0,272,273,5,13,0,0,273,274,5,23,0,0,274,275,3,56,28,0,275,
        276,5,24,0,0,276,277,5,12,0,0,277,278,3,54,27,0,278,43,1,0,0,0,279,
        282,3,86,43,0,280,282,5,53,0,0,281,279,1,0,0,0,281,280,1,0,0,0,282,
        45,1,0,0,0,283,284,5,36,0,0,284,285,5,67,0,0,285,47,1,0,0,0,286,
        295,5,53,0,0,287,291,3,50,25,0,288,290,3,52,26,0,289,288,1,0,0,0,
        290,293,1,0,0,0,291,289,1,0,0,0,291,292,1,0,0,0,292,295,1,0,0,0,
        293,291,1,0,0,0,294,286,1,0,0,0,294,287,1,0,0,0,295,49,1,0,0,0,296,
        297,3,86,43,0,297,298,5,52,0,0,298,301,1,0,0,0,299,301,5,52,0,0,
        300,296,1,0,0,0,300,299,1,0,0,0,301,51,1,0,0,0,302,303,3,86,43,0,
        303,304,5,52,0,0,304,314,1,0,0,0,305,314,5,52,0,0,306,314,5,69,0,
        0,307,314,5,38,0,0,308,314,5,50,0,0,309,314,5,42,0,0,310,314,5,41,
        0,0,311,314,5,66,0,0,312,314,3,86,43,0,313,302,1,0,0,0,313,305,1,
        0,0,0,313,306,1,0,0,0,313,307,1,0,0,0,313,308,1,0,0,0,313,309,1,
        0,0,0,313,310,1,0,0,0,313,311,1,0,0,0,313,312,1,0,0,0,314,53,1,0,
        0,0,315,316,5,23,0,0,316,317,3,90,45,0,317,318,5,24,0,0,318,321,
        1,0,0,0,319,321,3,8,4,0,320,315,1,0,0,0,320,319,1,0,0,0,321,55,1,
        0,0,0,322,327,3,58,29,0,323,324,5,38,0,0,324,326,3,58,29,0,325,323,
        1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,1,0,0,0,328,336,
        1,0,0,0,329,327,1,0,0,0,330,332,3,58,29,0,331,330,1,0,0,0,332,333,
        1,0,0,0,333,331,1,0,0,0,333,334,1,0,0,0,334,336,1,0,0,0,335,322,
        1,0,0,0,335,331,1,0,0,0,336,57,1,0,0,0,337,358,5,54,0,0,338,358,
        5,53,0,0,339,358,5,55,0,0,340,358,5,59,0,0,341,358,5,56,0,0,342,
        358,5,60,0,0,343,346,5,50,0,0,344,345,5,39,0,0,345,347,3,86,43,0,
        346,344,1,0,0,0,346,347,1,0,0,0,347,358,1,0,0,0,348,358,3,86,43,
        0,349,351,5,42,0,0,350,349,1,0,0,0,350,351,1,0,0,0,351,352,1,0,0,
        0,352,358,5,69,0,0,353,355,5,42,0,0,354,353,1,0,0,0,354,355,1,0,
        0,0,355,356,1,0,0,0,356,358,5,68,0,0,357,337,1,0,0,0,357,338,1,0,
        0,0,357,339,1,0,0,0,357,340,1,0,0,0,357,341,1,0,0,0,357,342,1,0,
        0,0,357,343,1,0,0,0,357,348,1,0,0,0,357,350,1,0,0,0,357,354,1,0,
        0,0,358,59,1,0,0,0,359,360,5,7,0,0,360,362,3,62,31,0,361,363,3,84,
        42,0,362,361,1,0,0,0,362,363,1,0,0,0,363,61,1,0,0,0,364,366,5,35,
        0,0,365,364,1,0,0,0,365,366,1,0,0,0,366,367,1,0,0,0,367,386,5,22,
        0,0,368,370,5,35,0,0,369,368,1,0,0,0,369,370,1,0,0,0,370,371,1,0,
        0,0,371,386,3,86,43,0,372,374,5,35,0,0,373,372,1,0,0,0,373,374,1,
        0,0,0,374,375,1,0,0,0,375,386,5,60,0,0,376,378,5,35,0,0,377,376,
        1,0,0,0,377,378,1,0,0,0,378,379,1,0,0,0,379,386,5,59,0,0,380,382,
        5,35,0,0,381,380,1,0,0,0,381,382,1,0,0,0,382,383,1,0,0,0,383,386,
        5,63,0,0,384,386,5,53,0,0,385,365,1,0,0,0,385,369,1,0,0,0,385,373,
        1,0,0,0,385,377,1,0,0,0,385,381,1,0,0,0,385,384,1,0,0,0,386,63,1,
        0,0,0,387,388,5,8,0,0,388,389,3,62,31,0,389,65,1,0,0,0,390,392,5,
        9,0,0,391,393,3,68,34,0,392,391,1,0,0,0,392,393,1,0,0,0,393,394,
        1,0,0,0,394,395,3,70,35,0,395,67,1,0,0,0,396,397,5,36,0,0,397,398,
        5,67,0,0,398,69,1,0,0,0,399,406,5,53,0,0,400,401,3,78,39,0,401,403,
        5,37,0,0,402,404,3,80,40,0,403,402,1,0,0,0,403,404,1,0,0,0,404,406,
        1,0,0,0,405,399,1,0,0,0,405,400,1,0,0,0,406,71,1,0,0,0,407,409,5,
        10,0,0,408,410,3,74,37,0,409,408,1,0,0,0,409,410,1,0,0,0,410,73,
        1,0,0,0,411,413,3,88,44,0,412,411,1,0,0,0,413,414,1,0,0,0,414,412,
        1,0,0,0,414,415,1,0,0,0,415,75,1,0,0,0,416,418,5,11,0,0,417,419,
        3,84,42,0,418,417,1,0,0,0,418,419,1,0,0,0,419,77,1,0,0,0,420,423,
        3,86,43,0,421,423,5,59,0,0,422,420,1,0,0,0,422,421,1,0,0,0,423,79,
        1,0,0,0,424,426,3,88,44,0,425,424,1,0,0,0,426,427,1,0,0,0,427,425,
        1,0,0,0,427,428,1,0,0,0,428,81,1,0,0,0,429,430,4,41,0,0,430,431,
        3,84,42,0,431,83,1,0,0,0,432,434,3,88,44,0,433,432,1,0,0,0,434,435,
        1,0,0,0,435,433,1,0,0,0,435,436,1,0,0,0,436,85,1,0,0,0,437,438,7,
        3,0,0,438,87,1,0,0,0,439,478,5,53,0,0,440,478,5,54,0,0,441,478,5,
        55,0,0,442,478,5,56,0,0,443,478,5,57,0,0,444,478,5,58,0,0,445,478,
        5,59,0,0,446,478,5,60,0,0,447,478,5,61,0,0,448,478,5,62,0,0,449,
        478,5,63,0,0,450,478,5,64,0,0,451,478,5,65,0,0,452,478,5,52,0,0,
        453,478,5,49,0,0,454,478,5,50,0,0,455,478,5,23,0,0,456,478,5,24,
        0,0,457,478,5,29,0,0,458,478,5,30,0,0,459,478,5,31,0,0,460,478,5,
        32,0,0,461,478,5,33,0,0,462,478,5,39,0,0,463,478,5,40,0,0,464,478,
        5,41,0,0,465,478,5,42,0,0,466,478,5,38,0,0,467,478,5,37,0,0,468,
        478,5,34,0,0,469,478,5,36,0,0,470,478,5,66,0,0,471,478,3,86,43,0,
        472,478,5,69,0,0,473,478,5,68,0,0,474,478,5,72,0,0,475,478,5,73,
        0,0,476,478,5,74,0,0,477,439,1,0,0,0,477,440,1,0,0,0,477,441,1,0,
        0,0,477,442,1,0,0,0,477,443,1,0,0,0,477,444,1,0,0,0,477,445,1,0,
        0,0,477,446,1,0,0,0,477,447,1,0,0,0,477,448,1,0,0,0,477,449,1,0,
        0,0,477,450,1,0,0,0,477,451,1,0,0,0,477,452,1,0,0,0,477,453,1,0,
        0,0,477,454,1,0,0,0,477,455,1,0,0,0,477,456,1,0,0,0,477,457,1,0,
        0,0,477,458,1,0,0,0,477,459,1,0,0,0,477,460,1,0,0,0,477,461,1,0,
        0,0,477,462,1,0,0,0,477,463,1,0,0,0,477,464,1,0,0,0,477,465,1,0,
        0,0,477,466,1,0,0,0,477,467,1,0,0,0,477,468,1,0,0,0,477,469,1,0,
        0,0,477,470,1,0,0,0,477,471,1,0,0,0,477,472,1,0,0,0,477,473,1,0,
        0,0,477,474,1,0,0,0,477,475,1,0,0,0,477,476,1,0,0,0,478,89,1,0,0,
        0,479,481,3,2,1,0,480,479,1,0,0,0,481,484,1,0,0,0,482,480,1,0,0,
        0,482,483,1,0,0,0,483,91,1,0,0,0,484,482,1,0,0,0,60,95,103,107,114,
        118,121,134,138,143,149,151,157,163,168,180,185,203,206,210,214,
        219,224,230,249,253,256,262,266,269,281,291,294,300,313,320,327,
        333,335,346,350,354,357,362,365,369,373,377,381,385,392,403,405,
        409,414,418,422,427,435,477,482
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
                     "<INVALID>", "<INVALID>", "'('", "')'", "'&'", "'|'", 
                     "'&&'", "'||'", "'>>'", "'>&'", "'<&'", "'>'", "'<'", 
                     "'=='", "':'", "'/'", "'='", "','", "'.'", "'\\'", 
                     "'+'", "'-'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'^'", "'*'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'!'", "'~'", "'%'" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "REM", "LABEL", "AT", 
                      "FOR", "IF", "CALL", "GOTO", "SET", "SETLOCAL", "ENDLOCAL", 
                      "DO", "IN", "EXIST", "DEFINED", "NOT", "ERRORLEVEL", 
                      "CMDEXTVERSION", "ELSE", "EXIT", "SHIFT", "EOF_KW", 
                      "LPAREN", "RPAREN", "AMP", "PIPE", "AMPAMP", "PIPEPIPE", 
                      "APPEND", "DUP_OUT", "DUP_IN", "GT", "LT", "EQ", "COLON", 
                      "SLASH", "EQUALS", "COMMA", "DOT", "BACKSLASH", "PLUS", 
                      "MINUS", "EQU", "NEQ", "LSS", "LEQ", "GTR", "GEQ", 
                      "CARET", "ASTERISK", "LINE_CONTINUATION", "CARET_ESCAPE", 
                      "DQ_STRING", "SQ_STRING", "BACKTICK_STRING", "PERCENT_TILDE", 
                      "PERCENT_VAR_SUBSTRING", "PERCENT_VAR_REPLACE", "PERCENT_VAR", 
                      "PERCENT_ARG", "FOR_VAR", "FOR_VAR_TILDE", "BANG_VAR", 
                      "BANG", "TILDE", "PERCENT", "WORD", "HEX_NUMBER", 
                      "NUMBER", "WS", "NEWLINE", "UNMATCHED_DQ", "UNMATCHED_SQ", 
                      "UNMATCHED_BACKTICK" ]

    RULE_script = 0
    RULE_line = 1
    RULE_label = 2
    RULE_commandLine = 3
    RULE_statement = 4
    RULE_exitStmt = 5
    RULE_exitTail = 6
    RULE_groupStmt = 7
    RULE_shiftStmt = 8
    RULE_ifStmt = 9
    RULE_ifIOpt = 10
    RULE_ifBody = 11
    RULE_elseClause = 12
    RULE_ifErrorlevelStmt = 13
    RULE_ifCmdextversionStmt = 14
    RULE_ifExistOperand = 15
    RULE_ifDefinedOperand = 16
    RULE_ifPredicate = 17
    RULE_comparison = 18
    RULE_compareOp = 19
    RULE_compareOperand = 20
    RULE_forStmt = 21
    RULE_forPath = 22
    RULE_forSlashMod = 23
    RULE_forFOptions = 24
    RULE_forFOptionAnchor = 25
    RULE_forFOptionExtra = 26
    RULE_forBody = 27
    RULE_forList = 28
    RULE_forListItem = 29
    RULE_callStmt = 30
    RULE_callTarget = 31
    RULE_gotoStmt = 32
    RULE_setStmt = 33
    RULE_setMode = 34
    RULE_setAssign = 35
    RULE_setlocalStmt = 36
    RULE_setlocalRest = 37
    RULE_endlocalStmt = 38
    RULE_setTarget = 39
    RULE_setRest = 40
    RULE_genericCmd = 41
    RULE_commandTail = 42
    RULE_argWord = 43
    RULE_token = 44
    RULE_block = 45

    ruleNames =  [ "script", "line", "label", "commandLine", "statement", 
                   "exitStmt", "exitTail", "groupStmt", "shiftStmt", "ifStmt", 
                   "ifIOpt", "ifBody", "elseClause", "ifErrorlevelStmt", 
                   "ifCmdextversionStmt", "ifExistOperand", "ifDefinedOperand", 
                   "ifPredicate", "comparison", "compareOp", "compareOperand", 
                   "forStmt", "forPath", "forSlashMod", "forFOptions", "forFOptionAnchor", 
                   "forFOptionExtra", "forBody", "forList", "forListItem", 
                   "callStmt", "callTarget", "gotoStmt", "setStmt", "setMode", 
                   "setAssign", "setlocalStmt", "setlocalRest", "endlocalStmt", 
                   "setTarget", "setRest", "genericCmd", "commandTail", 
                   "argWord", "token", "block" ]

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
    CMDEXTVERSION=18
    ELSE=19
    EXIT=20
    SHIFT=21
    EOF_KW=22
    LPAREN=23
    RPAREN=24
    AMP=25
    PIPE=26
    AMPAMP=27
    PIPEPIPE=28
    APPEND=29
    DUP_OUT=30
    DUP_IN=31
    GT=32
    LT=33
    EQ=34
    COLON=35
    SLASH=36
    EQUALS=37
    COMMA=38
    DOT=39
    BACKSLASH=40
    PLUS=41
    MINUS=42
    EQU=43
    NEQ=44
    LSS=45
    LEQ=46
    GTR=47
    GEQ=48
    CARET=49
    ASTERISK=50
    LINE_CONTINUATION=51
    CARET_ESCAPE=52
    DQ_STRING=53
    SQ_STRING=54
    BACKTICK_STRING=55
    PERCENT_TILDE=56
    PERCENT_VAR_SUBSTRING=57
    PERCENT_VAR_REPLACE=58
    PERCENT_VAR=59
    PERCENT_ARG=60
    FOR_VAR=61
    FOR_VAR_TILDE=62
    BANG_VAR=63
    BANG=64
    TILDE=65
    PERCENT=66
    WORD=67
    HEX_NUMBER=68
    NUMBER=69
    WS=70
    NEWLINE=71
    UNMATCHED_DQ=72
    UNMATCHED_SQ=73
    UNMATCHED_BACKTICK=74

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



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
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 92
                    self.line() 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 98
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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.label()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.commandLine()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
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
            self.state = 105
            self.match(BatchParser.LABEL)
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 106
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
            self.state = 109
            self.statement()
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 110
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 111
                    self.statement() 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 117
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


        def groupStmt(self):
            return self.getTypedRuleContext(BatchParser.GroupStmtContext,0)


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
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 120
                self.match(BatchParser.AT)


            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 123
                self.ifStmt()
                pass

            elif la_ == 2:
                self.state = 124
                self.forStmt()
                pass

            elif la_ == 3:
                self.state = 125
                self.callStmt()
                pass

            elif la_ == 4:
                self.state = 126
                self.gotoStmt()
                pass

            elif la_ == 5:
                self.state = 127
                self.setStmt()
                pass

            elif la_ == 6:
                self.state = 128
                self.setlocalStmt()
                pass

            elif la_ == 7:
                self.state = 129
                self.endlocalStmt()
                pass

            elif la_ == 8:
                self.state = 130
                self.exitStmt()
                pass

            elif la_ == 9:
                self.state = 131
                self.shiftStmt()
                pass

            elif la_ == 10:
                self.state = 132
                self.groupStmt()
                pass

            elif la_ == 11:
                self.state = 133
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
            self.state = 136
            self.match(BatchParser.EXIT)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 137
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
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(BatchParser.SLASH)
                self.state = 141
                self.match(BatchParser.WORD)
                self.state = 143
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 142
                    self.match(BatchParser.NUMBER)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 146
                        self.token()

                    else:
                        raise NoViableAltException(self)
                    self.state = 149 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupStmtContext(ParserRuleContext):
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

        def commandTail(self):
            return self.getTypedRuleContext(BatchParser.CommandTailContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_groupStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupStmt" ):
                return visitor.visitGroupStmt(self)
            else:
                return visitor.visitChildren(self)




    def groupStmt(self):

        localctx = BatchParser.GroupStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_groupStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(BatchParser.LPAREN)
            self.state = 154
            self.block()
            self.state = 155
            self.match(BatchParser.RPAREN)
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 156
                self.commandTail()


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
        self.enterRule(localctx, 16, self.RULE_shiftStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(BatchParser.SHIFT)
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 160
                    self.token() 
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(BatchParser.IF)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 167
                self.ifIOpt()


            self.state = 170
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
        self.enterRule(localctx, 20, self.RULE_ifIOpt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(BatchParser.SLASH)
            self.state = 173
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
        self.enterRule(localctx, 22, self.RULE_ifBody)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.ifPredicate()
                self.state = 176
                self.match(BatchParser.LPAREN)
                self.state = 177
                self.block()
                self.state = 178
                self.match(BatchParser.RPAREN)
                self.state = 180
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 179
                    self.elseClause()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.ifPredicate()
                self.state = 183
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
        self.enterRule(localctx, 24, self.RULE_elseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(BatchParser.ELSE)
            self.state = 188
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
        self.enterRule(localctx, 26, self.RULE_ifErrorlevelStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(BatchParser.ERRORLEVEL)
            self.state = 191
            self.match(BatchParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfCmdextversionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CMDEXTVERSION(self):
            return self.getToken(BatchParser.CMDEXTVERSION, 0)

        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_ifCmdextversionStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfCmdextversionStmt" ):
                return visitor.visitIfCmdextversionStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifCmdextversionStmt(self):

        localctx = BatchParser.IfCmdextversionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifCmdextversionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(BatchParser.CMDEXTVERSION)
            self.state = 194
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

        def FOR_VAR(self):
            return self.getToken(BatchParser.FOR_VAR, 0)

        def FOR_VAR_TILDE(self):
            return self.getToken(BatchParser.FOR_VAR_TILDE, 0)

        def BANG_VAR(self):
            return self.getToken(BatchParser.BANG_VAR, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_ifExistOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfExistOperand" ):
                return visitor.visitIfExistOperand(self)
            else:
                return visitor.visitChildren(self)




    def ifExistOperand(self):

        localctx = BatchParser.IfExistOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifExistOperand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            _la = self._input.LA(1)
            if not(((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & 18377) != 0)):
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


    class IfDefinedOperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def PERCENT_VAR(self):
            return self.getToken(BatchParser.PERCENT_VAR, 0)

        def FOR_VAR(self):
            return self.getToken(BatchParser.FOR_VAR, 0)

        def FOR_VAR_TILDE(self):
            return self.getToken(BatchParser.FOR_VAR_TILDE, 0)

        def BANG_VAR(self):
            return self.getToken(BatchParser.BANG_VAR, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_ifDefinedOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfDefinedOperand" ):
                return visitor.visitIfDefinedOperand(self)
            else:
                return visitor.visitChildren(self)




    def ifDefinedOperand(self):

        localctx = BatchParser.IfDefinedOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ifDefinedOperand)
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 43, 44, 45, 46, 47, 48, 67]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.argWord()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(BatchParser.PERCENT_VAR)
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
                self.match(BatchParser.FOR_VAR)
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 4)
                self.state = 201
                self.match(BatchParser.FOR_VAR_TILDE)
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 5)
                self.state = 202
                self.match(BatchParser.BANG_VAR)
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


    class IfPredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifErrorlevelStmt(self):
            return self.getTypedRuleContext(BatchParser.IfErrorlevelStmtContext,0)


        def NOT(self):
            return self.getToken(BatchParser.NOT, 0)

        def ifCmdextversionStmt(self):
            return self.getTypedRuleContext(BatchParser.IfCmdextversionStmtContext,0)


        def DEFINED(self):
            return self.getToken(BatchParser.DEFINED, 0)

        def ifDefinedOperand(self):
            return self.getTypedRuleContext(BatchParser.IfDefinedOperandContext,0)


        def EXIST(self):
            return self.getToken(BatchParser.EXIST, 0)

        def ifExistOperand(self):
            return self.getTypedRuleContext(BatchParser.IfExistOperandContext,0)


        def comparison(self):
            return self.getTypedRuleContext(BatchParser.ComparisonContext,0)


        def DQ_STRING(self):
            return self.getToken(BatchParser.DQ_STRING, 0)

        def PERCENT_TILDE(self):
            return self.getToken(BatchParser.PERCENT_TILDE, 0)

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_ifPredicate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfPredicate" ):
                return visitor.visitIfPredicate(self)
            else:
                return visitor.visitChildren(self)




    def ifPredicate(self):

        localctx = BatchParser.IfPredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ifPredicate)
        self._la = 0 # Token type
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 205
                    self.match(BatchParser.NOT)


                self.state = 208
                self.ifErrorlevelStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 209
                    self.match(BatchParser.NOT)


                self.state = 212
                self.ifCmdextversionStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 213
                    self.match(BatchParser.NOT)


                self.state = 216
                self.match(BatchParser.DEFINED)
                self.state = 217
                self.ifDefinedOperand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 218
                    self.match(BatchParser.NOT)


                self.state = 221
                self.match(BatchParser.EXIST)
                self.state = 222
                self.ifExistOperand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 224
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 223
                    self.match(BatchParser.NOT)


                self.state = 226
                self.comparison()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 227
                self.match(BatchParser.DQ_STRING)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 228
                self.match(BatchParser.PERCENT_TILDE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 229
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
        self.enterRule(localctx, 36, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.compareOperand()
            self.state = 233
            self.compareOp()
            self.state = 234
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
        self.enterRule(localctx, 38, self.RULE_compareOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 554171040268288) != 0)):
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

        def FOR_VAR(self):
            return self.getToken(BatchParser.FOR_VAR, 0)

        def FOR_VAR_TILDE(self):
            return self.getToken(BatchParser.FOR_VAR_TILDE, 0)

        def BANG_VAR(self):
            return self.getToken(BatchParser.BANG_VAR, 0)

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def MINUS(self):
            return self.getToken(BatchParser.MINUS, 0)

        def HEX_NUMBER(self):
            return self.getToken(BatchParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_compareOperand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareOperand" ):
                return visitor.visitCompareOperand(self)
            else:
                return visitor.visitChildren(self)




    def compareOperand(self):

        localctx = BatchParser.CompareOperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_compareOperand)
        self._la = 0 # Token type
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(BatchParser.DQ_STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(BatchParser.PERCENT_TILDE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.match(BatchParser.PERCENT_VAR_SUBSTRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 241
                self.match(BatchParser.PERCENT_VAR_REPLACE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 242
                self.match(BatchParser.PERCENT_VAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 243
                self.match(BatchParser.PERCENT_ARG)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 244
                self.match(BatchParser.FOR_VAR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 245
                self.match(BatchParser.FOR_VAR_TILDE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 246
                self.match(BatchParser.BANG_VAR)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 247
                self.argWord()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 248
                    self.match(BatchParser.MINUS)


                self.state = 251
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 252
                    self.match(BatchParser.MINUS)


                self.state = 255
                self.match(BatchParser.HEX_NUMBER)
                pass


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


        def forPath(self):
            return self.getTypedRuleContext(BatchParser.ForPathContext,0)


        def getRuleIndex(self):
            return BatchParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BatchParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(BatchParser.FOR)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 259
                self.forSlashMod()
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 265
                self.forFOptions()


            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & 4611984810712367103) != 0):
                self.state = 268
                self.forPath()


            self.state = 271
            self.match(BatchParser.FOR_VAR)
            self.state = 272
            self.match(BatchParser.IN)
            self.state = 273
            self.match(BatchParser.LPAREN)
            self.state = 274
            self.forList()
            self.state = 275
            self.match(BatchParser.RPAREN)
            self.state = 276
            self.match(BatchParser.DO)
            self.state = 277
            self.forBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForPathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def DQ_STRING(self):
            return self.getToken(BatchParser.DQ_STRING, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_forPath

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForPath" ):
                return visitor.visitForPath(self)
            else:
                return visitor.visitChildren(self)




    def forPath(self):

        localctx = BatchParser.ForPathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_forPath)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 43, 44, 45, 46, 47, 48, 67]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.argWord()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(BatchParser.DQ_STRING)
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
        self.enterRule(localctx, 46, self.RULE_forSlashMod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(BatchParser.SLASH)
            self.state = 284
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

        def forFOptionAnchor(self):
            return self.getTypedRuleContext(BatchParser.ForFOptionAnchorContext,0)


        def forFOptionExtra(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.ForFOptionExtraContext)
            else:
                return self.getTypedRuleContext(BatchParser.ForFOptionExtraContext,i)


        def getRuleIndex(self):
            return BatchParser.RULE_forFOptions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForFOptions" ):
                return visitor.visitForFOptions(self)
            else:
                return visitor.visitChildren(self)




    def forFOptions(self):

        localctx = BatchParser.ForFOptionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forFOptions)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.match(BatchParser.DQ_STRING)
                pass
            elif token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 43, 44, 45, 46, 47, 48, 52, 67]:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.forFOptionAnchor()
                self.state = 291
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 288
                        self.forFOptionExtra() 
                    self.state = 293
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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


    class ForFOptionAnchorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def CARET_ESCAPE(self):
            return self.getToken(BatchParser.CARET_ESCAPE, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_forFOptionAnchor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForFOptionAnchor" ):
                return visitor.visitForFOptionAnchor(self)
            else:
                return visitor.visitChildren(self)




    def forFOptionAnchor(self):

        localctx = BatchParser.ForFOptionAnchorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forFOptionAnchor)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 43, 44, 45, 46, 47, 48, 67]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.argWord()
                self.state = 297
                self.match(BatchParser.CARET_ESCAPE)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.match(BatchParser.CARET_ESCAPE)
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


    class ForFOptionExtraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def CARET_ESCAPE(self):
            return self.getToken(BatchParser.CARET_ESCAPE, 0)

        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def COMMA(self):
            return self.getToken(BatchParser.COMMA, 0)

        def ASTERISK(self):
            return self.getToken(BatchParser.ASTERISK, 0)

        def MINUS(self):
            return self.getToken(BatchParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(BatchParser.PLUS, 0)

        def PERCENT(self):
            return self.getToken(BatchParser.PERCENT, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_forFOptionExtra

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForFOptionExtra" ):
                return visitor.visitForFOptionExtra(self)
            else:
                return visitor.visitChildren(self)




    def forFOptionExtra(self):

        localctx = BatchParser.ForFOptionExtraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_forFOptionExtra)
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.argWord()
                self.state = 303
                self.match(BatchParser.CARET_ESCAPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.match(BatchParser.CARET_ESCAPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 307
                self.match(BatchParser.COMMA)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 308
                self.match(BatchParser.ASTERISK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 309
                self.match(BatchParser.MINUS)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 310
                self.match(BatchParser.PLUS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 311
                self.match(BatchParser.PERCENT)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 312
                self.argWord()
                pass


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
        self.enterRule(localctx, 54, self.RULE_forBody)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(BatchParser.LPAREN)
                self.state = 316
                self.block()
                self.state = 317
                self.match(BatchParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
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
        self.enterRule(localctx, 56, self.RULE_forList)
        self._la = 0 # Token type
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.forListItem()
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==38:
                    self.state = 323
                    self.match(BatchParser.COMMA)
                    self.state = 324
                    self.forListItem()
                    self.state = 329
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 330
                    self.forListItem()
                    self.state = 333 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1866174697549332448) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 7) != 0)):
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

        def MINUS(self):
            return self.getToken(BatchParser.MINUS, 0)

        def HEX_NUMBER(self):
            return self.getToken(BatchParser.HEX_NUMBER, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_forListItem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForListItem" ):
                return visitor.visitForListItem(self)
            else:
                return visitor.visitChildren(self)




    def forListItem(self):

        localctx = BatchParser.ForListItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forListItem)
        self._la = 0 # Token type
        try:
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(BatchParser.SQ_STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.match(BatchParser.DQ_STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
                self.match(BatchParser.BACKTICK_STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 340
                self.match(BatchParser.PERCENT_VAR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 341
                self.match(BatchParser.PERCENT_TILDE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 342
                self.match(BatchParser.PERCENT_ARG)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 343
                self.match(BatchParser.ASTERISK)
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 344
                    self.match(BatchParser.DOT)
                    self.state = 345
                    self.argWord()


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 348
                self.argWord()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 349
                    self.match(BatchParser.MINUS)


                self.state = 352
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 353
                    self.match(BatchParser.MINUS)


                self.state = 356
                self.match(BatchParser.HEX_NUMBER)
                pass


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
        self.enterRule(localctx, 60, self.RULE_callStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(BatchParser.CALL)
            self.state = 360
            self.callTarget()
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 361
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

        def BANG_VAR(self):
            return self.getToken(BatchParser.BANG_VAR, 0)

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
        self.enterRule(localctx, 62, self.RULE_callTarget)
        self._la = 0 # Token type
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 364
                    self.match(BatchParser.COLON)


                self.state = 367
                self.match(BatchParser.EOF_KW)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 368
                    self.match(BatchParser.COLON)


                self.state = 371
                self.argWord()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 372
                    self.match(BatchParser.COLON)


                self.state = 375
                self.match(BatchParser.PERCENT_ARG)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 377
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 376
                    self.match(BatchParser.COLON)


                self.state = 379
                self.match(BatchParser.PERCENT_VAR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 380
                    self.match(BatchParser.COLON)


                self.state = 383
                self.match(BatchParser.BANG_VAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 384
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
        self.enterRule(localctx, 64, self.RULE_gotoStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(BatchParser.GOTO)
            self.state = 388
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
        self.enterRule(localctx, 66, self.RULE_setStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(BatchParser.SET)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 391
                self.setMode()


            self.state = 394
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
        self.enterRule(localctx, 68, self.RULE_setMode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(BatchParser.SLASH)
            self.state = 397
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
        self.enterRule(localctx, 70, self.RULE_setAssign)
        try:
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(BatchParser.DQ_STRING)
                pass
            elif token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 43, 44, 45, 46, 47, 48, 59, 67]:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.setTarget()
                self.state = 401
                self.match(BatchParser.EQUALS)
                self.state = 403
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 402
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
        self.enterRule(localctx, 72, self.RULE_setlocalStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(BatchParser.SETLOCAL)
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.state = 408
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
        self.enterRule(localctx, 74, self.RULE_setlocalRest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 411
                    self.token()

                else:
                    raise NoViableAltException(self)
                self.state = 414 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

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
        self.enterRule(localctx, 76, self.RULE_endlocalStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(BatchParser.ENDLOCAL)
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 417
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
        self.enterRule(localctx, 78, self.RULE_setTarget)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 43, 44, 45, 46, 47, 48, 67]:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.argWord()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
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
        self.enterRule(localctx, 80, self.RULE_setRest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 424
                    self.token()

                else:
                    raise NoViableAltException(self)
                self.state = 427 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
        self.enterRule(localctx, 82, self.RULE_genericCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            if not self._notForToken() and self._notLonelyParen():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._notForToken() and self._notLonelyParen()")
            self.state = 430
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
        self.enterRule(localctx, 84, self.RULE_commandTail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 432
                    self.token()

                else:
                    raise NoViableAltException(self)
                self.state = 435 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,57,self._ctx)

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

        def CMDEXTVERSION(self):
            return self.getToken(BatchParser.CMDEXTVERSION, 0)

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
            return BatchParser.RULE_argWord

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgWord" ):
                return visitor.visitArgWord(self)
            else:
                return visitor.visitChildren(self)




    def argWord(self):

        localctx = BatchParser.ArgWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_argWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            _la = self._input.LA(1)
            if not(((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & 4611703335735656447) != 0)):
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

        def BANG(self):
            return self.getToken(BatchParser.BANG, 0)

        def TILDE(self):
            return self.getToken(BatchParser.TILDE, 0)

        def CARET_ESCAPE(self):
            return self.getToken(BatchParser.CARET_ESCAPE, 0)

        def CARET(self):
            return self.getToken(BatchParser.CARET, 0)

        def ASTERISK(self):
            return self.getToken(BatchParser.ASTERISK, 0)

        def LPAREN(self):
            return self.getToken(BatchParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BatchParser.RPAREN, 0)

        def APPEND(self):
            return self.getToken(BatchParser.APPEND, 0)

        def DUP_OUT(self):
            return self.getToken(BatchParser.DUP_OUT, 0)

        def DUP_IN(self):
            return self.getToken(BatchParser.DUP_IN, 0)

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

        def EQ(self):
            return self.getToken(BatchParser.EQ, 0)

        def SLASH(self):
            return self.getToken(BatchParser.SLASH, 0)

        def PERCENT(self):
            return self.getToken(BatchParser.PERCENT, 0)

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def HEX_NUMBER(self):
            return self.getToken(BatchParser.HEX_NUMBER, 0)

        def UNMATCHED_DQ(self):
            return self.getToken(BatchParser.UNMATCHED_DQ, 0)

        def UNMATCHED_SQ(self):
            return self.getToken(BatchParser.UNMATCHED_SQ, 0)

        def UNMATCHED_BACKTICK(self):
            return self.getToken(BatchParser.UNMATCHED_BACKTICK, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_token

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToken" ):
                return visitor.visitToken(self)
            else:
                return visitor.visitChildren(self)




    def token(self):

        localctx = BatchParser.TokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_token)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.match(BatchParser.DQ_STRING)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.match(BatchParser.SQ_STRING)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                self.match(BatchParser.BACKTICK_STRING)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 4)
                self.state = 442
                self.match(BatchParser.PERCENT_TILDE)
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 5)
                self.state = 443
                self.match(BatchParser.PERCENT_VAR_SUBSTRING)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 6)
                self.state = 444
                self.match(BatchParser.PERCENT_VAR_REPLACE)
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 7)
                self.state = 445
                self.match(BatchParser.PERCENT_VAR)
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 8)
                self.state = 446
                self.match(BatchParser.PERCENT_ARG)
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 9)
                self.state = 447
                self.match(BatchParser.FOR_VAR)
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 10)
                self.state = 448
                self.match(BatchParser.FOR_VAR_TILDE)
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 11)
                self.state = 449
                self.match(BatchParser.BANG_VAR)
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 12)
                self.state = 450
                self.match(BatchParser.BANG)
                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 13)
                self.state = 451
                self.match(BatchParser.TILDE)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 14)
                self.state = 452
                self.match(BatchParser.CARET_ESCAPE)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 15)
                self.state = 453
                self.match(BatchParser.CARET)
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 16)
                self.state = 454
                self.match(BatchParser.ASTERISK)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 17)
                self.state = 455
                self.match(BatchParser.LPAREN)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 18)
                self.state = 456
                self.match(BatchParser.RPAREN)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 19)
                self.state = 457
                self.match(BatchParser.APPEND)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 20)
                self.state = 458
                self.match(BatchParser.DUP_OUT)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 21)
                self.state = 459
                self.match(BatchParser.DUP_IN)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 22)
                self.state = 460
                self.match(BatchParser.GT)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 23)
                self.state = 461
                self.match(BatchParser.LT)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 24)
                self.state = 462
                self.match(BatchParser.DOT)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 25)
                self.state = 463
                self.match(BatchParser.BACKSLASH)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 26)
                self.state = 464
                self.match(BatchParser.PLUS)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 27)
                self.state = 465
                self.match(BatchParser.MINUS)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 28)
                self.state = 466
                self.match(BatchParser.COMMA)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 29)
                self.state = 467
                self.match(BatchParser.EQUALS)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 30)
                self.state = 468
                self.match(BatchParser.EQ)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 31)
                self.state = 469
                self.match(BatchParser.SLASH)
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 32)
                self.state = 470
                self.match(BatchParser.PERCENT)
                pass
            elif token in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 43, 44, 45, 46, 47, 48, 67]:
                self.enterOuterAlt(localctx, 33)
                self.state = 471
                self.argWord()
                pass
            elif token in [69]:
                self.enterOuterAlt(localctx, 34)
                self.state = 472
                self.match(BatchParser.NUMBER)
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 35)
                self.state = 473
                self.match(BatchParser.HEX_NUMBER)
                pass
            elif token in [72]:
                self.enterOuterAlt(localctx, 36)
                self.state = 474
                self.match(BatchParser.UNMATCHED_DQ)
                pass
            elif token in [73]:
                self.enterOuterAlt(localctx, 37)
                self.state = 475
                self.match(BatchParser.UNMATCHED_SQ)
                pass
            elif token in [74]:
                self.enterOuterAlt(localctx, 38)
                self.state = 476
                self.match(BatchParser.UNMATCHED_BACKTICK)
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
        self.enterRule(localctx, 90, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 479
                    self.line() 
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

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
        self._predicates[41] = self.genericCmd_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def genericCmd_sempred(self, localctx:GenericCmdContext, predIndex:int):
            if predIndex == 0:
                return self._notForToken() and self._notLonelyParen()
         




