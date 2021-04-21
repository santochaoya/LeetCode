# ===============================================================================================
# 
# Find the shortest element, assign it to prefix. Using min(list, key=len).
# Using build-in function startwith to check prefix with each element.
# Cut one character of prefix each time when prefix is not common.
#  
# ===============================================================================================


input_str = ["cir","car", "cbr", "ccr"]

if input_str:
    prefix = min(input_str, key=len)
else:
    prefix = ""
    
while prefix:
    for char in input_str:
        if not char.startswith(prefix):
            prefix = prefix[:-1]
            break
    else:
        break
    

print(prefix)

            
