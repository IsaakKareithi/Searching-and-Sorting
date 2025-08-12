class Data:
    def __init__(self, value, index, count=0):
        self.value= value
        self.index=index
        self.count=count

# Custom sort by element's frequency and index
def SortByFrequencyAndIndex(arr):
    if arr is None or len(arr)< 2:
        return
    
    hm = {}

    #For each array element, insert into the directory its frequency and index of its first occurence in the array
    for i in range(len(arr)):
        hm.setdefault(arr[i], Data(arr[i], i)). count += 1

    #Get values
    values = [*hm.values()]

    # Sort the values based on a custom operator 

    #1. if 2 elements have the same frequency, the one which has the lesser index should come first

    #2. if 2 elements have diffferent frequencies, then the one with greater frequency should come first

    values.sort(key =lambda x:(-x.count, x.index))

    k = 0
    for data in values:
        for j in range(data.count):
            arr[k] = data.value
            k += 1


if __name__ == '__main__':
    arr = [3,3,1,1,1,8,3,6,1,7,8]

    print("Original array: ",arr)
    SortByFrequencyAndIndex(arr)
    print("Sorted array: ",arr)
