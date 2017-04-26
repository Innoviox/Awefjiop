import numpy as np

import tkinter as tk
root = tk.Tk()
root.title("Dictionary")

languages = ['Awefjiop', 'English-Parentheses']
def isLanguageLine(line):
    return any(l in j for l in languages for j in line)

text = list(filter(bool, open("dict.txt").read().split('\n')))
dictionary = {}
for line in np.ravel(text, order='F').reshape(-1, 2):
    if isLanguageLine(line):
        continue
    dictionary[line[0].lower()] = line[1].strip('()')

def checkWord(*event):
    word = e.get().lower()
    dwl["text"] = dictionary.get(word, {v:k for k,v in dictionary.items()}.get(word, f"{word} is not a word"))
    dwl.pack()
    
l = tk.Label(root, height=2, width=50, text="Type an Awefjiop word below to get it's \nEnglish meaning (or the other way around).")

e = tk.Entry(root)
e.delete(0, tk.END)
e.insert(0, "word")


for i in [l, e]:
    i.pack()

dwl = tk.Label(root)

root.bind("<Return>", checkWord)
root.mainloop()
