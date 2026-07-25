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
        4,1,80,598,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,1,0,5,0,96,8,0,10,0,12,0,99,9,0,1,0,1,0,1,1,1,1,1,1,3,1,106,
        8,1,1,2,1,2,3,2,110,8,2,1,3,1,3,1,3,5,3,115,8,3,10,3,12,3,118,9,
        3,1,3,3,3,121,8,3,1,4,3,4,124,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,137,8,4,1,5,1,5,3,5,141,8,5,1,6,1,6,1,6,3,6,146,
        8,6,1,6,1,6,4,6,150,8,6,11,6,12,6,151,3,6,154,8,6,1,7,1,7,1,7,1,
        7,3,7,160,8,7,1,8,1,8,5,8,164,8,8,10,8,12,8,167,9,8,1,9,1,9,3,9,
        171,8,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,183,
        8,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,191,8,11,3,11,193,8,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,202,8,12,1,13,1,13,1,13,1,
        14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,3,15,215,8,15,1,15,4,15,218,
        8,15,11,15,12,15,219,1,15,1,15,3,15,224,8,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,3,15,234,8,15,1,16,1,16,1,16,1,16,1,16,3,16,
        241,8,16,1,17,3,17,244,8,17,1,17,1,17,3,17,248,8,17,1,17,1,17,3,
        17,252,8,17,1,17,1,17,1,17,3,17,257,8,17,1,17,1,17,1,17,3,17,262,
        8,17,1,17,1,17,1,17,1,17,3,17,268,8,17,1,18,1,18,1,18,1,18,1,19,
        1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,3,20,289,8,20,1,20,1,20,3,20,293,8,20,1,20,3,20,296,8,20,1,
        21,1,21,5,21,300,8,21,10,21,12,21,303,9,21,1,21,3,21,306,8,21,1,
        21,3,21,309,8,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,
        22,3,22,321,8,22,1,23,1,23,1,23,1,24,1,24,1,24,5,24,329,8,24,10,
        24,12,24,332,9,24,3,24,334,8,24,1,25,1,25,1,25,1,25,3,25,340,8,25,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,
        354,8,26,1,27,1,27,1,27,1,27,1,27,3,27,361,8,27,1,28,1,28,1,28,5,
        28,366,8,28,10,28,12,28,369,9,28,1,28,4,28,372,8,28,11,28,12,28,
        373,3,28,376,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,
        29,387,8,29,1,29,4,29,390,8,29,11,29,12,29,391,1,29,1,29,3,29,396,
        8,29,1,29,1,29,3,29,400,8,29,1,29,1,29,3,29,404,8,29,1,29,1,29,3,
        29,408,8,29,1,29,3,29,411,8,29,1,30,1,30,1,30,3,30,416,8,30,1,31,
        3,31,419,8,31,1,31,1,31,3,31,423,8,31,1,31,1,31,3,31,427,8,31,1,
        31,1,31,3,31,431,8,31,1,31,1,31,3,31,435,8,31,1,31,1,31,3,31,439,
        8,31,1,32,1,32,1,32,3,32,444,8,32,1,33,1,33,3,33,448,8,33,1,33,3,
        33,451,8,33,1,34,1,34,1,34,1,35,1,35,1,35,1,35,3,35,460,8,35,1,35,
        3,35,463,8,35,1,36,1,36,3,36,467,8,36,1,37,4,37,470,8,37,11,37,12,
        37,471,1,38,1,38,3,38,476,8,38,1,39,4,39,479,8,39,11,39,12,39,480,
        1,39,3,39,484,8,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,
        1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,502,8,40,1,41,4,41,505,8,
        41,11,41,12,41,506,1,42,1,42,1,42,1,43,4,43,513,8,43,11,43,12,43,
        514,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,
        1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,
        3,44,542,8,44,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,3,45,590,8,45,
        1,46,5,46,593,8,46,10,46,12,46,596,9,46,1,46,0,0,47,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,0,2,1,0,
        27,30,2,0,36,36,46,51,768,0,97,1,0,0,0,2,105,1,0,0,0,4,107,1,0,0,
        0,6,111,1,0,0,0,8,123,1,0,0,0,10,138,1,0,0,0,12,153,1,0,0,0,14,155,
        1,0,0,0,16,161,1,0,0,0,18,168,1,0,0,0,20,174,1,0,0,0,22,192,1,0,
        0,0,24,201,1,0,0,0,26,203,1,0,0,0,28,206,1,0,0,0,30,233,1,0,0,0,
        32,240,1,0,0,0,34,267,1,0,0,0,36,269,1,0,0,0,38,273,1,0,0,0,40,295,
        1,0,0,0,42,297,1,0,0,0,44,320,1,0,0,0,46,322,1,0,0,0,48,333,1,0,
        0,0,50,339,1,0,0,0,52,353,1,0,0,0,54,360,1,0,0,0,56,375,1,0,0,0,
        58,410,1,0,0,0,60,412,1,0,0,0,62,438,1,0,0,0,64,440,1,0,0,0,66,445,
        1,0,0,0,68,452,1,0,0,0,70,462,1,0,0,0,72,464,1,0,0,0,74,469,1,0,
        0,0,76,473,1,0,0,0,78,483,1,0,0,0,80,501,1,0,0,0,82,504,1,0,0,0,
        84,508,1,0,0,0,86,512,1,0,0,0,88,541,1,0,0,0,90,589,1,0,0,0,92,594,
        1,0,0,0,94,96,3,2,1,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,0,0,
        97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,101,5,0,0,1,101,1,
        1,0,0,0,102,106,3,4,2,0,103,106,3,6,3,0,104,106,5,77,0,0,105,102,
        1,0,0,0,105,103,1,0,0,0,105,104,1,0,0,0,106,3,1,0,0,0,107,109,5,
        3,0,0,108,110,5,77,0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,5,1,0,
        0,0,111,116,3,8,4,0,112,113,7,0,0,0,113,115,3,8,4,0,114,112,1,0,
        0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,120,1,0,
        0,0,118,116,1,0,0,0,119,121,5,77,0,0,120,119,1,0,0,0,120,121,1,0,
        0,0,121,7,1,0,0,0,122,124,5,4,0,0,123,122,1,0,0,0,123,124,1,0,0,
        0,124,136,1,0,0,0,125,137,3,18,9,0,126,137,3,42,21,0,127,137,3,60,
        30,0,128,137,3,64,32,0,129,137,3,66,33,0,130,137,3,72,36,0,131,137,
        3,76,38,0,132,137,3,10,5,0,133,137,3,16,8,0,134,137,3,14,7,0,135,
        137,3,84,42,0,136,125,1,0,0,0,136,126,1,0,0,0,136,127,1,0,0,0,136,
        128,1,0,0,0,136,129,1,0,0,0,136,130,1,0,0,0,136,131,1,0,0,0,136,
        132,1,0,0,0,136,133,1,0,0,0,136,134,1,0,0,0,136,135,1,0,0,0,137,
        9,1,0,0,0,138,140,5,22,0,0,139,141,3,12,6,0,140,139,1,0,0,0,140,
        141,1,0,0,0,141,11,1,0,0,0,142,143,5,38,0,0,143,145,5,73,0,0,144,
        146,5,75,0,0,145,144,1,0,0,0,145,146,1,0,0,0,146,154,1,0,0,0,147,
        154,5,75,0,0,148,150,3,90,45,0,149,148,1,0,0,0,150,151,1,0,0,0,151,
        149,1,0,0,0,151,152,1,0,0,0,152,154,1,0,0,0,153,142,1,0,0,0,153,
        147,1,0,0,0,153,149,1,0,0,0,154,13,1,0,0,0,155,156,5,25,0,0,156,
        157,3,92,46,0,157,159,5,26,0,0,158,160,3,86,43,0,159,158,1,0,0,0,
        159,160,1,0,0,0,160,15,1,0,0,0,161,165,5,23,0,0,162,164,3,90,45,
        0,163,162,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,
        0,166,17,1,0,0,0,167,165,1,0,0,0,168,170,5,8,0,0,169,171,3,20,10,
        0,170,169,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,3,22,11,
        0,173,19,1,0,0,0,174,175,5,38,0,0,175,176,5,73,0,0,176,21,1,0,0,
        0,177,178,3,34,17,0,178,179,5,25,0,0,179,180,3,92,46,0,180,182,5,
        26,0,0,181,183,3,24,12,0,182,181,1,0,0,0,182,183,1,0,0,0,183,193,
        1,0,0,0,184,185,3,34,17,0,185,186,4,11,0,0,186,187,6,11,-1,0,187,
        188,3,8,4,0,188,190,6,11,-1,0,189,191,3,24,12,0,190,189,1,0,0,0,
        190,191,1,0,0,0,191,193,1,0,0,0,192,177,1,0,0,0,192,184,1,0,0,0,
        193,23,1,0,0,0,194,195,5,21,0,0,195,196,5,25,0,0,196,197,3,92,46,
        0,197,198,5,26,0,0,198,202,1,0,0,0,199,200,5,21,0,0,200,202,3,8,
        4,0,201,194,1,0,0,0,201,199,1,0,0,0,202,25,1,0,0,0,203,204,5,19,
        0,0,204,205,5,75,0,0,205,27,1,0,0,0,206,207,5,20,0,0,207,208,5,75,
        0,0,208,29,1,0,0,0,209,234,5,57,0,0,210,234,5,73,0,0,211,214,5,53,
        0,0,212,213,5,42,0,0,213,215,3,88,44,0,214,212,1,0,0,0,214,215,1,
        0,0,0,215,234,1,0,0,0,216,218,5,54,0,0,217,216,1,0,0,0,218,219,1,
        0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,223,1,0,0,0,221,222,5,
        42,0,0,222,224,3,88,44,0,223,221,1,0,0,0,223,224,1,0,0,0,224,234,
        1,0,0,0,225,234,5,63,0,0,226,234,5,60,0,0,227,234,5,64,0,0,228,234,
        5,66,0,0,229,234,5,65,0,0,230,234,5,67,0,0,231,234,5,68,0,0,232,
        234,5,69,0,0,233,209,1,0,0,0,233,210,1,0,0,0,233,211,1,0,0,0,233,
        217,1,0,0,0,233,225,1,0,0,0,233,226,1,0,0,0,233,227,1,0,0,0,233,
        228,1,0,0,0,233,229,1,0,0,0,233,230,1,0,0,0,233,231,1,0,0,0,233,
        232,1,0,0,0,234,31,1,0,0,0,235,241,3,88,44,0,236,241,5,63,0,0,237,
        241,5,66,0,0,238,241,5,65,0,0,239,241,5,69,0,0,240,235,1,0,0,0,240,
        236,1,0,0,0,240,237,1,0,0,0,240,238,1,0,0,0,240,239,1,0,0,0,241,
        33,1,0,0,0,242,244,5,18,0,0,243,242,1,0,0,0,243,244,1,0,0,0,244,
        245,1,0,0,0,245,268,3,26,13,0,246,248,5,18,0,0,247,246,1,0,0,0,247,
        248,1,0,0,0,248,249,1,0,0,0,249,268,3,28,14,0,250,252,5,18,0,0,251,
        250,1,0,0,0,251,252,1,0,0,0,252,253,1,0,0,0,253,254,5,17,0,0,254,
        268,3,32,16,0,255,257,5,18,0,0,256,255,1,0,0,0,256,257,1,0,0,0,257,
        258,1,0,0,0,258,259,5,16,0,0,259,268,3,30,15,0,260,262,5,18,0,0,
        261,260,1,0,0,0,261,262,1,0,0,0,262,263,1,0,0,0,263,268,3,36,18,
        0,264,268,5,57,0,0,265,268,5,60,0,0,266,268,3,88,44,0,267,243,1,
        0,0,0,267,247,1,0,0,0,267,251,1,0,0,0,267,256,1,0,0,0,267,261,1,
        0,0,0,267,264,1,0,0,0,267,265,1,0,0,0,267,266,1,0,0,0,268,35,1,0,
        0,0,269,270,3,40,20,0,270,271,3,38,19,0,271,272,3,40,20,0,272,37,
        1,0,0,0,273,274,7,1,0,0,274,39,1,0,0,0,275,296,5,57,0,0,276,296,
        5,60,0,0,277,296,5,61,0,0,278,296,5,62,0,0,279,296,5,63,0,0,280,
        296,5,64,0,0,281,296,5,66,0,0,282,296,5,65,0,0,283,296,5,67,0,0,
        284,296,5,68,0,0,285,296,5,69,0,0,286,296,3,88,44,0,287,289,5,45,
        0,0,288,287,1,0,0,0,288,289,1,0,0,0,289,290,1,0,0,0,290,296,5,75,
        0,0,291,293,5,45,0,0,292,291,1,0,0,0,292,293,1,0,0,0,293,294,1,0,
        0,0,294,296,5,74,0,0,295,275,1,0,0,0,295,276,1,0,0,0,295,277,1,0,
        0,0,295,278,1,0,0,0,295,279,1,0,0,0,295,280,1,0,0,0,295,281,1,0,
        0,0,295,282,1,0,0,0,295,283,1,0,0,0,295,284,1,0,0,0,295,285,1,0,
        0,0,295,286,1,0,0,0,295,288,1,0,0,0,295,292,1,0,0,0,296,41,1,0,0,
        0,297,301,5,7,0,0,298,300,3,46,23,0,299,298,1,0,0,0,300,303,1,0,
        0,0,301,299,1,0,0,0,301,302,1,0,0,0,302,305,1,0,0,0,303,301,1,0,
        0,0,304,306,3,48,24,0,305,304,1,0,0,0,305,306,1,0,0,0,306,308,1,
        0,0,0,307,309,3,44,22,0,308,307,1,0,0,0,308,309,1,0,0,0,309,310,
        1,0,0,0,310,311,5,66,0,0,311,312,5,15,0,0,312,313,5,25,0,0,313,314,
        3,56,28,0,314,315,5,26,0,0,315,316,5,14,0,0,316,317,3,54,27,0,317,
        43,1,0,0,0,318,321,3,88,44,0,319,321,5,57,0,0,320,318,1,0,0,0,320,
        319,1,0,0,0,321,45,1,0,0,0,322,323,5,38,0,0,323,324,5,73,0,0,324,
        47,1,0,0,0,325,334,5,57,0,0,326,330,3,50,25,0,327,329,3,52,26,0,
        328,327,1,0,0,0,329,332,1,0,0,0,330,328,1,0,0,0,330,331,1,0,0,0,
        331,334,1,0,0,0,332,330,1,0,0,0,333,325,1,0,0,0,333,326,1,0,0,0,
        334,49,1,0,0,0,335,336,3,88,44,0,336,337,5,56,0,0,337,340,1,0,0,
        0,338,340,5,56,0,0,339,335,1,0,0,0,339,338,1,0,0,0,340,51,1,0,0,
        0,341,342,3,88,44,0,342,343,5,56,0,0,343,354,1,0,0,0,344,354,5,56,
        0,0,345,354,5,75,0,0,346,354,5,40,0,0,347,354,5,53,0,0,348,354,5,
        54,0,0,349,354,5,45,0,0,350,354,5,44,0,0,351,354,5,72,0,0,352,354,
        3,88,44,0,353,341,1,0,0,0,353,344,1,0,0,0,353,345,1,0,0,0,353,346,
        1,0,0,0,353,347,1,0,0,0,353,348,1,0,0,0,353,349,1,0,0,0,353,350,
        1,0,0,0,353,351,1,0,0,0,353,352,1,0,0,0,354,53,1,0,0,0,355,356,5,
        25,0,0,356,357,3,92,46,0,357,358,5,26,0,0,358,361,1,0,0,0,359,361,
        3,8,4,0,360,355,1,0,0,0,360,359,1,0,0,0,361,55,1,0,0,0,362,367,3,
        58,29,0,363,364,5,40,0,0,364,366,3,58,29,0,365,363,1,0,0,0,366,369,
        1,0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,376,1,0,0,0,369,367,
        1,0,0,0,370,372,3,58,29,0,371,370,1,0,0,0,372,373,1,0,0,0,373,371,
        1,0,0,0,373,374,1,0,0,0,374,376,1,0,0,0,375,362,1,0,0,0,375,371,
        1,0,0,0,376,57,1,0,0,0,377,411,5,58,0,0,378,411,5,57,0,0,379,411,
        5,59,0,0,380,411,5,63,0,0,381,411,5,60,0,0,382,411,5,64,0,0,383,
        386,5,53,0,0,384,385,5,42,0,0,385,387,3,88,44,0,386,384,1,0,0,0,
        386,387,1,0,0,0,387,411,1,0,0,0,388,390,5,54,0,0,389,388,1,0,0,0,
        390,391,1,0,0,0,391,389,1,0,0,0,391,392,1,0,0,0,392,395,1,0,0,0,
        393,394,5,42,0,0,394,396,3,88,44,0,395,393,1,0,0,0,395,396,1,0,0,
        0,396,411,1,0,0,0,397,399,5,42,0,0,398,400,3,88,44,0,399,398,1,0,
        0,0,399,400,1,0,0,0,400,411,1,0,0,0,401,411,3,88,44,0,402,404,5,
        45,0,0,403,402,1,0,0,0,403,404,1,0,0,0,404,405,1,0,0,0,405,411,5,
        75,0,0,406,408,5,45,0,0,407,406,1,0,0,0,407,408,1,0,0,0,408,409,
        1,0,0,0,409,411,5,74,0,0,410,377,1,0,0,0,410,378,1,0,0,0,410,379,
        1,0,0,0,410,380,1,0,0,0,410,381,1,0,0,0,410,382,1,0,0,0,410,383,
        1,0,0,0,410,389,1,0,0,0,410,397,1,0,0,0,410,401,1,0,0,0,410,403,
        1,0,0,0,410,407,1,0,0,0,411,59,1,0,0,0,412,413,5,9,0,0,413,415,3,
        62,31,0,414,416,3,86,43,0,415,414,1,0,0,0,415,416,1,0,0,0,416,61,
        1,0,0,0,417,419,5,37,0,0,418,417,1,0,0,0,418,419,1,0,0,0,419,420,
        1,0,0,0,420,439,5,24,0,0,421,423,5,37,0,0,422,421,1,0,0,0,422,423,
        1,0,0,0,423,424,1,0,0,0,424,439,3,88,44,0,425,427,5,37,0,0,426,425,
        1,0,0,0,426,427,1,0,0,0,427,428,1,0,0,0,428,439,5,64,0,0,429,431,
        5,37,0,0,430,429,1,0,0,0,430,431,1,0,0,0,431,432,1,0,0,0,432,439,
        5,63,0,0,433,435,5,37,0,0,434,433,1,0,0,0,434,435,1,0,0,0,435,436,
        1,0,0,0,436,439,5,69,0,0,437,439,5,57,0,0,438,418,1,0,0,0,438,422,
        1,0,0,0,438,426,1,0,0,0,438,430,1,0,0,0,438,434,1,0,0,0,438,437,
        1,0,0,0,439,63,1,0,0,0,440,441,5,10,0,0,441,443,3,62,31,0,442,444,
        3,86,43,0,443,442,1,0,0,0,443,444,1,0,0,0,444,65,1,0,0,0,445,447,
        5,11,0,0,446,448,3,68,34,0,447,446,1,0,0,0,447,448,1,0,0,0,448,450,
        1,0,0,0,449,451,3,70,35,0,450,449,1,0,0,0,450,451,1,0,0,0,451,67,
        1,0,0,0,452,453,5,38,0,0,453,454,5,73,0,0,454,69,1,0,0,0,455,463,
        5,57,0,0,456,457,3,78,39,0,457,459,5,39,0,0,458,460,3,82,41,0,459,
        458,1,0,0,0,459,460,1,0,0,0,460,463,1,0,0,0,461,463,3,78,39,0,462,
        455,1,0,0,0,462,456,1,0,0,0,462,461,1,0,0,0,463,71,1,0,0,0,464,466,
        5,12,0,0,465,467,3,74,37,0,466,465,1,0,0,0,466,467,1,0,0,0,467,73,
        1,0,0,0,468,470,3,90,45,0,469,468,1,0,0,0,470,471,1,0,0,0,471,469,
        1,0,0,0,471,472,1,0,0,0,472,75,1,0,0,0,473,475,5,13,0,0,474,476,
        3,86,43,0,475,474,1,0,0,0,475,476,1,0,0,0,476,77,1,0,0,0,477,479,
        3,80,40,0,478,477,1,0,0,0,479,480,1,0,0,0,480,478,1,0,0,0,480,481,
        1,0,0,0,481,484,1,0,0,0,482,484,5,63,0,0,483,478,1,0,0,0,483,482,
        1,0,0,0,484,79,1,0,0,0,485,502,3,88,44,0,486,502,5,75,0,0,487,502,
        5,74,0,0,488,502,5,71,0,0,489,502,5,4,0,0,490,502,5,5,0,0,491,502,
        5,6,0,0,492,502,5,41,0,0,493,502,5,40,0,0,494,502,5,42,0,0,495,502,
        5,44,0,0,496,502,5,45,0,0,497,502,5,53,0,0,498,502,5,54,0,0,499,
        502,5,25,0,0,500,502,5,26,0,0,501,485,1,0,0,0,501,486,1,0,0,0,501,
        487,1,0,0,0,501,488,1,0,0,0,501,489,1,0,0,0,501,490,1,0,0,0,501,
        491,1,0,0,0,501,492,1,0,0,0,501,493,1,0,0,0,501,494,1,0,0,0,501,
        495,1,0,0,0,501,496,1,0,0,0,501,497,1,0,0,0,501,498,1,0,0,0,501,
        499,1,0,0,0,501,500,1,0,0,0,502,81,1,0,0,0,503,505,3,90,45,0,504,
        503,1,0,0,0,505,506,1,0,0,0,506,504,1,0,0,0,506,507,1,0,0,0,507,
        83,1,0,0,0,508,509,4,42,1,0,509,510,3,86,43,0,510,85,1,0,0,0,511,
        513,3,90,45,0,512,511,1,0,0,0,513,514,1,0,0,0,514,512,1,0,0,0,514,
        515,1,0,0,0,515,87,1,0,0,0,516,542,5,73,0,0,517,542,5,7,0,0,518,
        542,5,8,0,0,519,542,5,11,0,0,520,542,5,14,0,0,521,542,5,15,0,0,522,
        542,5,16,0,0,523,542,5,17,0,0,524,542,5,18,0,0,525,542,5,19,0,0,
        526,542,5,20,0,0,527,542,5,22,0,0,528,542,5,23,0,0,529,542,5,9,0,
        0,530,542,5,10,0,0,531,542,5,13,0,0,532,542,5,12,0,0,533,534,4,44,
        2,0,534,542,5,21,0,0,535,542,5,46,0,0,536,542,5,47,0,0,537,542,5,
        48,0,0,538,542,5,49,0,0,539,542,5,50,0,0,540,542,5,51,0,0,541,516,
        1,0,0,0,541,517,1,0,0,0,541,518,1,0,0,0,541,519,1,0,0,0,541,520,
        1,0,0,0,541,521,1,0,0,0,541,522,1,0,0,0,541,523,1,0,0,0,541,524,
        1,0,0,0,541,525,1,0,0,0,541,526,1,0,0,0,541,527,1,0,0,0,541,528,
        1,0,0,0,541,529,1,0,0,0,541,530,1,0,0,0,541,531,1,0,0,0,541,532,
        1,0,0,0,541,533,1,0,0,0,541,535,1,0,0,0,541,536,1,0,0,0,541,537,
        1,0,0,0,541,538,1,0,0,0,541,539,1,0,0,0,541,540,1,0,0,0,542,89,1,
        0,0,0,543,590,5,57,0,0,544,590,5,58,0,0,545,590,5,59,0,0,546,590,
        5,60,0,0,547,590,5,61,0,0,548,590,5,62,0,0,549,590,5,63,0,0,550,
        590,5,64,0,0,551,590,5,66,0,0,552,590,5,65,0,0,553,590,5,67,0,0,
        554,590,5,68,0,0,555,590,5,69,0,0,556,590,5,70,0,0,557,590,5,71,
        0,0,558,590,5,4,0,0,559,590,5,5,0,0,560,590,5,6,0,0,561,590,5,56,
        0,0,562,590,5,52,0,0,563,590,5,53,0,0,564,590,5,54,0,0,565,590,5,
        25,0,0,566,567,4,45,3,0,567,590,5,26,0,0,568,590,5,31,0,0,569,590,
        5,32,0,0,570,590,5,33,0,0,571,590,5,34,0,0,572,590,5,35,0,0,573,
        590,5,42,0,0,574,590,5,43,0,0,575,590,5,44,0,0,576,590,5,45,0,0,
        577,590,5,40,0,0,578,590,5,41,0,0,579,590,5,39,0,0,580,590,5,36,
        0,0,581,590,5,38,0,0,582,590,5,72,0,0,583,590,3,88,44,0,584,590,
        5,75,0,0,585,590,5,74,0,0,586,590,5,78,0,0,587,590,5,79,0,0,588,
        590,5,80,0,0,589,543,1,0,0,0,589,544,1,0,0,0,589,545,1,0,0,0,589,
        546,1,0,0,0,589,547,1,0,0,0,589,548,1,0,0,0,589,549,1,0,0,0,589,
        550,1,0,0,0,589,551,1,0,0,0,589,552,1,0,0,0,589,553,1,0,0,0,589,
        554,1,0,0,0,589,555,1,0,0,0,589,556,1,0,0,0,589,557,1,0,0,0,589,
        558,1,0,0,0,589,559,1,0,0,0,589,560,1,0,0,0,589,561,1,0,0,0,589,
        562,1,0,0,0,589,563,1,0,0,0,589,564,1,0,0,0,589,565,1,0,0,0,589,
        566,1,0,0,0,589,568,1,0,0,0,589,569,1,0,0,0,589,570,1,0,0,0,589,
        571,1,0,0,0,589,572,1,0,0,0,589,573,1,0,0,0,589,574,1,0,0,0,589,
        575,1,0,0,0,589,576,1,0,0,0,589,577,1,0,0,0,589,578,1,0,0,0,589,
        579,1,0,0,0,589,580,1,0,0,0,589,581,1,0,0,0,589,582,1,0,0,0,589,
        583,1,0,0,0,589,584,1,0,0,0,589,585,1,0,0,0,589,586,1,0,0,0,589,
        587,1,0,0,0,589,588,1,0,0,0,590,91,1,0,0,0,591,593,3,2,1,0,592,591,
        1,0,0,0,593,596,1,0,0,0,594,592,1,0,0,0,594,595,1,0,0,0,595,93,1,
        0,0,0,596,594,1,0,0,0,74,97,105,109,116,120,123,136,140,145,151,
        153,159,165,170,182,190,192,201,214,219,223,233,240,243,247,251,
        256,261,267,288,292,295,301,305,308,320,330,333,339,353,360,367,
        373,375,386,391,395,399,403,407,410,415,418,422,426,430,434,438,
        443,447,450,459,462,466,471,475,480,483,501,506,514,541,589,594
    ]

class BatchParser ( Parser ):

    grammarFileName = "BatchParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'@'", "'#'", "'$'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'&'", "'|'", "'&&'", "'||'", "'>>'", "'>&'", "'<&'", 
                     "'>'", "'<'", "'=='", "':'", "'/'", "'='", "','", "';'", 
                     "'.'", "'\\'", "'+'", "'-'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'^'", "'*'", "'?'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'!'", "'~'", "'%'" ]

    symbolicNames = [ "<INVALID>", "LINE_COMMENT", "REM", "LABEL", "AT", 
                      "HASH", "DOLLAR", "FOR", "IF", "CALL", "GOTO", "SET", 
                      "SETLOCAL", "ENDLOCAL", "DO", "IN", "EXIST", "DEFINED", 
                      "NOT", "ERRORLEVEL", "CMDEXTVERSION", "ELSE", "EXIT", 
                      "SHIFT", "EOF_KW", "LPAREN", "RPAREN", "AMP", "PIPE", 
                      "AMPAMP", "PIPEPIPE", "APPEND", "DUP_OUT", "DUP_IN", 
                      "GT", "LT", "EQ", "COLON", "SLASH", "EQUALS", "COMMA", 
                      "SEMICOLON", "DOT", "BACKSLASH", "PLUS", "MINUS", 
                      "EQU", "NEQ", "LSS", "LEQ", "GTR", "GEQ", "CARET", 
                      "ASTERISK", "QUESTION", "LINE_CONTINUATION", "CARET_ESCAPE", 
                      "DQ_STRING", "SQ_STRING", "BACKTICK_STRING", "PERCENT_TILDE", 
                      "PERCENT_VAR_SUBSTRING", "PERCENT_VAR_REPLACE", "PERCENT_VAR", 
                      "PERCENT_ARG", "FOR_VAR_TILDE", "FOR_VAR", "BANG_VAR_SUBSTRING", 
                      "BANG_VAR_REPLACE", "BANG_VAR", "BANG", "TILDE", "PERCENT", 
                      "WORD", "HEX_NUMBER", "NUMBER", "WS", "NEWLINE", "UNMATCHED_DQ", 
                      "UNMATCHED_SQ", "UNMATCHED_BACKTICK" ]

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
    RULE_setNamePart = 40
    RULE_setRest = 41
    RULE_genericCmd = 42
    RULE_commandTail = 43
    RULE_argWord = 44
    RULE_token = 45
    RULE_block = 46

    ruleNames =  [ "script", "line", "label", "commandLine", "statement", 
                   "exitStmt", "exitTail", "groupStmt", "shiftStmt", "ifStmt", 
                   "ifIOpt", "ifBody", "elseClause", "ifErrorlevelStmt", 
                   "ifCmdextversionStmt", "ifExistOperand", "ifDefinedOperand", 
                   "ifPredicate", "comparison", "compareOp", "compareOperand", 
                   "forStmt", "forPath", "forSlashMod", "forFOptions", "forFOptionAnchor", 
                   "forFOptionExtra", "forBody", "forList", "forListItem", 
                   "callStmt", "callTarget", "gotoStmt", "setStmt", "setMode", 
                   "setAssign", "setlocalStmt", "setlocalRest", "endlocalStmt", 
                   "setTarget", "setNamePart", "setRest", "genericCmd", 
                   "commandTail", "argWord", "token", "block" ]

    EOF = Token.EOF
    LINE_COMMENT=1
    REM=2
    LABEL=3
    AT=4
    HASH=5
    DOLLAR=6
    FOR=7
    IF=8
    CALL=9
    GOTO=10
    SET=11
    SETLOCAL=12
    ENDLOCAL=13
    DO=14
    IN=15
    EXIST=16
    DEFINED=17
    NOT=18
    ERRORLEVEL=19
    CMDEXTVERSION=20
    ELSE=21
    EXIT=22
    SHIFT=23
    EOF_KW=24
    LPAREN=25
    RPAREN=26
    AMP=27
    PIPE=28
    AMPAMP=29
    PIPEPIPE=30
    APPEND=31
    DUP_OUT=32
    DUP_IN=33
    GT=34
    LT=35
    EQ=36
    COLON=37
    SLASH=38
    EQUALS=39
    COMMA=40
    SEMICOLON=41
    DOT=42
    BACKSLASH=43
    PLUS=44
    MINUS=45
    EQU=46
    NEQ=47
    LSS=48
    LEQ=49
    GTR=50
    GEQ=51
    CARET=52
    ASTERISK=53
    QUESTION=54
    LINE_CONTINUATION=55
    CARET_ESCAPE=56
    DQ_STRING=57
    SQ_STRING=58
    BACKTICK_STRING=59
    PERCENT_TILDE=60
    PERCENT_VAR_SUBSTRING=61
    PERCENT_VAR_REPLACE=62
    PERCENT_VAR=63
    PERCENT_ARG=64
    FOR_VAR_TILDE=65
    FOR_VAR=66
    BANG_VAR_SUBSTRING=67
    BANG_VAR_REPLACE=68
    BANG_VAR=69
    BANG=70
    TILDE=71
    PERCENT=72
    WORD=73
    HEX_NUMBER=74
    NUMBER=75
    WS=76
    NEWLINE=77
    UNMATCHED_DQ=78
    UNMATCHED_SQ=79
    UNMATCHED_BACKTICK=80

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
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    self.line() 
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 100
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
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.label()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.commandLine()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
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
            self.state = 107
            self.match(BatchParser.LABEL)
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 108
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
            self.state = 111
            self.statement()
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 112
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 113
                    self.statement() 
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 119
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
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 122
                self.match(BatchParser.AT)


            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 125
                self.ifStmt()
                pass

            elif la_ == 2:
                self.state = 126
                self.forStmt()
                pass

            elif la_ == 3:
                self.state = 127
                self.callStmt()
                pass

            elif la_ == 4:
                self.state = 128
                self.gotoStmt()
                pass

            elif la_ == 5:
                self.state = 129
                self.setStmt()
                pass

            elif la_ == 6:
                self.state = 130
                self.setlocalStmt()
                pass

            elif la_ == 7:
                self.state = 131
                self.endlocalStmt()
                pass

            elif la_ == 8:
                self.state = 132
                self.exitStmt()
                pass

            elif la_ == 9:
                self.state = 133
                self.shiftStmt()
                pass

            elif la_ == 10:
                self.state = 134
                self.groupStmt()
                pass

            elif la_ == 11:
                self.state = 135
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
            self.state = 138
            self.match(BatchParser.EXIT)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 139
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
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(BatchParser.SLASH)
                self.state = 143
                self.match(BatchParser.WORD)
                self.state = 145
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 144
                    self.match(BatchParser.NUMBER)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 148
                        self.token()

                    else:
                        raise NoViableAltException(self)
                    self.state = 151 
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
            self.state = 155
            self.match(BatchParser.LPAREN)
            self.state = 156
            self.block()
            self.state = 157
            self.match(BatchParser.RPAREN)
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 158
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
            self.state = 161
            self.match(BatchParser.SHIFT)
            self.state = 165
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 162
                    self.token() 
                self.state = 167
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(BatchParser.IF)
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 169
                self.ifIOpt()


            self.state = 172
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
            self.state = 174
            self.match(BatchParser.SLASH)
            self.state = 175
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
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.ifPredicate()
                self.state = 178
                self.match(BatchParser.LPAREN)
                self.state = 179
                self.block()
                self.state = 180
                self.match(BatchParser.RPAREN)
                self.state = 182
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 181
                    self.elseClause()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.ifPredicate()
                self.state = 185
                if not self._notOpenParenThen():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self._notOpenParenThen()")
                self._enterThenStmt()
                self.state = 187
                self.statement()
                self._exitThenStmt()
                self.state = 190
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 189
                    self.elseClause()


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

        def LPAREN(self):
            return self.getToken(BatchParser.LPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(BatchParser.BlockContext,0)


        def RPAREN(self):
            return self.getToken(BatchParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(BatchParser.StatementContext,0)


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
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(BatchParser.ELSE)
                self.state = 195
                self.match(BatchParser.LPAREN)
                self.state = 196
                self.block()
                self.state = 197
                self.match(BatchParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(BatchParser.ELSE)
                self.state = 200
                self.statement()
                pass


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
            self.state = 203
            self.match(BatchParser.ERRORLEVEL)
            self.state = 204
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
            self.state = 206
            self.match(BatchParser.CMDEXTVERSION)
            self.state = 207
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

        def ASTERISK(self):
            return self.getToken(BatchParser.ASTERISK, 0)

        def DOT(self):
            return self.getToken(BatchParser.DOT, 0)

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def QUESTION(self, i:int=None):
            if i is None:
                return self.getTokens(BatchParser.QUESTION)
            else:
                return self.getToken(BatchParser.QUESTION, i)

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

        def BANG_VAR_SUBSTRING(self):
            return self.getToken(BatchParser.BANG_VAR_SUBSTRING, 0)

        def BANG_VAR_REPLACE(self):
            return self.getToken(BatchParser.BANG_VAR_REPLACE, 0)

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
        try:
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(BatchParser.DQ_STRING)
                pass
            elif token in [73]:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(BatchParser.WORD)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.match(BatchParser.ASTERISK)
                self.state = 214
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 212
                    self.match(BatchParser.DOT)
                    self.state = 213
                    self.argWord()


                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 4)
                self.state = 217 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 216
                        self.match(BatchParser.QUESTION)

                    else:
                        raise NoViableAltException(self)
                    self.state = 219 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 223
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 221
                    self.match(BatchParser.DOT)
                    self.state = 222
                    self.argWord()


                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 5)
                self.state = 225
                self.match(BatchParser.PERCENT_VAR)
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 6)
                self.state = 226
                self.match(BatchParser.PERCENT_TILDE)
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 7)
                self.state = 227
                self.match(BatchParser.PERCENT_ARG)
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 8)
                self.state = 228
                self.match(BatchParser.FOR_VAR)
                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 9)
                self.state = 229
                self.match(BatchParser.FOR_VAR_TILDE)
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 10)
                self.state = 230
                self.match(BatchParser.BANG_VAR_SUBSTRING)
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 11)
                self.state = 231
                self.match(BatchParser.BANG_VAR_REPLACE)
                pass
            elif token in [69]:
                self.enterOuterAlt(localctx, 12)
                self.state = 232
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
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.argWord()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(BatchParser.PERCENT_VAR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.match(BatchParser.FOR_VAR)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.match(BatchParser.FOR_VAR_TILDE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.match(BatchParser.BANG_VAR)
                pass


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
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 242
                    self.match(BatchParser.NOT)


                self.state = 245
                self.ifErrorlevelStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 246
                    self.match(BatchParser.NOT)


                self.state = 249
                self.ifCmdextversionStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 250
                    self.match(BatchParser.NOT)


                self.state = 253
                self.match(BatchParser.DEFINED)
                self.state = 254
                self.ifDefinedOperand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==18:
                    self.state = 255
                    self.match(BatchParser.NOT)


                self.state = 258
                self.match(BatchParser.EXIST)
                self.state = 259
                self.ifExistOperand()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 261
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 260
                    self.match(BatchParser.NOT)


                self.state = 263
                self.comparison()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 264
                self.match(BatchParser.DQ_STRING)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 265
                self.match(BatchParser.PERCENT_TILDE)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 266
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
            self.state = 269
            self.compareOperand()
            self.state = 270
            self.compareOp()
            self.state = 271
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
            self.state = 273
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4433299602669568) != 0)):
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

        def BANG_VAR_SUBSTRING(self):
            return self.getToken(BatchParser.BANG_VAR_SUBSTRING, 0)

        def BANG_VAR_REPLACE(self):
            return self.getToken(BatchParser.BANG_VAR_REPLACE, 0)

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
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(BatchParser.DQ_STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(BatchParser.PERCENT_TILDE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.match(BatchParser.PERCENT_VAR_SUBSTRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 278
                self.match(BatchParser.PERCENT_VAR_REPLACE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 279
                self.match(BatchParser.PERCENT_VAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 280
                self.match(BatchParser.PERCENT_ARG)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 281
                self.match(BatchParser.FOR_VAR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 282
                self.match(BatchParser.FOR_VAR_TILDE)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 283
                self.match(BatchParser.BANG_VAR_SUBSTRING)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 284
                self.match(BatchParser.BANG_VAR_REPLACE)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 285
                self.match(BatchParser.BANG_VAR)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 286
                self.argWord()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 287
                    self.match(BatchParser.MINUS)


                self.state = 290
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 291
                    self.match(BatchParser.MINUS)


                self.state = 294
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(BatchParser.FOR)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 298
                    self.forSlashMod() 
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 304
                self.forFOptions()


            self.state = 308
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 307
                self.forPath()


            self.state = 310
            self.match(BatchParser.FOR_VAR)
            self.state = 311
            self.match(BatchParser.IN)
            self.state = 312
            self.match(BatchParser.LPAREN)
            self.state = 313
            self.forList()
            self.state = 314
            self.match(BatchParser.RPAREN)
            self.state = 315
            self.match(BatchParser.DO)
            self.state = 316
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
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.argWord()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.match(BatchParser.DQ_STRING)
                pass


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
            self.state = 322
            self.match(BatchParser.SLASH)
            self.state = 323
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
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(BatchParser.DQ_STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.forFOptionAnchor()
                self.state = 330
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 327
                        self.forFOptionExtra() 
                    self.state = 332
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

                pass


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
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.argWord()
                self.state = 336
                self.match(BatchParser.CARET_ESCAPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.match(BatchParser.CARET_ESCAPE)
                pass


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

        def QUESTION(self):
            return self.getToken(BatchParser.QUESTION, 0)

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
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.argWord()
                self.state = 342
                self.match(BatchParser.CARET_ESCAPE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.match(BatchParser.CARET_ESCAPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 346
                self.match(BatchParser.COMMA)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 347
                self.match(BatchParser.ASTERISK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 348
                self.match(BatchParser.QUESTION)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 349
                self.match(BatchParser.MINUS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 350
                self.match(BatchParser.PLUS)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 351
                self.match(BatchParser.PERCENT)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 352
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
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(BatchParser.LPAREN)
                self.state = 356
                self.block()
                self.state = 357
                self.match(BatchParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
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
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.forListItem()
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==40:
                    self.state = 363
                    self.match(BatchParser.COMMA)
                    self.state = 364
                    self.forListItem()
                    self.state = 369
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 370
                        self.forListItem()

                    else:
                        raise NoViableAltException(self)
                    self.state = 373 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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


        def QUESTION(self, i:int=None):
            if i is None:
                return self.getTokens(BatchParser.QUESTION)
            else:
                return self.getToken(BatchParser.QUESTION, i)

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
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(BatchParser.SQ_STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.match(BatchParser.DQ_STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 379
                self.match(BatchParser.BACKTICK_STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 380
                self.match(BatchParser.PERCENT_VAR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 381
                self.match(BatchParser.PERCENT_TILDE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 382
                self.match(BatchParser.PERCENT_ARG)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 383
                self.match(BatchParser.ASTERISK)
                self.state = 386
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 384
                    self.match(BatchParser.DOT)
                    self.state = 385
                    self.argWord()


                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 389 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 388
                        self.match(BatchParser.QUESTION)

                    else:
                        raise NoViableAltException(self)
                    self.state = 391 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

                self.state = 395
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 393
                    self.match(BatchParser.DOT)
                    self.state = 394
                    self.argWord()


                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 397
                self.match(BatchParser.DOT)
                self.state = 399
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 398
                    self.argWord()


                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 401
                self.argWord()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 402
                    self.match(BatchParser.MINUS)


                self.state = 405
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 407
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==45:
                    self.state = 406
                    self.match(BatchParser.MINUS)


                self.state = 409
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
            self.state = 412
            self.match(BatchParser.CALL)
            self.state = 413
            self.callTarget()
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 414
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
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 417
                    self.match(BatchParser.COLON)


                self.state = 420
                self.match(BatchParser.EOF_KW)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 421
                    self.match(BatchParser.COLON)


                self.state = 424
                self.argWord()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 425
                    self.match(BatchParser.COLON)


                self.state = 428
                self.match(BatchParser.PERCENT_ARG)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 429
                    self.match(BatchParser.COLON)


                self.state = 432
                self.match(BatchParser.PERCENT_VAR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 433
                    self.match(BatchParser.COLON)


                self.state = 436
                self.match(BatchParser.BANG_VAR)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 437
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


        def commandTail(self):
            return self.getTypedRuleContext(BatchParser.CommandTailContext,0)


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
            self.state = 440
            self.match(BatchParser.GOTO)
            self.state = 441
            self.callTarget()
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.state = 442
                self.commandTail()


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

        def setMode(self):
            return self.getTypedRuleContext(BatchParser.SetModeContext,0)


        def setAssign(self):
            return self.getTypedRuleContext(BatchParser.SetAssignContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(BatchParser.SET)
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 446
                self.setMode()


            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 449
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
            self.state = 452
            self.match(BatchParser.SLASH)
            self.state = 453
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
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(BatchParser.DQ_STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.setTarget()
                self.state = 457
                self.match(BatchParser.EQUALS)
                self.state = 459
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                if la_ == 1:
                    self.state = 458
                    self.setRest()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 461
                self.setTarget()
                pass


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
            self.state = 464
            self.match(BatchParser.SETLOCAL)
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.state = 465
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
            self.state = 469 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 468
                    self.token()

                else:
                    raise NoViableAltException(self)
                self.state = 471 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

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
            self.state = 473
            self.match(BatchParser.ENDLOCAL)
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.state = 474
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

        def setNamePart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BatchParser.SetNamePartContext)
            else:
                return self.getTypedRuleContext(BatchParser.SetNamePartContext,i)


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
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 477
                        self.setNamePart()

                    else:
                        raise NoViableAltException(self)
                    self.state = 480 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.match(BatchParser.PERCENT_VAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetNamePartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argWord(self):
            return self.getTypedRuleContext(BatchParser.ArgWordContext,0)


        def NUMBER(self):
            return self.getToken(BatchParser.NUMBER, 0)

        def HEX_NUMBER(self):
            return self.getToken(BatchParser.HEX_NUMBER, 0)

        def TILDE(self):
            return self.getToken(BatchParser.TILDE, 0)

        def AT(self):
            return self.getToken(BatchParser.AT, 0)

        def HASH(self):
            return self.getToken(BatchParser.HASH, 0)

        def DOLLAR(self):
            return self.getToken(BatchParser.DOLLAR, 0)

        def SEMICOLON(self):
            return self.getToken(BatchParser.SEMICOLON, 0)

        def COMMA(self):
            return self.getToken(BatchParser.COMMA, 0)

        def DOT(self):
            return self.getToken(BatchParser.DOT, 0)

        def PLUS(self):
            return self.getToken(BatchParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(BatchParser.MINUS, 0)

        def ASTERISK(self):
            return self.getToken(BatchParser.ASTERISK, 0)

        def QUESTION(self):
            return self.getToken(BatchParser.QUESTION, 0)

        def LPAREN(self):
            return self.getToken(BatchParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BatchParser.RPAREN, 0)

        def getRuleIndex(self):
            return BatchParser.RULE_setNamePart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetNamePart" ):
                return visitor.visitSetNamePart(self)
            else:
                return visitor.visitChildren(self)




    def setNamePart(self):

        localctx = BatchParser.SetNamePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_setNamePart)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.argWord()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 486
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 487
                self.match(BatchParser.HEX_NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 488
                self.match(BatchParser.TILDE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 489
                self.match(BatchParser.AT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 490
                self.match(BatchParser.HASH)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 491
                self.match(BatchParser.DOLLAR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 492
                self.match(BatchParser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 493
                self.match(BatchParser.COMMA)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 494
                self.match(BatchParser.DOT)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 495
                self.match(BatchParser.PLUS)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 496
                self.match(BatchParser.MINUS)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 497
                self.match(BatchParser.ASTERISK)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 498
                self.match(BatchParser.QUESTION)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 499
                self.match(BatchParser.LPAREN)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 500
                self.match(BatchParser.RPAREN)
                pass


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
        self.enterRule(localctx, 82, self.RULE_setRest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 503
                    self.token()

                else:
                    raise NoViableAltException(self)
                self.state = 506 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,69,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_genericCmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            if not self._notForToken() and self._notLonelyParen():
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "self._notForToken() and self._notLonelyParen()")
            self.state = 509
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
        self.enterRule(localctx, 86, self.RULE_commandTail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 511
                    self.token()

                else:
                    raise NoViableAltException(self)
                self.state = 514 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,70,self._ctx)

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

        def ELSE(self):
            return self.getToken(BatchParser.ELSE, 0)

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
        self.enterRule(localctx, 88, self.RULE_argWord)
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.match(BatchParser.WORD)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(BatchParser.FOR)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 518
                self.match(BatchParser.IF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 519
                self.match(BatchParser.SET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 520
                self.match(BatchParser.DO)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 521
                self.match(BatchParser.IN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 522
                self.match(BatchParser.EXIST)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 523
                self.match(BatchParser.DEFINED)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 524
                self.match(BatchParser.NOT)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 525
                self.match(BatchParser.ERRORLEVEL)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 526
                self.match(BatchParser.CMDEXTVERSION)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 527
                self.match(BatchParser.EXIT)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 528
                self.match(BatchParser.SHIFT)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 529
                self.match(BatchParser.CALL)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 530
                self.match(BatchParser.GOTO)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 531
                self.match(BatchParser.ENDLOCAL)
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 532
                self.match(BatchParser.SETLOCAL)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 533
                if not self._elseAsArgAllowed():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self._elseAsArgAllowed()")
                self.state = 534
                self.match(BatchParser.ELSE)
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 535
                self.match(BatchParser.EQU)
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 536
                self.match(BatchParser.NEQ)
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 537
                self.match(BatchParser.LSS)
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 538
                self.match(BatchParser.LEQ)
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 539
                self.match(BatchParser.GTR)
                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 540
                self.match(BatchParser.GEQ)
                pass


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

        def BANG_VAR_SUBSTRING(self):
            return self.getToken(BatchParser.BANG_VAR_SUBSTRING, 0)

        def BANG_VAR_REPLACE(self):
            return self.getToken(BatchParser.BANG_VAR_REPLACE, 0)

        def BANG_VAR(self):
            return self.getToken(BatchParser.BANG_VAR, 0)

        def BANG(self):
            return self.getToken(BatchParser.BANG, 0)

        def TILDE(self):
            return self.getToken(BatchParser.TILDE, 0)

        def AT(self):
            return self.getToken(BatchParser.AT, 0)

        def HASH(self):
            return self.getToken(BatchParser.HASH, 0)

        def DOLLAR(self):
            return self.getToken(BatchParser.DOLLAR, 0)

        def CARET_ESCAPE(self):
            return self.getToken(BatchParser.CARET_ESCAPE, 0)

        def CARET(self):
            return self.getToken(BatchParser.CARET, 0)

        def ASTERISK(self):
            return self.getToken(BatchParser.ASTERISK, 0)

        def QUESTION(self):
            return self.getToken(BatchParser.QUESTION, 0)

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

        def SEMICOLON(self):
            return self.getToken(BatchParser.SEMICOLON, 0)

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
        self.enterRule(localctx, 90, self.RULE_token)
        try:
            self.state = 589
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.match(BatchParser.DQ_STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                self.match(BatchParser.SQ_STRING)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 545
                self.match(BatchParser.BACKTICK_STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 546
                self.match(BatchParser.PERCENT_TILDE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 547
                self.match(BatchParser.PERCENT_VAR_SUBSTRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 548
                self.match(BatchParser.PERCENT_VAR_REPLACE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 549
                self.match(BatchParser.PERCENT_VAR)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 550
                self.match(BatchParser.PERCENT_ARG)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 551
                self.match(BatchParser.FOR_VAR)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 552
                self.match(BatchParser.FOR_VAR_TILDE)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 553
                self.match(BatchParser.BANG_VAR_SUBSTRING)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 554
                self.match(BatchParser.BANG_VAR_REPLACE)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 555
                self.match(BatchParser.BANG_VAR)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 556
                self.match(BatchParser.BANG)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 557
                self.match(BatchParser.TILDE)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 558
                self.match(BatchParser.AT)
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 559
                self.match(BatchParser.HASH)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 560
                self.match(BatchParser.DOLLAR)
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 561
                self.match(BatchParser.CARET_ESCAPE)
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 562
                self.match(BatchParser.CARET)
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 563
                self.match(BatchParser.ASTERISK)
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 564
                self.match(BatchParser.QUESTION)
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 565
                self.match(BatchParser.LPAREN)
                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 566
                if not self._notLonelyParen():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self._notLonelyParen()")
                self.state = 567
                self.match(BatchParser.RPAREN)
                pass

            elif la_ == 25:
                self.enterOuterAlt(localctx, 25)
                self.state = 568
                self.match(BatchParser.APPEND)
                pass

            elif la_ == 26:
                self.enterOuterAlt(localctx, 26)
                self.state = 569
                self.match(BatchParser.DUP_OUT)
                pass

            elif la_ == 27:
                self.enterOuterAlt(localctx, 27)
                self.state = 570
                self.match(BatchParser.DUP_IN)
                pass

            elif la_ == 28:
                self.enterOuterAlt(localctx, 28)
                self.state = 571
                self.match(BatchParser.GT)
                pass

            elif la_ == 29:
                self.enterOuterAlt(localctx, 29)
                self.state = 572
                self.match(BatchParser.LT)
                pass

            elif la_ == 30:
                self.enterOuterAlt(localctx, 30)
                self.state = 573
                self.match(BatchParser.DOT)
                pass

            elif la_ == 31:
                self.enterOuterAlt(localctx, 31)
                self.state = 574
                self.match(BatchParser.BACKSLASH)
                pass

            elif la_ == 32:
                self.enterOuterAlt(localctx, 32)
                self.state = 575
                self.match(BatchParser.PLUS)
                pass

            elif la_ == 33:
                self.enterOuterAlt(localctx, 33)
                self.state = 576
                self.match(BatchParser.MINUS)
                pass

            elif la_ == 34:
                self.enterOuterAlt(localctx, 34)
                self.state = 577
                self.match(BatchParser.COMMA)
                pass

            elif la_ == 35:
                self.enterOuterAlt(localctx, 35)
                self.state = 578
                self.match(BatchParser.SEMICOLON)
                pass

            elif la_ == 36:
                self.enterOuterAlt(localctx, 36)
                self.state = 579
                self.match(BatchParser.EQUALS)
                pass

            elif la_ == 37:
                self.enterOuterAlt(localctx, 37)
                self.state = 580
                self.match(BatchParser.EQ)
                pass

            elif la_ == 38:
                self.enterOuterAlt(localctx, 38)
                self.state = 581
                self.match(BatchParser.SLASH)
                pass

            elif la_ == 39:
                self.enterOuterAlt(localctx, 39)
                self.state = 582
                self.match(BatchParser.PERCENT)
                pass

            elif la_ == 40:
                self.enterOuterAlt(localctx, 40)
                self.state = 583
                self.argWord()
                pass

            elif la_ == 41:
                self.enterOuterAlt(localctx, 41)
                self.state = 584
                self.match(BatchParser.NUMBER)
                pass

            elif la_ == 42:
                self.enterOuterAlt(localctx, 42)
                self.state = 585
                self.match(BatchParser.HEX_NUMBER)
                pass

            elif la_ == 43:
                self.enterOuterAlt(localctx, 43)
                self.state = 586
                self.match(BatchParser.UNMATCHED_DQ)
                pass

            elif la_ == 44:
                self.enterOuterAlt(localctx, 44)
                self.state = 587
                self.match(BatchParser.UNMATCHED_SQ)
                pass

            elif la_ == 45:
                self.enterOuterAlt(localctx, 45)
                self.state = 588
                self.match(BatchParser.UNMATCHED_BACKTICK)
                pass


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
        self.enterRule(localctx, 92, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 591
                    self.line() 
                self.state = 596
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

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
        self._predicates[11] = self.ifBody_sempred
        self._predicates[42] = self.genericCmd_sempred
        self._predicates[44] = self.argWord_sempred
        self._predicates[45] = self.token_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def ifBody_sempred(self, localctx:IfBodyContext, predIndex:int):
            if predIndex == 0:
                return self._notOpenParenThen()
         

    def genericCmd_sempred(self, localctx:GenericCmdContext, predIndex:int):
            if predIndex == 1:
                return self._notForToken() and self._notLonelyParen()
         

    def argWord_sempred(self, localctx:ArgWordContext, predIndex:int):
            if predIndex == 2:
                return self._elseAsArgAllowed()
         

    def token_sempred(self, localctx:TokenContext, predIndex:int):
            if predIndex == 3:
                return self._notLonelyParen()
         




