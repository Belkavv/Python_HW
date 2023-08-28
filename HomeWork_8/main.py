import json

phone_book = {}

def Save():
    with open("contact.json", "w", encoding="utf-8") as pb:
        pb.write(json.dumps(phone_book, ensure_ascii=False))
    print("Контакт сохранен")

def Load():
    with open("contact.json", "r", encoding="utf-8") as pb:
        phone_book = json.load(pb)
    return phone_book

try:
    with open("contact.json", "r", encoding="utf-8") as pb:
        phone_book = json.load(pb)
except:
    phone_book = {}

while True:
    command = input("Введите команду: ")

    if command == "/add":
        name = input("Введите имя нового контакта: ")
        number0 = input("Введите первый номер телефона: ")
        number1 = input("Введите второй номер телефона: ")
        birth_day = input("Введите ДР: ")
        mail = input("Введите email: ")
        phone_book[name] = {"phone_numbers": [number0, number1], "birth_day": birth_day, "email": mail}
        print("Контакт добавлен")
        Save()
    elif command == "/all":
        print(f"Ткущий список контактов: \n{phone_book}")
    elif command == '/find':
        name = input("Введите имя для поиска: ")
        for name in phone_book:
            print(name, phone_book[name])
    elif command == "/save":
        Save()
    elif command == "/load":
        phone_book = Load()
        print("Загрузка контактов успешно выполнена!")
    elif command == "/del":
        contact = input("Введите имя контакта, который надо удалить: ")
        try:
            del phone_book[contact]
            print("Контакт успешно удален!")
        except:
            print("Такого контакта нет!")