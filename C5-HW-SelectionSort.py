A = int(input("Enter number of elements: "))

#traverse the array
for i in range(len(A)):
    #find min element in array
    min_id = i
    for j in range(i+1,len(A)):
        if A[min_id] > A[j]:
            min_id = j

    #Swap the min array 
    A[i],