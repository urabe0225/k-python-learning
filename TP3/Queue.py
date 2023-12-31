from collections import deque

n,p = map(int, input().split())
que = deque([])

for i in range(n):
    name, time = input().split()
    time = int(time)
    que.append([name,time])

t = 0
while len(que) > 0:
    atop = que.popleft()
    spend = min (atop[1], p)
    atop[1] -= spend
    t += spend
    if(atop[1] == 0):
        print(atop[0],t)
    else:
        que.append(atop)
