#finding pair with sum closest to given value

MAX_VAL = 100000000000

def printClosest(arr, n, x):

    #TO store indexes of pairs
    res_l, res_r = 0,0

    #initialize left and right indexes and 
    #difference btwn sums and x
    l, r, diff = 0, n-1, MAX_VAL

    #While the are elements between l and r 
    while r>l:

        #Check if the pair is closer than the 
        #closest pair so far
        if abs(arr[l]+arr[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l]+arr[r] - x)

        if arr[l] + arr[r] > x:
            #If pair has larger val move to smaller number
            r -= 1

        else:
            #move to larger values
            l += 1

    print("the closest pair to sum {} is {} and {}".format (x, arr[res_l],arr[res_r]))

#driver code to test above
if __name__ == "__main__":
    arr = [10,22,28,29,30,40]
    n = len(arr)
    x = 54
    printClosest(arr,n,x)