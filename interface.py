import tkinter as tk
import tkinter.font as fnt


class Ui:

    def __init__(self, *args, **kwargs):

        self.window = tk.Tk()
        frame_left = tk.Frame(master=self.window, background="red")
        frame_left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        frame_right = tk.Frame(master=self.window, background="yellow")
        frame_right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        frame_right_numerical_buttons = tk.Frame(master=frame_right, background="yellow")
        frame_right_numerical_buttons.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

        for i in range(4):
            for j in range(3):
                numerical_button_frame = tk.Frame(
                    master=frame_right_numerical_buttons,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                numerical_button_frame.grid(row=i, column=j, padx=5, pady=5)
                if i == 3 and j == 0:
                    numerical_button = tk.Button(master=numerical_button_frame, text="Wyczyść", padx=15, pady=10,
                                                 font=fnt.Font(size=10), command=lambda: self.clear_entry())
                elif i == 3 and j == 2:
                    numerical_button = tk.Button(master=numerical_button_frame, text="Backspace", padx=15, pady=10,
                                                 font=fnt.Font(size=10), command=lambda: self.backspace_entry())
                elif i == 3 and j == 1:
                    numerical_button = tk.Button(master=numerical_button_frame, text="0", padx=15, pady=10,
                                                 font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("0"))
                else:
                    numerical_button = tk.Button(master=numerical_button_frame, text=str(j + 1 + 3 * i), padx=15,
                                                 pady=10,
                                                 font=fnt.Font(size=10),
                                                 command=(lambda x=(j + 1 + 3 * i): self.add_number_to_entry(str(x))))
                numerical_button.pack()

        numerical_button_frame = tk.Frame(
            master=frame_right_numerical_buttons,
            relief=tk.RAISED,
            borderwidth=1
        )
        numerical_button_frame.grid(row=0, column=3, padx=5, pady=5)
        weigh_button = tk.Button(master=numerical_button_frame, text="Zważ", padx=15, pady=10, font=fnt.Font(size=10))
        weigh_button.pack()

        self.ent_weigh = tk.Entry(master=frame_right, font=fnt.Font(size=20), text="1", state=tk.DISABLED)
        self.ent_weigh.place(width=300, height=50, relx=0.5, rely=0.15, anchor=tk.CENTER)

    def add_number_to_entry(self, number):
        self.ent_weigh.configure(state=tk.NORMAL)
        current_text = self.ent_weigh.get()
        self.ent_weigh.delete(0, tk.END)
        self.ent_weigh.insert(0, current_text + number)
        self.ent_weigh.configure(state=tk.DISABLED)

    def clear_entry(self):
        self.ent_weigh.configure(state=tk.NORMAL)
        self.ent_weigh.delete(0, tk.END)
        self.ent_weigh.configure(state=tk.DISABLED)

    def backspace_entry(self):
        self.ent_weigh.configure(state=tk.NORMAL)
        current_text = self.ent_weigh.get()
        self.ent_weigh.delete(0, tk.END)
        self.ent_weigh.insert(0, current_text[:-1])
        self.ent_weigh.configure(state=tk.DISABLED)
