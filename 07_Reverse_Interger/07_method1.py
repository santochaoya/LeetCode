# ===============================================================================================
# 
# Given a signed 32-bit integer abs_x, return abs_x with its digits reversed. 
# If reversing abs_x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
# then return 0.
# 
# ===============================================================================================

x = input ('x = ')

abs_x = abs(x)
original_abs_x = str(abs_x)
remain_len = len(original_abs_x)
result = 0

while remain_len > 0:
    digit_ten = len(original_abs_x) - remain_len
    quotient, abs_x = divmod(abs_x, 10 ** (remain_len - 1))
    last_number = 10 ** digit_ten * quotient
    result += last_number
    remain_len -= 1

if abs(result) > 2*31-1:
    result = 0
elif x < 0:
    result = -1 * result
    
print("Output: ", result)
