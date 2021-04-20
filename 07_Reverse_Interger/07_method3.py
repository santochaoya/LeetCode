# ===============================================================================================
# 
# This is the simplified edition of method1. Reverse number style.
# 
# ===============================================================================================

x = int(input ('x = '))

abs_x = abs(x)
result = 0

while abs_x > 0:
    result = result * 10 + abs_x % 10
    abs_x = abs_x // 10

if abs(result) > 2*31-1:
    result = 0
elif x < 0:
    result = -1 * result
    
print("Output: ", result)
