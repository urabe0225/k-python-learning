st = []
for c in input().split():
    if c in "+-*":
        v2 = st.pop()
        v1 = st.pop()
        st.append(str(eval(v1 + c + v2)))
    else:
        st.append(c)
    
print(st[0])
