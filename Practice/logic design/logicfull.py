from math import floor
def d_to_n(number, base):
    if not (2 <= base <= 36):
        raise ValueError("Invalid base choosen.")
    digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    integer_part = floor(number)
    floating_part = number - integer_part
    res1 = ""      #Integer_part 
    if integer_part == 0:
        res1 = "0"
    while integer_part > 0:
        dig = digit[integer_part % base]
        res1 = dig + res1
        integer_part //= base
    res2 = ""      #Floating_part
    for i in range(4):
        pdt = floating_part * base
        dig = floor(pdt)
        res2 += digit[dig]
        floating_part = pdt - dig   
    return res1 + "." + res2

number = float(input("enter a real number :"))
tb=int(input("enter target base (2 <=base<=36) :"))
ans = d_to_n(number,tb)
print(ans) 
