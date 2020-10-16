#Anonymous function:A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression


# example = lambda a : a * 10
# print(example(5))

# example2 = lambda a,b,c : a + b *c

# print(example2(2,5,6))

# def function10(a,b,c):
#     return a*b+c
# print(function10(2,5,6))

#Power of lambda 
def functionexample(n):

    return lambda a: a * n

x = functionexample(2)
print(x(11))

