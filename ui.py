import tkinter as tk
import tkinter.font as fnt

def createUI(window):

    frameLeft = tk.Frame(master=window, background="red")
    frameLeft.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    label = tk.Label(master=frameLeft, text="xdddd")
    label.pack()

    frameRight = tk.Frame(master=window, background="yellow")
    frameRight.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    label2 = tk.Label(master=frameRight, text="xdddd")
    label2.pack()

    frameRightNumericalButtons = tk.Frame(master=frameRight, background="yellow")
    frameRightNumericalButtons.pack(side=tk.BOTTOM, expand=True, fill=tk.NONE)

    for i in range(4):
        for j in range(3):
            numericalButtonFrame = tk.Frame(
                master=frameRightNumericalButtons,
                relief=tk.RAISED,
                borderwidth=1
            )
            numericalButtonFrame.grid(row=i, column=j, padx=5, pady=5)
            if i == 3 and j == 0:
                numericalButton = tk.Button(master=numericalButtonFrame, text="Wyczyść", padx=15, pady=10, font = fnt.Font(size = 10))
            elif i == 3 and j == 2:
                numericalButton = tk.Button(master=numericalButtonFrame, text="Backspace", padx=15, pady=10, font = fnt.Font(size = 10))
            elif i == 3 and j == 1:
                numericalButton = tk.Button(master=numericalButtonFrame, text=0, padx=15, pady=10, font = fnt.Font(size = 10))
            else:
                numericalButton = tk.Button(master=numericalButtonFrame, text=j + 1 + 3 * i, padx=15, pady=10, font = fnt.Font(size = 10))
            numericalButton.pack()

