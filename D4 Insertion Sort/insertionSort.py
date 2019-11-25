import random
def insertionSort():
    numbers = [i for i in range(1, 10001)]
    numbers = random.sample(numbers, len(numbers))

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print(numbers)
    return
insertionSort()
            
