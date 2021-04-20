# ===============================================================================================
# 
# Simplified method1
# 
# ===============================================================================================


input_num = int(input())

# Identify rules from number correspond to roman characters
num_rule = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
roman_rule = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

i = 0
roman_num = ''

while input_num > 0:
    roman_num += (input_num // num_rule[i]) * roman_rule[i]
    input_num %= num_rule[i]
    i += 1

print(roman_num)