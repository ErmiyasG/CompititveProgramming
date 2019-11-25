import random
def selectionSort():
    inList = [i for i in range(1, 10001)]
    inList = random.sample(inList, len(inList))
    indexOfMin = 0
    for i in range(len(inList)):
        indexOfMin = i
        for j in range(i+1, len(inList)):
            if inList[j] < inList[indexOfMin]:
                inList[indexOfMin], inList[j] = inList[j], inList[indexOfMin]
        
    print(inList)
    return
selectionSort()
    
