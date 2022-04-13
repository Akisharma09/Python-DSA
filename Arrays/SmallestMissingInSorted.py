'''
Approach 1
for i in range(len(arr)-1):
  if (arr[i+1]- arr[i]) != 1:
    return i+1
'''
def findFirstMissingV2(arr,n):
    for i in range(n-1):
        if (arr[i+1] - arr[i]) != 1:
            print(i)
            return i+1


'''
Approach 2
Modified Binary search:(Array is already sorted)
if 1st element is != index of element return the index as smallest element

if mid element = mid index of array i.e. the elements before the index are in continuous range, thus search in mid+1 to end
else search in start to mid index.
'''

def findFirstMissing(arr, start , end):
    if start>end:
        return end+1
    if start != arr[start]:
        return start
    
    mid = (start+end)//2
    if mid == arr[mid]:
        return findFirstMissing(arr,mid+1,end)
    
    return findFirstMissing(arr,start,mid)

def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 10]
    n = len(arr)
    print("Smallest missing element is",
          findFirstMissing(arr, 0, n-1))

if __name__ == '__main__':
    main()
   
