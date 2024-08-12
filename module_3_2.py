def send_email(massage, recipient, *, sender='university.help@gmail.com'):
    option1 = '@' in str(recipient) and '@' in str(sender)
    if (str(recipient).rfind('.com') != -1 or str(recipient).rfind('.ru') != -1 or
            str(recipient).rfind('.net') != -1):
        option2_1 = True
    else:
        option2_1 = False
    if (str(sender).rfind('.com') != -1 or str(sender).rfind('.ru') != -1 or
            str(sender).rfind('.net') != -1):
        option2_2 = True
    else:
        option2_2 = False
    option2 = option2_1 * option2_2 * option1
    if not option2:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
