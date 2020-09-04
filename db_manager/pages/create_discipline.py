import tkinter as tk                # python 3
from tkinter import messagebox
from services.mongo_client import MongoClient


class CreateDiscipline(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_label = tk.Label(self, text="Create Discipline", font=controller.title_font)
        title_label.pack(side="top", fill="x", pady=10)

        name_label = tk.Label(self, text="Name")
        name_label.pack()

        name_entry = tk.Entry(self)
        name_entry.pack()

        tk.Label(self).pack()

        area_label = tk.Label(self, text="Area")
        area_label.pack()

        area_entry = tk.Entry(self)
        area_entry.pack()

        tk.Label(self).pack()

        path_label = tk.Label(self, text="Mongo Path")
        path_label.pack()

        path_entry = tk.Entry(self)
        path_entry.pack()

        tk.Label(self).pack()

        button_add = tk.Button(self, text="Create",
                           command=lambda: self.create_discipline(name_entry.get(), area_entry.get(), path_entry.get()))
        button_add.pack()

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

    def create_discipline(self, name: str, area: str, path: str):
        # Connect to DB
        client = MongoClient(path)
        if client.connect():
            messagebox.showinfo("Executed", client.create_discipline(name, area))
            return
        else:
            messagebox.showerror("Error", "Could not connect to the DB")
            return

