def triangle():
    rows = eval(input("Enter the number of rows: "))
    counter = 1
    space = rows -1
    while counter <= rows:
        print(" " * space, "*" * (2*counter - 1))
        counter += 1
        space -= 1
    return

triangle()
