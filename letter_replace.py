from tkinter import *

replace_letters = {
    "А" : "A", "а" : "a", "В" : "B", "Е" : "E", "е" : "e", "К" : "K", "М" : "M", "Н" : "H",
    "О" : "O", "о" : "o", "Р" : "P", "р" : "p", "С" : "C", "с" : "c", "Т" : "T", "у" : "y", "Х" : "X", "х" : "x"
}

def clear():
   ent.delete(1.0, END)
   lab['text'] = "Поле ввода очищено."

def str_to_sort_list():
    text = ent.get(1.0, END)
    if (text != "" and text != None and text[0] * len(text) != text): 
        for key in replace_letters.keys():
            text = text.replace(key, replace_letters[key])
        lab['text'] = "Текст преобразован и скопирован в буфер обмена."
        text = text[:-1]
        root.clipboard_clear()
        root.clipboard_append(text)
    else:
        lab['text'] = "Вы не ввели текст!"

root = Tk()
root.title("Letter Replacer")
root.geometry("425x440")

lab1 = Label(text="Преобразование русских символов в английские без видимых изменений.", font="Arial 9", width=100, fg="#eee", bg="#333")
ent = Text(root, height=20, width=50)
but = Button(text="Преобразовать", command=str_to_sort_list)
but1 = Button(text="Очистить", command=clear)
lab = Label(text="Введите текст для преобразования!", width=100, bg='black', fg='white')
 
lab1.pack()
ent.pack()
but.pack()
but1.pack()
lab.pack()
root.mainloop()