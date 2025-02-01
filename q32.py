'''
Write a program that opens a file dialog that allows you to select a text file.
The program then displays the contents of the file in a textbox.
'''

import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes = [("Text Files","*.txt")])
    if file_path:
        with open(file_path,'r') as file:
            text_box.delete("1.0",tk.END)
            text_box.insert(tk.END,file.read())

root = tk.Tk()
root.title("Text file viewer")
root.geometry("500x400")

tk.Button(root,text ="Select File",command = open_file).pack(pady=10)

text_box = tk.Text(root,wrap ="word")
text_box.pack(padx=20,pady=20,fill=tk.BOTH,expand=True)

root.mainloop()




