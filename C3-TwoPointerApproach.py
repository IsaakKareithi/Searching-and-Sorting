# Using two pointer method

def isPairSum(A,N,X):

    #First pointer
    i = 0

    #Second pointer
    j = N - 1

    while (i < j):

        # If we find a pair
        if (A[i] +A[j] == X):
            return [A[i],A[j]]
        
        #if sum of element at current pointers is less,
        #we move to higher values
        elif (A[i]+ A[j] < X):
            i += 1

        #IF sum of elements at currnet pointer is more,
        #move pointer to lower values
        else:
            j -= 1
    
    return 0

# Array declaration
arr = [2,3,5,8,9,10,11]

val = 17

print("Pair with the sum equal to {} is: {}".format(val, isPairSum(arr, len(arr), val)))