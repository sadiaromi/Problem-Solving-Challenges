# Using String Conversion
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

print(sum_of_digits(32541))

# Using Modulus(%) and Division (//)
def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits


print(sum_of_digits(32541))
