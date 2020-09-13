import tkinter as tk                # python 3
from tkinter.scrolledtext import ScrolledText
from services.mongo_client import MongoClient
from tkinter import messagebox


class CreateTrick(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_label = tk.Label(self, text="Create Trick", font=controller.title_font)
        title_label.pack(side="top", fill="x", pady=10)

        name_label = tk.Label(self, text="Name")
        name_label.pack()

        name_entry = tk.Entry(self)
        name_entry.pack()

        tk.Label(self).pack()

        discipline_label = tk.Label(self, text="Discipline")
        discipline_label.pack()

        discipline_entry = tk.Entry(self)
        discipline_entry.pack()

        tk.Label(self).pack()

        video_label = tk.Label(self, text="Video URL")
        video_label.pack()

        video_entry = ScrolledText(self, width=50, height=5)
        video_entry.pack()

        tk.Label(self).pack()

        path_label = tk.Label(self, text="Mongo Path")
        path_label.pack()

        path_entry = tk.Entry(self)
        path_entry.pack()

        tk.Label(self).pack()

        button_add = tk.Button(self, text="Create",
                               command=lambda: self.create_trick(
                                   name=name_entry.get(),
                                   discipline=discipline_entry.get(),
                                   videos=video_entry.get('1.0', 'end-1c'),
                                   path=path_entry.get()
                               ))
        button_add.pack()

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

    def create_trick(self, name: str, discipline: str, videos: str, path: str):
        # Connect to DB
        client = MongoClient(path)
        if client.connect():
            messagebox.showinfo("Executed", client.create_trick(name, discipline, videos.split()))
            return
        else:
            messagebox.showerror("Error", "Could not connect to the DB")
            return
