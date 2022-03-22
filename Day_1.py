# 1) Print out the whole multiplication table of the given Number.
def solve(N):
    print("The Multiplication Table of the:", N, "is given below:")
    for i in range(1, 11):
        print(N, " * ", i, " = ", (N * i))
    return 0


solve(25)
# Output
# The Multiplication Table of the: 25 is given below:
# 25  *  1  =  25
# 25  *  2  =  50
# 25  *  3  =  75
# 25  *  4  =  100
# 25  *  5  =  125
# 25  *  6  =  150
# 25  *  7  =  175
# 25  *  8  =  200
# 25  *  9  =  225
# 25  *  10  =  250
