rules = [
    # ME
    ['Me', ['Exp']],
    ['Me', ['Exp', 'extExp']],

    ['extExp', ['relopExp']],
    ['extExp', ['relopExp', 'extExp']],

    ['relopExp', ['relop', 'Exp']],

    # Exp
    ['Exp', ['BRACKETLEFT', 'Exp', 'BRACKETRIGHT']],# adhoc
    ['Exp', ['Term']],
    ['Exp', ['Term', 'extTerm']],

    ['extTerm', ['sumopTerm']],
    ['extTerm', ['sumopTerm', 'extTerm']],

    ['sumopTerm', ['sumop', 'Term']],

    # Term
    ['Term', ['Factor']],
    ['Term', ['Factor', 'extFactor']],

    ['extFactor', ['mulopFactor']],
    ['extFactor', ['mulopFactor' , 'extFactor']],

    ['mulopFactor', ['mulop', 'Factor']],
    ['mulopFactor', ['Factor']], # without mul

    # Factor
    ['Factor', ['IDVAR']],
    ['Factor', ['CN']],

    # Op
    ['relop', ['EQUAL']],
    ['relop', ['SIMEQUAL']],
    ['relop', ['LESS']],
    ['relop', ['GREATER']],
    ['relop', ['LESSEQ']],
    ['relop', ['GREATEREQ']],
    ['relop', ['LEFTARROW']],# assignment
    # set part
    ['relop', ['IN']],

    ['sumop', ['PLUS']],
    ['sumop', ['MINUS']],
    ['sumop', ['CUP']],

    ['mulop', ['MUL']],
    ['mulop', ['DIV']],
    ['mulop', ['CAP']],

    # TODO, which level?
    #['setop', ['CUP']],

    ['singleop', ['LOG']],# list of function only receiving one argument
    ['singleop', ['O']],# list of function only receiving one argument
    ['singleop', ['MIN']],# list of function only receiving one argument

    # fence
    ['GroupOpen', ['BRACKETLEFT']],
    ['GroupClose', ['BRACKETRIGHT']],
    ['ArgOpen', ['BRACKETLEFT']],
    ['ArgClose', ['BRACKETRIGHT']],

    ['AbsOpen', ['VERTBAR']],
    ['AbsClose', ['VERTBAR']],
    ['CardOpen', ['VERTBAR']],
    ['CardClose', ['VERTBAR']],
    ['NormOpen', ['DOUBLEVERTBAR']],
    ['NormClose', ['DOUBLEVERTBAR']],

    ['NormFactor', ['NormOpen', 'Exp', 'NormClose']],
    ['NormFactor', ['NormFactor', 'SUBOPEN', 'Exp', 'SUBCLOSE']],# type of norm
    ['NormFactor', ['NormFactor', 'SUBOPEN', 'ExpList', 'SUBCLOSE']],# adhoc

    ['Factor', ['GroupOpen', 'Exp', 'GroupClose']],
    ['Factor', ['AbsOpen', 'Exp', 'AbsClose']],
    ['Factor', ['CardOpen', 'Exp', 'CardClose']], # should be a set within
    ['Factor', ['NormFactor']],
    ['Factor', ['SetFactor']],

    ['Factor', ['SQRTOPEN', 'Exp', 'SQRTCLOSE']],
    ['Factor', ['singleop', 'Exp']],
    ['Factor', ['singleop', 'ArgOpen', 'Exp', 'ArgClose']],

    # big op
    ['Factor', ['BigOpExp']],
    ['BigOpExp', ['BigOp', 'BigOpUnder', 'Exp']],
    ['BigOpExp', ['BigOp', 'BigOpSub', 'Exp']],
    ['BigOpExp', ['BigOp', 'BigOpSub', 'BigOpSup', 'Exp']],
    # TODO, this could be a relation
    ['BigOpUnder', ['UNDEROPEN', 'Exp', 'UNDERCLOSE']],
    ['BigOpSub', ['SUBOPEN', 'Me', 'SUBCLOSE']],
    ['BigOpSup', ['SUPOPEN', 'Exp', 'SUPCLOSE']],
    # adhoc rule
    ['BigOpSub', ['SUBOPEN', 'ExpList', 'EQUAL', 'CN', 'SUBCLOSE']],

    ['BigOp', ['SUM']],
    ['BigOp', ['MIN']],

    # TODO, List of term
    # separated by comma
    # example V_{A, k}
    #['IDVARList', ['IDVAR', 'PUNCTCOMMA', 'IDVAR']],

    # sup, sub
    ['Factor', ['SubFactor']],
    ['SubFactor',['Factor', 'SUBOPEN', 'Exp', 'SUBCLOSE']],
    ['SubFactor',['Factor', 'SUBOPEN', 'ExpList', 'SUBCLOSE']],
    ['Factor', ['SupFactor']],
    ['SupFactor', ['Factor', 'SUPOPEN', 'Exp', 'SUPCLOSE']],

    # TODO, named function

    # collection related
    ['ExpList', ['Exp', 'extExpList']],
    ['extExpList', ['PunctCommaExp']],
    ['extExpList', ['PunctCommaExp', 'extExpList']],
    ['PunctCommaExp', ['PUNCTCOMMA', 'Exp']],

    ['SetOpen', ['CURVEBRACKETLEFT']],
    ['SetClose', ['CURVEBRACKETRIGHT']],
    ['SetFactor', ['SetOpen', 'ExpList', 'SetClose']],
    ['SetFactor', ['SetOpen', 'Exp', 'SetClose']],
    ['SetFactor', ['REALDOMAIN']],
    ['SetFactor', ['EMPTY']],
    ['SetFactor', ['SetFactor', 'SetSup']], # product of Set
    ['SetFactor', ['SetFactor', 'SetSub', 'SetSup']], # value range of free variable

    # kind of adhoc here
    ['SetSub', ['SUBOPEN', 'Me', 'SUBCLOSE']],
    ['SetSup', ['SUPOPEN', 'Me', 'SUPCLOSE']],




]




