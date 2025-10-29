import time as t
import numpy as n

numbers = []
def cleanFile():
    file = open("numbers.txt")
    number = file.read().split(",")
    for num in number:
        num = int(num.strip())
        numbers.append(num)

def compare(arrA, arrB):
    f_array = []
    a_index = 0
    b_index = 0
    while True:
        if a_index != len(arrA):

            if b_index != len(arrB):
                
                if arrA[a_index] < arrB[b_index]:
                    f_array.append(arrA[a_index])
                    a_index += 1
                else:
                    f_array.append(arrB[b_index])
                    b_index += 1
            
            else:
                f_array.append(arrA[a_index])
                a_index += 1
        
        elif b_index != len(arrB):
            f_array.append(arrB[b_index])
            b_index += 1

        else:
            return f_array

def mergeSort(arr): 
    t_arr = n.array_split(arr, 2)
    arrA = t_arr[0]
    arrB = t_arr[1]

    #Split input into two
    if len(arrA) > 1:
        return compare(mergeSort(arrA), mergeSort(arrB))
        
    else:
        return compare(arrA, arrB)
    

s_time = t.time()
cleanFile()
print(mergeSort(numbers))
print(t.time() - s_time)