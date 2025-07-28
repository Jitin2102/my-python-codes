digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def d_to_b(n, base):
    if not (2 <= base <= 36):
        return "Base must be between 2 and 36"
    result = ""

    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n = n // base

    return result or "0"
def b_to_d(num, base):
    if not (2 <= base <= 36):
        return "Base must be between 2 and 36"
    
    num_str = str(num)
    num_str = num_str.upper()
    if any(char not in digits[:base] for char in num_str):
        raise ValueError(f"Invalid characters in number for base {base}")
    decimal = 0
    length = len(num_str)
    for i in range(length):
        digit = num_str[length - 1 - i]
        value = digits.index(digit)
        decimal += value * (base ** i)

    return decimal
def b1_to_b2(num, sb, tb):
    if not (2 <= sb <= 36 and 2 <= tb <= 36):
        return "Bases must be between 2 and 36"
    decimal = b_to_d(num, sb)       
    return d_to_b(decimal, tb)

def check_for_shortcut(s,t):
    if t < s:
        for i in range(2,s):
            if pow(s,i) == t:
               return i
        print("No shortcut found")   
    elif s < t:
        for i in range(2,t):
            if pow(t,i) == s:
                return i 
        print("No shortcut found")       
    else:
        return None
    
def apply_shortcut(num,s,t):
    p=check_for_shortcut(s,t)
    num_str = str(num)
    i = len(num_str)
    
    if p is not None:
        if t > s:
            res=""
            j= p
            while(i >=0 and j <= len(num_str)):
                
                if num_str[i] == num_str[j]:
                   pair = num_str[-j:i]
                   res= b1_to_b2(pair, s, t) + res
                   i-=p
                   j+=p
            return res

def check_for_shortcut1(num, base):
    if not (2 <= base <= 36):
        return "Base must be between 2 and 36"
    num_str = str(num).upper()
    if num_str == "0":
        return "0"
    if num_str == "1":
        return "1"
    if num_str == digits[base - 1]:
        return digits[base - 1] + " in base " + str(base)
    return None
    

