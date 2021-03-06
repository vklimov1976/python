'''
Инструкции циклов могут иметь ветвь else. Она исполняется, когда цикл выполнил
перебор до конца (в случае for) или когда условие становится ложным (в случае while),
но не в тех случаях, когда цикл прерывается по break.
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "равно", x, "*", n // x)
            break
        else:
            # Циклу не удалось найти множитель.
            print(n, "- простое число.")