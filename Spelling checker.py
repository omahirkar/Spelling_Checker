from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")

def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    corrected_text = str(a.correct())
    spell.config(text="Correct Text is: " + corrected_text)

heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50, 0))

enter_text = Entry(root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()

button = Button(root, text="Check", font=("arial", 20, "bold"), bg="black", fg="white", command=check_spelling)
button.pack()

spell = Label(root, font=("poppins", 20), bg="#dae6f6", fg="#364971")
spell.pack(pady=10)

root.mainloop()
