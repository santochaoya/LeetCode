# ===============================================================================================
# 
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
# then return 0.
# 
# ===============================================================================================

x = input ('x = ')

original_x = str(x)
remain_len = len(original_x)
result = 0

if abs(x) > 2**31 - 1:
    y = 0
else:
    while remain_len > 0:
        digit_ten = len(original_x) - remain_len
        quotient, x = divmod(x, 10 ** (remain_len - 1))
        last_number = 10 ** digit_ten * quotient
        result += last_number
        remain_len -= 1

print("Output: ", result)