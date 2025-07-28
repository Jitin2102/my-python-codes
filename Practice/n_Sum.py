n = int(input("Enter a number: "))
def sum_of_n(n):
    if n < 0:
        return 0
    else:
        return n + sum_of_n(n - 1)

result = sum_of_n(n)
print("The sum of numbers from 1 to", n, "is:", result)