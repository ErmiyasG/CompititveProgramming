import random
def efficientRandomization():
    numbers = [i for i in range(1, 10001)]
    random.shuffle(numbers)
    print(numbers)
efficientRandomization()
