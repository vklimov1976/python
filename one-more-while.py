while True:
    text = input("Введите число или команду стоп для выхода: ")
    if text == 'стоп':
        print("Выход из программы! До скорой встречи!")
        break
    elif text == '1':
        print("Число 1")
    else:
        print("Что это?")