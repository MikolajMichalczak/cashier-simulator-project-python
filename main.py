import interface


def main():
    ui = interface.Ui()
    window = ui.window
    window.geometry('1000x500')
    window.resizable(False, False)
    window.title("Symulator kasjera")
    window.mainloop()



main()
