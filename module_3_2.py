def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка на валидные адреса
    valid_domains = (".com", ".ru", ".net")
    
    if ("@" not in recipient or not recipient.endswith(valid_domains)) or \
       ("@" not in sender or not sender.endswith(valid_domains)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

