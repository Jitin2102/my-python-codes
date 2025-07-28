digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def d_to_b(n, base): #decimal to other base
    if not (2 <= base <= 36):
        return -1
    res = ""
    while n > 0:
        res = digits[n % base] + res
        n //= base
    return res or "0"
def b_to_d(num, base):
    if not (2 <= base <= 36):
        return -1 
    num = str(num)
    num = num.upper()
    if any(char not in digits[:base] for char in num):
        raise ValueError(f"Invalid characters in number for base {base}")
    decimal = 0
    length = len(num)
    for i in range(length):
        digit = num[length - 1 - i]
        value = digits.index(digit)
        decimal += value * (base ** i)
    return decimal
def b1_to_b2(num, sb, tb):
    if not (2 <= sb <= 36 and 2 <= tb <= 36):
        return -1
    decimal = b_to_d(num, sb)
    return d_to_b(decimal, tb)
def check_for_shortcut(s, t):
    for i in range(2, 10):  # for small bases 
        if pow(s, i) == t:
            return ("expansion", i)  # s^i = t  pair i digits
        elif pow(t, i) == s:
            return ("reduction", i)  # t^i = s  each digit becomes i digits
    return (None, None)
def apply_shortcut(num, s, t):
    mode,p = check_for_shortcut(s, t)
    num = str(num).upper()
    if mode is None:  #No shortcut
        return b1_to_b2(num, s, t)
    if mode == "expansion":  #making pairs of p digits from base-s and convert to base-t
        rem = len(num) % p
        if rem != 0:
            num = num.zfill(len(num) + (p - rem))
        res = ""
        for i in range(0, len(num), p):
            pair = num[i:i+p]
            res += b1_to_b2(pair, s, t)
        return res
    elif mode == "reduction":  #each base-s digit becomes p digits in base-t
        res = ""
        for ch in num:
            pair = b1_to_b2(ch, s, t)
            res += pair.zfill(p)  #pad to p digits to handle if zeroes
        return res                #kam pad rhe hain pairing karne mein

print(apply_shortcut(11001100, 2, 16))   #(expansion mode)
print(apply_shortcut("CC", 16, 2))         #(reduction mode)
print(apply_shortcut("9C", 16, 5))         #no shortcut
