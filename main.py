import tkinter as tk
from tkinter import ttk
from tkinter import END
from analyzer import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SEO анализ")
        self.geometry("1920x1080")

        self.page1 = tk.Frame(self)

        label1 = tk.Label(self.page1, text="Введите текст")
        label1.pack(pady=10)
        self.input = tk.Text(self.page1, wrap='word', height=15)
        self.input.pack(fill='x')

        button1 = tk.Button(self.page1, text="Проанализировать", command=self.analysis)
        button1.pack(pady=20)
        button1 = tk.Button(self.page1, text="Очистить", command=self.delete)
        button1.pack()

        columns = ("key", "num")
        self.tree = ttk.Treeview(columns=columns, show="headings")
        # определяем заголовки
        self.tree.heading("key", text="Ключевые слова")
        self.tree.heading("num", text="Количество")

        self.page1.pack(fill="both", expand=True)

    def analysis(self):
        try:
            self.label2.pack_forget()
            self.tree.pack_forget()
            for item in self.tree.get_children(""):
                self.tree.delete(item)
        except:
            pass

        text = self.input.get(1.0, END)

        if '\n' in text:
            text = text.replace('\n', ' ')
        
        if text.isspace() or text == '\n':
            self.page1.pack(fill="both", expand=True)
            return
        symbols = count_symbols(text)
        words = count_words(text)
        key_word = key_words(text)
        water_procent = water(text, words)
        spam_procent = spam(words, key_word)

        self.label2 = tk.Label(self.page1, 
        text=f"Количество символов = {str(symbols)}\nКоличество слов = {str(words)}\nВода = {str(round(water_procent, 2))}%\nЗаспамленность = {str(round(spam_procent, 2))}%")
        self.label2.pack(anchor='w')
        
        for word in key_word:
            values = []
            w = word[1][1]
            for i in word[1][2:]:
                w += f", {str(i)}"
            values.append(w)
            values.append(word[1][0])
            values = tuple(values)
            self.tree.insert("", END, values=values)
        self.tree.pack(fill='x')

    def delete(self):
        self.input.delete(1.0, END)
        try:
            self.label2.pack_forget()
        except:
            pass
        self.tree.pack_forget()
        for item in self.tree.get_children(""):
            self.tree.delete(item)

if __name__ == "__main__":
    app = App()
    app.mainloop()
