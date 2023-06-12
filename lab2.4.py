lang = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
shag = int(input('Шаг шифровки: '))
sms = input("Сообщение для шифровки: ").upper()
shifr = ''
for i in sms:
    mesto = lang.find(i)
    new_mesto = mesto + shag
    if i in lang:
        shifr += lang[new_mesto]
    else:
        shifr += i
print (shifr)