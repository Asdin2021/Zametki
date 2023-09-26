def create_note():
    note = input("Введите текст заметки: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Заметка сохранена.")


def read_notes():
    with open("notes.txt", "r") as file:
        notes = file.readlines()
    for i, note in enumerate(notes):
        print(f"{i + 1}. {note}", end="")
    if not notes:
        print("Заметок нет.")


def edit_note():
    with open("notes.txt", "r") as file:
        notes = file.readlines()
    for i, note in enumerate(notes):
        print(f"{i + 1}. {note}", end="")
    if not notes:
        print("Заметок нет.")
        return
    choice = int(input("Введите номер заметки для редактирования: "))
    if choice < 1 or choice > len(notes):
        print("Неверный номер заметки.")
        return
    new_note = input("Введите новый текст заметки: ")
    notes[choice - 1] = new_note + "\n"
    with open("notes.txt", "w") as file:
        file.writelines(notes)
    print("Заметка отредактирована.")


while True:
    print("\nМеню:")
    print("1. Создать заметку")
    print("2. Просмотреть заметки")
    print("3. Редактировать заметку")
    print("4. Выход")
    choice = input("Выберите действие: ")
    if choice == "1":
        create_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        break
