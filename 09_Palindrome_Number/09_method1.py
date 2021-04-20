input_number = input()
flag = []

for idx in range(int(len(input_number)/2)+1):

    print(idx)
    print(input_number[idx])
    print(input_number[-idx-1])
  

    if input_number[idx] == input_number[-idx-1]:
        flag.append(1)
    else:
        flag.append(0)
    print(flag)
    print("-------------------")

if sum(flag) == len(flag):
    result = "true"
else:
    result = "false"
    
print(result)