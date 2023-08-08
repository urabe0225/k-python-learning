while True:
    H, W = map(int, input().split())
    if W == 0 and H == 0:
        break
    for i in range(0,H):
        for j in range(0,W):
            if(i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                print('#',end='')
            else:
                print('.',end="")
        print()
    print()