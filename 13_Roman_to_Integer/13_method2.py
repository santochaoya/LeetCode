# ===============================================================================================
# 
# Specify roman characters from leftside is adding, rightside is minus
# 
# ===============================================================================================

roman_num = input()
roman_rule = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

int_num = 0

for i in range(len(roman_num)):
    int_num += roman_rule[roman_num[i]]
    if roman_rule[roman_num[i]] > roman_rule[roman_num[i-1]] and i != 0:
        int_num -= 2 * roman_rule[roman_num[i-1]]

print(int_num)
