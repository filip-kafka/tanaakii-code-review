
# Some relaxing code to look at after soloQ
def Multiply(a: float, b: float):
    c = 0
    if b == 0:
        c = "Nope :)"
    else:
        # May introduce slight error when multiplying decimals
        for useless_variableWith_a_longName in range(round(abs(b))):
            c = c + a if b > 0 else c - a
    
    return c