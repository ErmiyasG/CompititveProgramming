def reverseInteger():
    value = input("Enter the integer: ")
    result = ""
    
    if value[0] == '-':
        value = value[1:]
        for i in value:
            result = result + value[-1]
            value = value[:-1]
        result = '-' + result
        print(result)
    else:
        for i in value:
            result = result + value[-1]
            value = value[:-1]
        print(result)
    
reverseInteger()
