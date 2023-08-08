while True:
    H, W = map(int, input().split()) # 高さと幅を入力
    if H == 0 and W == 0: # 高さと幅が共に0の場合は終了
        break
    for i in range(0,H):
        for j in range(0,W):
            if i == 0 or i == H-1 or j == 0 or  j == W-1: # 高さと幅のどちらかが0か最大値の場合
                print('#', end = '')
            else:
                print('.' ,end = '')
        print()
    print()