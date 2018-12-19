import re
from sets import Set

REALDOMAIN="REALDOMAIN"
DAGGER="DAGGER"
LOG="LOG"
NORMCLOSE="NORMCLOSE"
SUM="SUM"
SUBCLOSE="SUBCLOSE"
VERTBAR="VERTBAR"
SETCLOSE="SETCLOSE"
MUL="MUL"
DIV="DIV"
MINUS="MINUS"
EMPTY="EMPTY"
SQRTOPEN="SQRTOPEN"
SIMEQUAL="SIMEQUAL"
LESS="LESS"
TODO="TODO"
MIN="MIN"
CUP="CUP"
BRACKETLEFT="BRACKETLEFT"
BIGO="BIGO"
IDVAR="IDVAR"
PUNCTCOMMA="PUNCTCOMMA"
A="A"
CN="CN"
LEFTARROW="LEFTARROW"
O="O"
EQUAL="EQUAL"
CNF="CNF"
NORMOPEN="NORMOPEN"
SUPOPEN="SUPOPEN"
T="T"
IN="IN"
SUPCLOSE="SUPCLOSE"
UNDEROPEN="UNDEROPEN"
UNDERCLOSE="UNDERCLOSE"
SQRTCLOSE="SQRTCLOSE"
SUBOPEN="SUBOPEN"
SETOPEN="SETOPEN"
BRACKETRIGHT="BRACKETRIGHT"
CURVEBRACKETLEFT="CURVEBRACKETLEFT"
CURVEBRACKETRIGHT="CURVEBRACKETRIGHT"
DOUBLEVERTBAR="DOUBLEVERTBAR"


def get_all_upper():
    t_set = Set()
    lines = open("CNFParser_unittest.py").readlines()
    for line in lines:
        ws = line.strip().split(" ")
        #print ws
        for w in ws:
            if w.isupper() and re.match(r'^[A-Z]*$', w):
                t_set.add(w)
    for t in t_set:
        print '%s="%s"'%(t, t)

if __name__ == '__main__':
    get_all_upper()
