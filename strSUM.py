s = 'aaaa3bBBc6cc'
total = 0
for i in range(len(s)):
    if s[i].isalpha():
        continue
    total += int(s[i])
print("Сумма чисел:", total)