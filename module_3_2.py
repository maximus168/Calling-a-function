def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f'Невозможно отправить письмо с адреса  {sender} на адрес {recipient}')
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print(f" {message} письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email ('Всё в порядке ', 'Simon@.ru')