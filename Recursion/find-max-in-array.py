#find max in array through recursion
def max_in_array(arr,start,end):
    if start==end:
        return arr[end]
    maximum=max_in_array(arr,start+1,end)
    return max(arr[start],maximum)