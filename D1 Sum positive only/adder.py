def adder():
    num1 = input(" First number: ")
    num2= input("Second number: ")

    carry = 0
    result = "" 

    if len(num1) > len(num2):
        while len(num1) != len(num2):
            num2 = "0" + num2

    if len(num2) > len(num1):
        while len(num1) != len(num2):
            num1 = "0" + num1
        
    while len(num1) > 0:
        temp = int(num1[-1]) + int(num2[-1]) + carry
        carry = 0
        if temp > 9:
            result = str(temp)[1] + result
            carry = int(str(temp)[0])
        num1 = num1[:-1]
        num2 = num2[:-1]
    if carry > 0:
        result = str(carry) + result

    print(result)
    return
adder()
