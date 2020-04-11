operators = { '+', '-', '*', '/', '**', '%', '&', '|', '!'}
def check_syntax( tokens ):
    res = False
    if( len(tokens) == 3 ):
        a, op, b = tokens
        try:
            aa = float(a)
            bb = float(b)
        except ValueError:
            return res
        if( op in operators ):
            res = True
    elif(len(tokens) == 2):
        a, op = tokens
        try:
            aa = float(a)
        except ValueError:
            return res
        if( op == '!' ):
            res = True
    return res

#operators = { '+', '-', '*', '/', '**', '%', '&', '|', '!'}
def solve(tokens):
    if( len(tokens) == 3 ):
        a, op, b = tokens
        aa = float(a)
        bb = float(b)
        if( op == '+'):
            return aa + bb
        if( op == '-'):
            return aa - bb
        if( op == '*'):
            return aa * bb
        if( op == '/'):
            try:
                return aa / bb
            except ZeroDivisionError as e:
                return "Syntax Error: {}".format(e)
        if( op == '**' ):
            if( aa != int(aa) or bb != int(bb) ):
                return "Syntax Error: support only \'int ** int\'"
            aa = int(aa)
            bb = int(bb)
            res = 1
            for i in range(bb):
                res = res * aa
            return res
        if( op == '%' ):
            if( aa != int(aa) or bb != int(bb) ):
                return "Syntax Error: support only \'int | int\'"
            aa = int(aa)
            bb = int(bb)
            try:
                return aa - int(aa / bb) * bb
            except ZeroDivisionError as e:
                return "Syntax Error: {}".format(e)
        if( op == '&' ):
            if( a not in {'0', '1'} or b not in {'0', '1'} ):
                return "Syntax Error: support only \'[01] | [01]\'"
            aa = int(aa)
            bb = int(bb)
            if( aa == 1 and bb == 1 ):
                return 1
            return 0
        if( op == '|' ):
            if( a not in {'0', '1'} or b not in {'0', '1'} ):
                return "Syntax Error: support only \'[01] | [01]\'"
            aa = int(aa)
            bb = int(bb)
            if( aa == 1 or bb == 1 ):
                return 1
            return 0
    elif(len(tokens) == 2):
        a, op = tokens
        aa = float(a)
        if( op == '!' ):
            if( aa != int(aa) ):
                return "Syntax Error: support only \'int !\'"
            aa = int(aa)
            res = 1
            for i in range(1, aa+1):
                res = res * i
            return res

    return "Syntax Error"

def parse_request( string ):
    tokens = string.strip().split()

    if( check_syntax(tokens) == False ):
        return "Syntax Error"

    return str(solve(tokens))
