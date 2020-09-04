import tkinter as tk                # python 3


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="TrickBase: DB Manager", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        button1 = tk.Button(self, text="Create discipline",
                            command=lambda: controller.show_frame("CreateDiscipline"))
        button2 = tk.Button(self, text="Create trick",
                            command=lambda: controller.show_frame("CreateTrick"))
        button3 = tk.Button(self, text="Modify discipline",
                            command=lambda: controller.show_frame("ModifyDiscipline"))
        button4 = tk.Button(self, text="Modify trick",
                            command=lambda: controller.show_frame("ModifyTrick"))
        button5 = tk.Button(self, text="Delete discipline",
                            command=lambda: controller.show_frame("DeleteDiscipline"))
        button6 = tk.Button(self, text="Delete trick",
                            command=lambda: controller.show_frame("DeleteTrick"))

        button1.pack()
        tk.Label(self).pack()
        button2.pack()
        tk.Label(self).pack()
        button3.pack()
        tk.Label(self).pack()
        button4.pack()
        tk.Label(self).pack()
        button5.pack()
        tk.Label(self).pack()
        button6.pack()
        tk.Label(self).pack()
