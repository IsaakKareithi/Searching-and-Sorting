#Build in function
def compare(n1,n2):

    return str(n1)+ str(n2) > str(n2) + str(n1)

# Selection sort
def largestNumber3(nums):
    for i in range(len(nums),0,-1):
        tmp = 0
        for j in range(i):
            if not compare(nums[j], nums[tmp]):
                tmp = j

        nums[tmp], nums[i-1] =nums[i-1], nums[tmp]

    return str(int("".join(map(str, nums))))

#Driver code
arr = [3,30,34,5,9]
print("Given array: ",arr)
print("Largest possible number: ", largestNumber3(arr))