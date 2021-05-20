import tkinter as tk
import tkinter.font as fnt


class Ui:

    def __init__(self, start_callback, item_click_callback):

        self.cleared_entry = True
        self.start_callback = start_callback
        self.item_click_callback = item_click_callback

        self.window = tk.Tk()
        frame_left = tk.Frame(master=self.window, background="red")
        frame_left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        frame_right = tk.Frame(master=self.window, background="yellow")
        frame_right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        frame_right_numerical_btns = tk.Frame(master=frame_right, background="yellow")
        frame_right_numerical_btns.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

        for i in range(4):
            for j in range(3):
                numerical_btn_frame = tk.Frame(
                    master=frame_right_numerical_btns,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                numerical_btn_frame.grid(row=i, column=j, padx=5, pady=5)
                if i == 3 and j == 0:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="Wyczyść", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.clear_entry())
                elif i == 3 and j == 2:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="Backspace", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.backspace_entry())
                elif i == 3 and j == 1:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text="0", padx=15, pady=10,
                                              font=fnt.Font(size=10), command=lambda: self.add_number_to_entry("0"))
                else:
                    numerical_btn = tk.Button(master=numerical_btn_frame, text=str(j + 1 + 3 * i), padx=15,
                                              pady=10,
                                              font=fnt.Font(size=10),
                                              command=(lambda x=(j + 1 + 3 * i): self.add_number_to_entry(str(x))))
                numerical_btn.pack()

        numerical_btn_frame = tk.Frame(
            master=frame_right_numerical_btns,
            relief=tk.RAISED,
            borderwidth=1
        )
        numerical_btn_frame.grid(row=0, column=3, padx=5, pady=5)
        weigh_btn = tk.Button(master=numerical_btn_frame, text="Zważ", padx=15, pady=10, font=fnt.Font(size=10))
        weigh_btn.pack()

        self.ent_weigh = tk.Entry(master=frame_right, font=fnt.Font(size=20), text="1")
        self.ent_weigh.place(width=300, height=50, relx=0.5, rely=0.15, anchor=tk.CENTER)
        self.ent_weigh.insert(0, 1)
        self.ent_weigh.configure(state=tk.DISABLED)

        self.next_client_btn = tk.Button(master=frame_left, text="Następny klient", padx=15, pady=10,
                                         font=fnt.Font(size=10),
                                         command=lambda: self.hide_next_client_btn_and_start())
        self.next_client_btn.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

        self.item_btn = tk.Button(master=frame_left, padx=15, pady=10,
                                  font=fnt.Font(size=10),
                                  command=lambda: self.item_click_callback())

    def add_number_to_entry(self, number):
        self.ent_weigh.configure(state=tk.NORMAL)
        if self.cleared_entry:
            self.ent_weigh.delete(0, tk.END)
            self.ent_weigh.insert(0, number)
            self.cleared_entry = False
        else:
            current_text = self.ent_weigh.get()
            self.ent_weigh.delete(0, tk.END)
            self.ent_weigh.insert(0, current_text + number)

        self.ent_weigh.configure(state=tk.DISABLED)

    def clear_entry(self):
        self.ent_weigh.configure(state=tk.NORMAL)
        self.ent_weigh.delete(0, tk.END)
        self.ent_weigh.insert(0, 1)
        self.ent_weigh.configure(state=tk.DISABLED)
        self.cleared_entry = True

    def backspace_entry(self):
        self.ent_weigh.configure(state=tk.NORMAL)
        if len(self.ent_weigh.get()) == 1:
            self.ent_weigh.delete(0, tk.END)
            self.ent_weigh.insert(0, 1)
        else:
            self.ent_weigh.delete(len(self.ent_weigh.get()) - 1, tk.END)
            self.cleared_entry = True

        self.ent_weigh.configure(state=tk.DISABLED)

    def hide_next_client_btn_and_start(self):
        self.next_client_btn.pack_forget()
        self.start_callback()

    def show_item(self, text):
        self.item_btn['text'] = text
        self.item_btn.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)


