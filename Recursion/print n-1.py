# print n natural numbers in reverse via recursion
def recur(n):
    if n<1:
        return
    print(n) 
    recur(n)
    
recur(10)
