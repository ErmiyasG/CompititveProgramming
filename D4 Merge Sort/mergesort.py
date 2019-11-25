import random
inList = [i for i in range(1, 10001)]
inList = random.sample(inList, len(inList))
def mergeSort(inList):
    if len(inList) > 1:
        midValue = len(inList) // 2
        half1 = inList[:midValue]
        half2 = inList[midValue:]
        mergeSort(half1)
        mergeSort(half2)

        i = j = k = 0
        while i < len(half1) and j < len(half2): 
            if half1[i] < half2[j]: 
                inList[k] = half1[i] 
                i+=1
            else: 
                inList[k] = half2[j] 
                j+=1
            k+=1

        while i < len(half1): 
            inList[k] = half1[i] 
            i+=1
            k+=1
          
        while j < len(half2): 
            inList[k] = half2[j] 
            j+=1
            k+=1
mergeSort(inList)
print(inList)
