x = input ('x = ')

abs_x = abs(x)
original_abs_x = str(abs_x)
result = int(original_abs_x[::-1])

if result > 2**31-1:
    result = 0
elif x < 0:
    result = -1 * result

print("Output: ", result)
