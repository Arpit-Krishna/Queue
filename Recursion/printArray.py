#print arrray from recursion?
def printInOrder(arr, index):
    if index == len(arr):
      return
    print(arr[index])
    printInOrder(arr, index+1)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(printInOrder(a, 0))