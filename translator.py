from tkinter import *
from googletrans import Translator

translator = Translator()

def translate_text():
    text = input_text.get("1.0", END)
    translated = translator.translate(text, dest="hi")

    output_text.delete("1.0", END)
    output_text.insert(END, translated.text)

root = Tk()
root.title("Language Translator")

Label(root, text="Enter Text").pack()

input_text = Text(root, height=5, width=40)
input_text.pack()

Button(root, text="Translate", command=translate_text).pack()

output_text = Text(root, height=5, width=40)
output_text.pack()

root.mainloop()