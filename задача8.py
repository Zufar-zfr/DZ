v = int(input("введите значение скорости"))
t = int(input("введите значение времени"))
s = v*t
if s > 108:
    while(s > 108):
        s=s-109
    print(s)
elif s < 0:
    s = 109 + s
    print(s)
    
else:
    print(s)
