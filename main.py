import interface
from datetime import datetime
import random

item_names = ["Marchewka", "Arbuz", "Chleb", "Makaron", "Dorsz", "Ananas", "Banan", "Ziemniak", "Cukinia", "Pomidor",
              "Jabłko", "Cytryna", "Czekolada",
              "Mango", "Gruszka", "Kapusta", "Kiwi", "Groch", "Granat", "Tuńczyk"]
items_list = []
items_counter = 0
start_time = datetime.now()
items_size = 0
global current_item_index
global ui
global current_item_type
global current_item


class Towar:

    def __init__(self):
        self.append_time = datetime.now()
        self.validate_time = datetime.now()
        self.name = random.choice(item_names)


class TowarNaSztuki(Towar):

    def __init__(self):
        super().__init__()
        self.quantity = self.getQuantity()

    @staticmethod
    def getQuantity():
        is_more_than_one = random.choice([True, False])
        return random.randint(2, 50) if is_more_than_one else 1


class TowarNaWage(Towar):

    def __init__(self):
        super().__init__()
        self.weight = round(random.uniform(0.05, 2), 2)


def start():
    global items_counter, start_time, items_size, items_list, current_item_index

    items_counter = 0
    start_time = datetime.now()
    items_size = random.randint(10, 20)
    items_list = shuffle_list_and_return([TowarNaSztuki() if x < int(items_size / 2)
                                          else TowarNaWage() for x in range(items_size)])
    current_item_index = 0
    setCurrentItemInfo(current_item_index)
    showTowarNaWageItem(current_item) if type(current_item) == TowarNaWage else showTowarNaSztukiItem(current_item)


def main():
    global ui

    ui = interface.Ui(start, on_item_click)
    window = ui.window
    window.geometry('1000x500')
    window.resizable(False, False)
    window.title("Symulator kasjera")
    window.mainloop()


def shuffle_list_and_return(x):
    random.shuffle(x)
    return x


def setCurrentItemInfo(index):
    global current_item_type, current_item

    current_item = items_list[index]
    current_item.append_time = datetime.now()
    current_item_type = type(current_item)


def showTowarNaWageItem(item: TowarNaWage):
    ui.show_item(item.name+"x"+str(item.weight))


def showTowarNaSztukiItem(item: TowarNaSztuki):
    ui.show_item(item.name+"x"+str(item.quantity))


def on_item_click():
    pass


main()
