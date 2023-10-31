from tkinter import *
from tkinter import ttk
from methodes import *


class App:
    def __init__(self, window):
        self.window = window
        self.home()
    
        



    def utilisateurs(self):
        for i in self.window.winfo_children():
            i.destroy()

        self.frame = Frame(self.window, width=300, height=300)
        self.frame.pack()
        self.frame_title = ttk.Label(self.frame, text="Gestion d'utilisateurs", font=("Arial", 15))
        self.frame_title.pack()

        


    
    def home(self):
        for i in self.window.winfo_children():
            i.destroy()
        self.frame = Frame(self.window, width=300, height=300)
        self.frame.pack()
        
        self.frame_title = ttk.Label(self.frame, text="Application de gestion d'emploi de temps", font=("Arial", 15))
        self.frame_title.pack(pady=20)

        self.utilisateurs_btn = ttk.Button(self.frame, width=40, text="Gestion d'Utilisateurs", command=self.utilisateurs)
        self.utilisateurs_btn.pack(pady=10)

        self.cours_btn = ttk.Button(self.frame, width=40, text="Gestion de Cours", command=self.cours)
        self.cours_btn.pack(pady=10)

        self.salles_btn = ttk.Button(self.frame, width=40, text="Gestion de Salles", command=self.salles)
        self.salles_btn.pack(pady=10)

        self.emploi_btn = ttk.Button(self.frame, width=40, text="Gestion d'emploi de temps", command=self.emploi)
        self.emploi_btn.pack(pady=10)


    def cours(self):
        for i in self.window.winfo_children():
            i.destroy()
        self.frame = Frame(self.window, width=300, height=300)
        self.frame.pack()
        
        self.frame_title = ttk.Label(self.frame, text="Gestion de Cours", font=("Arial", 15))
        self.frame_title.pack(pady=20)

        self.home_btn = ttk.Button(self.frame, text="Go to Home", command=self.home)
        self.home_btn.pack()


    def salles(self):
        for i in self.window.winfo_children():
            i.destroy()
        self.frame = Frame(self.window, width=300, height=300)
        self.frame.pack()
        
        self.frame_title = ttk.Label(self.frame, text="Gestion de Salles", font=("Arial", 15))
        self.frame_title.pack(pady=20)

        self.home_btn = ttk.Button(self.frame, text="Go to Home", command=self.home)
        self.home_btn.pack()


    def emploi(self):
        for i in self.window.winfo_children():
            i.destroy()
        self.frame = Frame(self.window, width=300, height=300)
        self.frame.pack()
        
        self.frame_title = ttk.Label(self.frame, text="Gestion d'emploi de temps", font=("Arial", 15))
        self.frame_title.pack(pady=20)

        self.home_btn = ttk.Button(self.frame, text="Go to Home", command=self.home)
        self.home_btn.pack()




window = Tk()
window.title("Application de gestion d'emploi de temps")
window.config(bg="#eee")
window.geometry("700x450")
window.maxsize(700, 450)
window.minsize(700, 450)
App(window)
window.mainloop()