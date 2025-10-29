import time as t

arr = [12, 6, 3, 9, 4, 1, 2, 13, 7, 15]
start = t.time()

arr = []
def cleanFile():
    file = open("numbers.txt")
    number = file.read().split(",")
    for num in number:
        num = int(num.strip())
        arr.append(num)

def partition(arr, low, high):
    pivot = arr[high]

    i = low -1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    
    swap(arr, i + 1, high)
    return i +1
    
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def quickSort(arr, low, high):
    if low < high:

        pivot = partition(arr, low, high)

        quickSort(arr, low, pivot -1)
        quickSort(arr, pivot +1, high)


cleanFile()
quickSort(arr, 0,  len(arr) -1)
print(arr)
print(t.time()- start)