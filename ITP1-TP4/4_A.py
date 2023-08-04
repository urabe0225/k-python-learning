a,b = map(int, input().split())
d = a // b # 小数点以下を切り捨てる商を出している
r = a % b # 余りを出している
f = a / b # 小数点を含む商を出している
print(f"{d} {r} {f:.5f}") 