# program for selection sort
A = [64,25,12,22,11]

#Traverse through the array
for i in range(len(A)):

    #Find the minimum element in array
    min_id=i
    for j in range(i+1, len(A)):
        if A[min_id] > A[j]:
            min_id = j

    #swap the minimum element with first element
    A[i], A[min_id] = A[min_id], A[i]

#Driver code 
print("Sorted array")
for i in range(len(A)):
    print("%d" %A[i], end=" ")