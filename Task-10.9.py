# Упражнение 10.9
# Дан произвольный текст. Напечатайте все имеющиеся в нем цифры, определите их
# количество, сумму и найти максимальное.
text = "1 hello 4 kite 9 bite 7 shit 3"
ls = []
for i in text:
    if i in '1234567890':
        ls.append(int(i))
print("\n=========================================================")
print("\nМассив TEXT содержит следующие цифры: ",ls)
print("\n-----------------------------------------------------------")
print("\nМассив TEXT содержит -",len(ls), "цифр.")
print("\n-----------------------------------------------------------")
print("\nСумма цифр в массиве TEXT =",sum(ls))
print("\n-----------------------------------------------------------")
print("\nМаксимальная цифра в массиве TEXT: ",max(ls), "\n")
print("\n=========================================================")