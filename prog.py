import customtkinter as ctk

# функции

dot = '.'
namefile = 'filesmthng'

def entry_callback():
    text = entry.get()

    button_callback(text)


    
def button_callback(text):
    with open(text, "w") as f:
        f.write("")



app = ctk.CTk()
app.geometry("400x150")


# поле ввода
entry = ctk.CTkEntry(app, placeholder_text=namefile)
entry.bind("<Return>", lambda event: entry_callback())
entry.pack(padx=20, pady=20)

# кнопка
button = ctk.CTkButton(app, text="my button", command=lambda: button_callback(entry.get()))
button.pack(padx=20, pady=20)


app.mainloop()