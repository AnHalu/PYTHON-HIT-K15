from functools import reduce
def myMathShower (*args) :
    res = reduce(lambda a,b : a*b ,args)
    return sum(args) , res , args[0]*2 - sum(args)

sum , tich , hieu = myMathShower(10, 4, 1, 1)
print(sum , tich , hieu )