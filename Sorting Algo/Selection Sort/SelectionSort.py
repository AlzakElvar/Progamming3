import math
import time as t

file = open("numbers.txt")
file = file.read()
text = file.split(",")
f_text = []

for number in text:
    number = int(number.strip())
    f_text.append(number)

def main(list):
    start = t.time()   
    f_list = []
    j = 0
    index = 0
    for i in range(len(list)):    #Once for every entry 
        min = math.inf
        while j < len(list):      #Loop through the array and grab the smallest
            if list[j] < min:     #Grabbing the smallest
                min = list[j]
                index = j
            j += 1
        list[i], list[index] = list[index], list[i]
        j = i + 1

    return t.time() - start



print(main(f_text))