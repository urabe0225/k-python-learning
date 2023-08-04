while True:
    a, op, b = input().split()
    a = int(a) # aを整数型に変換
    b = int(b) # bを整数型に変換
    if op == "+":
        c = a + b
    elif op == "-":
        c = a - b
    elif op == "*":
        c = a * b
    elif op == "/":
        c = a // b
    else:
        break
    print(c)