from collections import deque

LIST = deque()
num_command = int(input())
for loop in range(num_command):
    input_command = input()
    if input_command == "deleteFirst":
        LIST.popleft()
    elif input_command == "deleteLast":
        LIST.pop();
else:
    com,num = input_command.split()
    
    if com == "insert":
        LIST.appendleft(num)
    elif com == "delete":
        try:
            LIST.remove(num)
        except:
            pass
print(" ". join(LIST))