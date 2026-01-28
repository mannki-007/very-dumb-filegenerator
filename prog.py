import customtkinter as ctk
from pathlib import Path
import os


# var / переменные
dot = '.'
namefile = 'type file name and ext'
namefilepath = 'type path'


file_path = '' 


# функции / fucntions
def entry_callback():
    text = entry.get()

    button_callback(text)

def entry_path():
    pathfile = entrypath.get()

    button_callback(pathfile)

fullpath = ''
    
def button_callback(text, pathfile):
    fullpath = os.path.join(pathfile, text)
    with open(fullpath, "w") as f:
        f.write("")
        print('file created at: ', fullpath)
        label.configure(text=f'Created at: {fullpath}')






# window parameters
main = ctk.CTk()
main.geometry("400x200")
main.title("File creater by mannki")


# текст / label

label = ctk.CTkLabel(main,text="", fg_color="transparent")
label.pack(padx=20, pady=0)

# поле ввода / entry
entry = ctk.CTkEntry(main, placeholder_text=namefile)
entry.bind("<Return>", lambda event: entry_callback())
entry.pack(padx=20, pady=20)

entrypath = ctk.CTkEntry(main, placeholder_text=namefilepath)
entrypath.bind("<Return>", lambda event: entry_path())
entrypath.pack(padx=20, pady=0)

# кнопка / buttton
button = ctk.CTkButton(main, text="Create file!", command=lambda: button_callback(entry.get(), entrypath.get()))
button.pack(padx=20, pady=20)


main.mainloop()