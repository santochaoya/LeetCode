roman_num = input()

# Identify rules from number correspond to roman characters
roman_rule = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

int_num = 0
roman_counter = {}

for i in roman_rule:
    roman_counter[i]=roman_num.count(i)

print(roman_counter)

thousands = 1000 * (roman_counter['M'] - roman_counter['CM'])
hunderds = 900 * roman_counter['CM'] + 400 * roman_counter['CD'] + 500 * (roman_counter['D'] - roman_counter['CD']) + 100 * (roman_counter['C'] - roman_counter['XC'] - roman_counter['CM'] - roman_counter['CD'])
tens = 90 * roman_counter['XC'] + 50 * (roman_counter['L'] - roman_counter['XL']) + 40 * roman_counter['XL'] + 10 * (roman_counter['X'] - roman_counter['IX'] - roman_counter['XC'] - roman_counter['XL'])
digits = 9 * roman_counter['IX'] + 5 * (roman_counter['V'] - roman_counter['IV']) + 4 * roman_counter['IV'] + roman_counter['I'] - roman_counter['IV'] - roman_counter['IX']

int_num = thousands + hunderds + tens + digits

print(int_num)