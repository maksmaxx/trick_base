import tkinter as tk                # python 3
from services.mongo_client import MongoClient
from tkinter import messagebox


class DeleteTrick(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_label = tk.Label(self, text="Delete Trick", font=controller.title_font)
        title_label.pack(side="top", fill="x", pady=10)

        uuid_label = tk.Label(self, text="Trick's UUID")
        uuid_label.pack()

        uuid_entry = tk.Entry(self)
        uuid_entry.pack()

        tk.Label(self).pack()

        path_label = tk.Label(self, text="Mongo Path")
        path_label.pack()

        path_entry = tk.Entry(self)
        path_entry.pack()

        tk.Label(self).pack()

        button_delete = tk.Button(self, text="Delete",
                               command=lambda: self.delete_trick(
                                   uuid=uuid_entry.get(),
                                   path=path_entry.get()

                               ))
        button_delete.pack()

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

    def delete_trick(self, uuid: str, path: str):
        # Connect to DB
        client = MongoClient(path)
        if client.connect():
            messagebox.showinfo("Executed", client.delete_trick(uuid))
            return
        else:
            messagebox.showerror("Error", "Could not connect to the DB")
            return
