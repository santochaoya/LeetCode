# ===============================================================================================
# 
# A very original and brute force method:
#   * get number of each digit
#   * convert to roman characters with specific rules
# 
# ===============================================================================================


input_num = int(input())

thousand_number = input_num // 1000
hunderd_number = (input_num // 100) % 10
ten_number = (input_num // 10) % 10
digit_number = input_num % 10

print(
    "thousands: {}\nhunderds: {}\nhunderds: {}\ndigits: {}"
    .format(thousand_number, hunderd_number, ten_number, digit_number)
)

print(" ------------------------- ")

# thousands
thousands = thousand_number * 'M'
print("Roman thondsands: {}".format(thousands))
print(" ------------------------- ")

# hunderds
if hunderd_number == 9:
    hunderds = 'CM'
elif hunderd_number == 5:
    hunderds = 'D'
elif hunderd_number == 4:
    hunderds = 'CD'
elif hunderd_number > 5:
    hunderds = 'D' + hunderd_number % 5 * 'C'
else:
    hunderds = hunderd_number % 5 * 'C'
print("Roman hunderds: {}".format(hunderds))
print(" ------------------------- ")

# tens
if ten_number == 9:
    tens = 'XC'
elif ten_number == 5:
    tens = 'L'
elif ten_number == 4:
    tens = 'XL'
elif ten_number > 5:
    tens = 'L' + ten_number % 5 * 'X'
else:
    tens = ten_number % 5 * 'X'
print("Roman tens: {}".format(tens))
print(" ------------------------- ")

# digits
if digit_number == 9:
    digits = 'IX'
elif digit_number == 5:
    digits = 'V'
elif digit_number == 4:
    digits = 'IV'
elif digit_number > 5:
    digits = 'V' + digit_number % 5 * 'I'
else:
    digits = digit_number % 5 * 'I'
print("Roman digits: {}".format(digits))
print(" ------------------------- ")

result_roman = thousands + hunderds + tens + digits

print(result_roman)