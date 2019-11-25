def reverseInteger():
    value = input()
    result = ""
    integer = 0
    
    if value[0] == '-':
        value = value[1:]
        for i in value:
            result = result + value[-1]
            value = value[:-1]
        result = '-' + result
        integer = int(result)
        print(integer)
    else:
        for i in value:
            result = result + value[-1]
            value = value[:-1]
            integer = int(result)
        print(integer)
    
reverseInteger()
