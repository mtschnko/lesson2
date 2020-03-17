dict = {"Какая погода?": "Хорошая!", "Что делаешь?": "Программирую", "Будешь есть?": "Да"}

for key in dict.keys():
  user_say = input('Задай мне вопрос: ')
  while key == user_say:
      print(dict[user_say])
      break
  else:
      print('Не знаю такого вопроса, попробуйте еще раз.')
