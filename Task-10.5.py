# Упражнение 10.5
# Дано число, введенное с клавиатуры. Определите сумму квадратов нечетных цифр в
# числе.
s = input("\nВведите любое число, а я найду сумму нечетных цифр в нем: ")
t = 0
for i in range(len(s)):
    if s[i].isdigit(): 
        if int(s[i]) % 2 !=0:
            t += int(s[i]) ** 2
    else:
        print(s[i],"- Не цифра!")
print("Сумма квадратов нечетных чисел в числе:", s, "=", t)