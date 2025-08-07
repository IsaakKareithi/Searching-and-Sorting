# Program to perform recursive binary search

def binarySearch(arr, l, r, x):

    #Check if length is greater than or equal to 0
    if r >= l:

        #Find the mid element's index
        mid = l +(r-1) // 2

        # If element is present at the middle element itself
        if arr[mid] == x:
            return mid
        
        # If element is smaller check in the leftmost subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        
        #ELse check in right subarry
        else:
            return binarySearch(arr, r, mid+1, x)
        
    else:

        # Element is not present in array
        return -1
    
#Driver code
arr = [2,4,3,10,40]
x = 10

#Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element {} is present in array at index {}.".format(x, result))

else:
    print("Element is not present in array")