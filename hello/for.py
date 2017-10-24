# Loops List
a = ['cat', 'window', 'defenestrate']
for x in a:
    print x, len(x)

#range（101）：0-100 整数
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)