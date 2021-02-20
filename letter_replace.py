from tkinter import Tk

replace_letters = {
    "А" : "A", "а" : "a", "В" : "B", "Е" : "E", "е" : "e", "К" : "K", "М" : "M", "Н" : "H",
    "О" : "O", "о" : "o", "Р" : "P", "р" : "p", "С" : "C", "с" : "c", "Т" : "T", "у" : "y", "Х" : "X", "х" : "x"
}

def copy(text):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)

def letter_replace(text: str):
    for key in replace_letters.keys():
        text = text.replace(key, replace_letters[key])

    copy(text)
    letter_replace(input("\n##Введите текст, который хотите отредактировать.##\n"))

print("\nПриветствую вас в утилите Letter-Replace, введенный вами текст сразу преобразуется и добавиться в ваш буфер обмена.")
letter_replace(input("\n##Введите текст, который хотите отредактировать.##\n"))
