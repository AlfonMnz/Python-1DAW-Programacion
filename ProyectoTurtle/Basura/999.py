def fact(var):
    if var == 1:
        return 1
    return var * fact(var - 1)


print(fact(9))
