#Implement a quick sort

items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19, 51, 123, 5678, 44, 66, 77, 29, 675, 7689, 34, 22, 1, 0, 44]

def quicksort(dataset, first, last):
    if first < last:
        #calculate the split point
        pivotId = partition(dataset, first, last)

        #now sort the two partitions
        quicksort(dataset, first, pivotId-1)
        quicksort(dataset, pivotId + 1,last )


def partition(datavalues, first, last):
    #choose the first item as the pivot value
    pivotvalue = datavalues[first]

    #establish the upper and lower indexes
    lower = first + 1
    upper = last

    #start searching for the crossing point
    done = False
    while not done:
        #TODO advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1 

        #TODO advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        #TODO if the indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp
    
    #when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    #return the split point index
    return upper

print(items)
quicksort(items, 0, len(items)-1)
print(items)