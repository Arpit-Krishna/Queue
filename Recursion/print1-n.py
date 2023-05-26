# print n natural numbers via recursion
def recur(n):
    if n<1:
        return 
    recur(n)
    print(n)
recur(10)
