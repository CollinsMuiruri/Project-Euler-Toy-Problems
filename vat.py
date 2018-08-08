
def vat():
    value = int(input("Input raw value for VAT conversion:  "))
    prod = value*0.16
    add = prod+value
    print("VAT is :", prod)
    print("Final conversion is:", add)

vat()
while True:
    vat()