#data
print('data........')
def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
  
    for j in range(low, high):
  
        if arr[j] <= pivot:
  
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)

        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
  
  

arr = ['W','U','V'] 
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)

# 11111111111111111111111111111111111111111111111

def partition(arr1, low, high):
    i = (low-1)         
    pivot = arr1[high]     
  
    for j in range(low, high):
  
        if arr1[j] <= pivot:
  
            i = i+1
            arr1[i], arr1[j] = arr1[j], arr1[i]
  
    arr1[i+1], arr1[high] = arr1[high], arr1[i+1]
    return (i+1)
  
def quickSort(arr1, low, high):
    if len(arr1) == 1:
        return arr1
    if low < high:

        pi = partition(arr1, low, high)

        quickSort(arr1, low, pi-1)
        quickSort(arr1, pi+1, high)
  
  

arr1 = ['T','S','Q','P','R'] 
n = len(arr1)
quickSort(arr1, 0, n-1)
print(arr1)

#data lain
print ('data lain.............')
def partition(arra, low, high):
    i = (low-1)         
    pivot = arra[high]     
  
    for j in range(low, high):
  
      
        if arra[j] <= pivot:
  
            i = i+1
            arra[i], arra[j] = arra[j], arra[i]
  
    arra[i+1], arra[high] = arra[high], arra[i+1]
    return (i+1)
  

def quickSort(arra, low, high):
    if len(arra) == 1:
        return arra
    if low < high:

        pi = partition(arra, low, high)

        quickSort(arra, low, pi-1)
        quickSort(arra, pi+1, high)
  
  

arra = ['W','U','V'] 
n = len(arra)
quickSort(arra, 0, n-1)
print(arra)
################################
def partition(arrb, low, high):
    i = (low-1)         # index of smaller element
    pivot = arrb[high]     # pivot
  
    for j in range(low, high):
  
        
        if arrb[j] <= pivot:
  
            i = i+1
            arrb[i], arrb[j] = arrb[j], arrb[i]
  
    arrb[i+1], arrb[high] = arrb[high], arrb[i+1]
    return (i+1)
  

def quickSort(arrb, low, high):
    if len(arrb) == 1:
        return arrb
    if low < high:

        pi = partition(arrb, low, high)

        quickSort(arrb, low, pi-1)
        quickSort(arrb, pi+1, high)
  
  

arrb = ['M','L','O','N'] 
n = len(arrb)
quickSort(arrb, 0, n-1)
print(arrb)
############################
def partition(arrc, low, high):
    i = (low-1)        
    pivot = arrc[high]    
  
    for j in range(low, high):
  
   
        if arrc[j] <= pivot:
  

            i = i+1
            arrc[i], arrc[j] = arrc[j], arrc[i]
  
    arrc[i+1], arrc[high] = arrc[high], arrc[i+1]
    return (i+1)
  

def quickSort(arrc, low, high):
    if len(arrc) == 1:
        return arrc
    if low < high:

        pi = partition(arrc, low, high)

        quickSort(arrc, low, pi-1)
        quickSort(arrc, pi+1, high)
  
  

arrc = ['T','S','Q','P','R'] 
n = len(arrc)
quickSort(arrc, 0, n-1)
print(arrc)