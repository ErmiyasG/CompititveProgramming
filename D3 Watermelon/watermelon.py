def dividerInToEven():
    weight = eval(input())
    if weight < 1 or weight > 100:
        Print("NO")
        return
    if weight == 2:
        print("NO")
        return
    if weight % 2 != 0:
        print("NO")
        return
    else:
        print("YES")
        return
dividerInToEven()
