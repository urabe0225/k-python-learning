a,b,c = map(int, input().split())
ans = 0
for i in range(a,b+1): # aからbまでの全ての整数に対して反復
    if c%i == 0: # cをiで割った際の余りが0の場合約数
        ans = ans + 1
print(ans)