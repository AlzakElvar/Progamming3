import time as t
import random as r
import math

"""
psudeo code moment


sort partiton(minIndex, maxIndex, array):
    choose pivot
    ran.range(0 len-o-array)
    
    Index = 0
    IIndex = len-o-array -1

    ifl():
        for i in maxIndex:
            if array[i + minIndex] is bigger then pivot
                return i + minIndex
    
    ifr():
        for i in array
            j = len-o-array - (i + 1)
            if array[j] is smaller than pivot:
                return j

    while PENIS:
        if ifl > ifr:
            swap array[ifl] with pivot
            return
        else:
            swap array[ifl] with array[ifr]

    PIVOT ESTABLISHED

    partition at pivot

    if maxIndex - minIndex <= 1:
        reutrn array

"""

def swap(thin1, thin2):
    print(0)
    (thin1, thin2) = (thin2, thin1)


def sortPart(part):
    pivot = r.randrange(0, len(part))
    p_item = part[pivot]
    part.pop(pivot)
    
    ifl = 0
    ifr = 1
    while True:
        
        for i in range(len(part)):
#            print(i)
            if part[i] > p_item:
                ifl = i
                break
            else:
                ifl = len(part)
        
        for i in range(len(part)):
            if part[len(part) - i -1] < p_item:
                ifr = len(part) - i - 1
                break
            else:
                ifr = 0

#        print(f"swap {part[ifl]} with {part[ifr]}")
        if ifl < ifr:
            (part[ifl], part[ifr]) = (part[ifr], part[ifl])
        else:
            break

    part.append(p_item)
#    print(p_item)
    (part[ifl], part[len(part) -1]) = (part[len(part) -1] , part[ifl])          #PIVOT? YIPPIE!!!

    partA = part[0:ifl]
    partB = part[ifl: len(part)]

    # print(partA)
    # print(partB)
    
    if type(partA) == None:
        return partB
    elif type(partB) == None:
        return partA

#    t.sleep(.5)

    nA = []

    if len(partA) < 2:
        print(f"{len(partA)} and {len(partB)}")
        
        if len(partB) < 2:
            nA.append(partA.append(partB))
            return nA
        else:
            nA.append(partA.append(sortPart(partB)))
            return partA.append(sortPart(partB))
    else:
        print(f"{len(partA)} and {len(partB)}")        
        
        if len(partB) <2:
            nA.append(sortPart(partA)).append(partB)
            return nA
        else:
            nA.append(sortPart(partA)).append(sortPart(partB))
            return nA

    
    


print(sortPart([4, 5, 2, 3, 1, 0]))
