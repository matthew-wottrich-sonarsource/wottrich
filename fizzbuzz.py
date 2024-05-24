for fizzbuzz in range(100):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

#for fizzbuzz in range(100):
#    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#        print("fizzbuzz")
#        continue
#    elif fizzbuzz % 3 == 0:
#        print("fizz")
#        continue
#    elif fizzbuzz % 5 == 0:
#        print("buzz")
#        continue
#    print(fizzbuzz)

#for fizzbuzz in range(100):
#    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#        print("fizzbuzz")
#        continue
#    elif fizzbuzz % 3 == 0:
#        print("fizz")
#        continue
#    elif fizzbuzz % 5 == 0:
#        print("buzz")
#        continue
#    print(fizzbuzz)

def func_x(num):
    if num == 1:
        return a()
    elif num == 2:
        return b()
    elif num == 3:
        return c()
    elif num == 4:
        return d()
    elif num == 5:
        return e()


# Better
def func_y(num):
    mapper = {
        1: a,
        2: b,
        3: c,
        4: d,
        5: e
    }
    return mapper[num]()
