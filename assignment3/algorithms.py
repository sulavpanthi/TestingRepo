# 1. bubble sort

list1 = [1,7,2,2,99,9,66,88,77,33,1,22,32,3,5,2,3,4]

for a in range(len(list1)):
  for i in range(len(list1)-a-1):
    if list1[i]>list1[i+1]:
      list1[i], list1[i+1] = list1[i+1], list1[i]

for i in list1:
  print(i)




# 2. Insertion sort



def insertion_sort(seq):
   for i in range(1, len(seq)):
      key = seq[i]
      j = i-1
      while j >=0 and key < seq[j] :
         seq[j+1] = seq[j]
         j -= 1
      seq[j+1] = key

seq = [2,1,99,22,34,12,56,31,3,4,9,5]
insertion_sort(seq)
print ("The sorted array result is:")
for i in range(len(seq)):
   print (seq[i])



# 3. Quick sort


def partition_func(arr,low,high):
   i = low-1 
   pivot = arr[high]
   for j in range(low , high):
      if arr[j] <= pivot:
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return i+1 

def quickSort(arr,low,high):
   if low < high:
      pi = partition_func(arr,low,high)
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)

arr = [1,3,2,4,99,22,33,12,13,77,55,98,43,40]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array result is:")
for i in range(n):
   print (arr[i],end=" ")




# 4. Merge sort


def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    i = 0     
    j = 0      
    k = l     
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
   
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
 
def merge_sort(arr,l,r): 
    if l < r:  
        m = (l+(r-1))//2
   
        merge_sort(arr, l, m) 
        merge_sort(arr, m+1, r) 
        merge(arr, l, m, r) 
  
arr = [12, 11, 13, 5, 6, 7] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
merge_sort(arr,0,n-1) 
print ("\n\nSorted array is") 
for i in range(n): 
    print ("%d" %arr[i]),




# 5. Linear search


def linear_search(arr, val):
  count = 0
  for item in arr:
    if item == val:
      return arr.index(item)
    else:
      count += 1
  if count == len(arr):
    return 'Not found anywhere in the list'


idx = linear_search([1,2,3,4,5,6,9,22,11], 9)
print(idx)



# 6. Binary search



def binary_search(seq, item):
  global l,r
  if len(seq[l:r+1]) >= 1:
    if item == seq[(l+r) // 2]:
      return (l+r)//2
    elif item > seq[(l+r)//2]:
      l = (l+r)//2 + 1
      r = r
      return binary_search(seq, item)
    elif item < seq[(l+r) // 2]:
      l = l
      r = (l+r)//2 - 1
      return binary_search(seq, item)
    else:
      return None
  else:
    if item == seq[(l+r) // 2]:
      return l
    else:
      return -1


seq = [1,2,4,5,7,8,9,22,33]
l=0
r=len(seq)
mid = (l+r)//2

res = binary_search(seq, 9)
print(res)




# 7. Interpolation search



def interpolation_search(arr, n, x): 
    lo = 0
    hi = (n - 1) 
   
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return lo; 
            return -1; 
          
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
  
        if arr[pos] == x: 
            return pos 
   
        if arr[pos] < x: 
            lo = pos + 1; 
   
        else: 
            hi = pos - 1; 
      
    return -1
  
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 
n = len(arr) 
  
x = 14 
index = interpolation_search(arr, n, x) 
  
if index != -1: 
    print ("Element found at index",index)
else: 
    print ("Sorry! element is not found in the array.")
  


# 8. Tower of Hanoi



def tower_hanoi(n , from_rod, to_rod, aux_rod):
   if n == 1:
      print ("Move disk 1 from rod",from_rod,"to rod",to_rod)
      return
   tower_hanoi(n-1, from_rod, aux_rod, to_rod)
   print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
   tower_hanoi(n-1, aux_rod, to_rod, from_rod)

n = 3
tower_hanoi(n, 'A', 'C', 'B')








  