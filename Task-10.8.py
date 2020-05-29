'''
Упражнение 10.8
Дан произвольный текст. Найдите номер первого самого длинного слова в нем.
'''
text = 'one two three four'
maximum = 0
for index, word in enumerate(text.split()):
    if len(word) > maximum:
        i = index
        maximum = len(word)
print(f'Слово длиной {maximum} находится на позиции {i + 1}')

# Еще одно решение через функцию numLongestWord
def nLW(text):
    wlist=text.split(' ')
    llist=list(map(len,wlist))
    return llist.index(max(llist))+1
 
z=nLW("one two three four five six seven")
print(z)