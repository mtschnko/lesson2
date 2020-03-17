while True:
    say = input('Как дела? ')
    if say == 'Хорошо':
        print('Ну и хорошо!')
        break
    else:
        print('Ответ "{}" не подходит, попробуйте еще раз'.format(say))
    print(say)
