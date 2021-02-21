from tkinter import *

replace_letters = {
    "А" : "A", "а" : "a", "В" : "B", "Е" : "E", "е" : "e", "К" : "K", "М" : "M", "Н" : "H",
    "О" : "O", "о" : "o", "Р" : "P", "р" : "p", "С" : "C", "с" : "c", "Т" : "T", "у" : "y", "Х" : "X", "х" : "x"
}

def clear():
   enter_text.delete(1.0, END)
   label_second['text'] = "Поле ввода очищено."

def letter_replace():
    text = enter_text.get(1.0, END)

    if (text != "" and text != None and text[0] * len(text) != text): 
        for key in replace_letters.keys():
            text = text.replace(key, replace_letters[key])

        label_second['text'] = "Текст преобразован и скопирован в буфер обмена."
        root.clipboard_clear()
        root.clipboard_append(text[:-1])
    else:
        label_second['text'] = "Вы не ввели текст!"

#====TK INIT====
root = Tk()
root.title("Letter Replacer")
root.geometry("425x440")
#===============

#====up label====
first_label = Label(text="Преобразование русских символов в английские без видимых изменений.", font="Arial 9", width=100, fg="#eee", bg="#333")
#================

#====enter text====
enter_text = Text(root, height=20, width=50)
#==================

#====buttons====
edit_button = Button(text="Преобразовать", command=letter_replace)
clear_button = Button(text="Очистить", command=clear)
#===============

#====down label====
label_second = Label(text="Введите текст для преобразования!", width=100, bg='black', fg='white')
#==================

#====Start Gui====
first_label.pack(); enter_text.pack(); edit_button.pack(); clear_button.pack(); label_second.pack()
root.mainloop()