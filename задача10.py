x = int(input("чему равен вклад"))
p = int(input("какой процент"))
q = p/100
y = int(input("сколько хочешь денег?"))
v = 0
if y <= x:
    print("у тебя уже столько есть")
else:
    while x <= y:
      x = x + (x*q)
      v = v+1
print(v)
