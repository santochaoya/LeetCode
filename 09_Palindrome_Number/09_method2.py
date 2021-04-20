# ===============================================================================================
# 
# Compare the reverse string to the original string
# 
# ===============================================================================================


input_number = input()
reversed_number = input_number[::-1]

if reversed_number == input_number:
    result = "true"
else:
    result = "false"
    
print(result)