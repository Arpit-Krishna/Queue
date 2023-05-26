#print arrray in reverse from recursion
def printInOrder(arr, index):
    if index == len(arr):
      return
    printInOrder(arr, index+1)
    print(arr[index])
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(printInOrder(a, 0))
