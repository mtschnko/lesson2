age = int(input('Введи свой возраст и я скажу чем ты занимаешься:'))

def profession(age):
    if age <= 0:
        return 'Поздравляю, ты только родился!'
    elif 1 <= age <= 6:
        return 'Мама водит в ясли'
    elif 7 <= age <= 16:
        return 'Иногда ходишь в школу'
    elif 7 <= age <= 16:
        return 'Заскакиеваешь в ПТУ'
    elif 17 <= age <= 65:
        return 'Работаешь на не любимой работе'
    else:
        return 'Ух, старичок! Даже не знаю'

print(profession(age))