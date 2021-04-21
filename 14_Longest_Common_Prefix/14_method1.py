# ===============================================================================================
# 
# Assign the first element to prefix. 
# Compare each element to temp prefix.
# Assign the same character to temp prefix.
# Assign temp prefix to prefix.
#  
# ===============================================================================================


input_str = ["cir","car", "cbr", "ccr"]
if input_str:
    prefix = input_str[0]
else:
    prefix = ""

for i in range(len(input_str)):
    temp_prefix = ""
    for j in range(min(len(input_str[i]), len(prefix))):
        if prefix[j] == input_str[i][j]:
            temp_prefix += (prefix[j])
        else:
            break
    prefix = temp_prefix

print(prefix)

            
