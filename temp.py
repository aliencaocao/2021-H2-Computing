n = int(input('enter n: '))
value = 1
counter = 1
for i in range(1, n, 2):
    value = value + ((-1**counter)/i)
    counter+=1

print(value)