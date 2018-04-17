number = 0

for x in range(999,100,-1):
    for y in range(x,100,-1):
        product = x*y
        check = str(x*y)
        
        if check == check[::-1]:
            if product > number:
                number = product

print(number)
