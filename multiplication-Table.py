print("What number do you want to see its table?")
n = int(input())
numbers = list(range(1, 11))
for i in numbers:
    count = n * i
    print(n, 'x', i, 'is:', count)
