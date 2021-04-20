# Method 1 : Pop and Push Digits & Check before Overflow

### Performance of Method 1:
```
1032/1032 cases passed (32 ms)
Your runtime beats 68.50 % of python3 submissions
Your memory usage beats 91.02 % of python3 submissions (14.1 MB)
```

# Method 2 : Reverse String

Reverse string by:

```string[::-1]```

### Performance of Method 2:
```
1032/1032 cases passed (28 ms)
Your runtime beats 88.07 % of python3 submissions
Your memory usage beats 46.67 % of python3 submissions (14.3 MB)
```

# Method 3 : Simplified method1

Reverse number by:
```
reversed_num = 0

while original_num > 0:
    reversed_num = reversed_num * 10 + original_num % 10
    original_num = original_num // 10
```

### Performance of Method 2:
```
1032/1032 cases passed (16 ms)
Your runtime beats 99.91 % of python3 submissions
Your memory usage beats 45.65 % of python3 submissions (14.2 MB)
```