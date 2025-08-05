#Find if there is a pair in A[0...n-1] with given sum
# 
def isPairSum(A, N, X):

    for i in range(N):
        for j in range(N):

            #Equal i and j means same element 
            if (i == j):
                continue

            #Pair exists
            if (A[i] + A[j] == X):
                return [A[i], A[j]]

            # as the array is sorted 
            if (A[i]+A[j] > X):
                break

# No pair found within given sum 
    return 0

#array declaration
arr = [2,3,5,8,9,10,11]

#no to search
val = 17

print("pair with the sum equal to {} is: {}".format(val, isPairSum(arr, len(arr), val)))