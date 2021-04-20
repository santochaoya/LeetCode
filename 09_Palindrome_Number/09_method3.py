# ===============================================================================================
# 
# Compare the reverse number to the original number
# 
# ===============================================================================================

input_number = int(input())
ori_number = input_number
result_number = 0

while ori_number > 0:
    result_number = result_number * 10 + ori_number % 10
    ori_number = ori_number // 10
    print(result_number)
    print(ori_number)

if result_number == input_number or input_number == 0:
    result = "True"
else:
    result = "False"
    
print(result)