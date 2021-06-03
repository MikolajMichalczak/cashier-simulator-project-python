import interface
from exceptions import *
from datetime import datetime
import random

item_names = ["Marchewka", "Arbuz", "Chleb", "Makaron", "Dorsz", "Ananas", "Banan", "Ziemniak", "Cukinia", "Pomidor",
              "Jabłko", "Cytryna", "Czekolada",
              "Mango", "Gruszka", "Kapusta", "Kiwi", "Groch", "Granat", "Tuńczyk"]
items_list = []
items_counter = 0
start_time = datetime.now()
items_size = 0
should_weigh_item = False
user_lost = False
validating_finished = False
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
        self.weighed = False


def start():
    global items_counter, start_time, items_size, items_list, current_item_index, user_lost, validating_finished

    user_lost = False
    validating_finished = False
    items_counter = 0
    start_time = datetime.now()
    items_size = random.randint(10, 20)
    items_list = generate_items_list(3)
    current_item_index = 0
    set_current_item_info(current_item_index)
    show_towar_na_wage_item(current_item) if current_item_type == TowarNaWage else show_towar_na_sztuki_item(
        current_item)


def main():
    global ui

    if __name__ == "__main__":
        ui = interface.Ui(start, on_item_click, on_weigh_click)
        window = ui.window
        window.geometry('1000x500')
        window.resizable(False, False)
        window.title("Symulator kasjera")
        window.mainloop()


def shuffle_list_and_return(x):
    random.shuffle(x)
    return x


def generate_items_list(size):
    unshuffled_list = shuffle_list_and_return([TowarNaSztuki() if x < int(size / 2)
                                               else TowarNaWage() for x in range(size)])
    return shuffle_list_and_return(unshuffled_list)


def set_current_item_info(index):
    global current_item_type, current_item

    current_item = items_list[index]
    current_item.append_time = datetime.now()
    current_item_type = type(current_item)


def show_towar_na_wage_item(item: TowarNaWage):
    ui.show_item(item.name + " ?kg")


def show_towar_na_sztuki_item(item: TowarNaSztuki):
    ui.show_item(item.name + " x" + str(item.quantity))


def on_item_click(quantity):
    global should_weigh_item, items_counter, user_lost, validating_finished
    try:
        if should_weigh_item:
            should_weigh_item = False
            raise ItemUnweightedError()
        else:
            if current_item_type == TowarNaWage:
                if is_towar_na_wage_weighed(current_item):
                    items_counter += 1
                    current_item.validate_time = datetime.now()
                    ui.clear_entry()
                    show_next_item()
                else:
                    should_weigh_item = True
            else:
                handle_towar_na_sztuki_click(current_item, quantity)
    except ItemUnweightedError:
        user_lost = True
        ui.show_loss_information()


def is_towar_na_wage_weighed(item: TowarNaWage):
    return True if item.weighed else False


def on_weigh_click():
    global should_weigh_item, user_lost

    try:
        if current_item_type == TowarNaWage:
            handle_on_weigh_click(current_item)
        else:
            raise TowarNaSztukiWeightedError

    except TowarNaSztukiWeightedError:
        user_lost = True
        ui.show_loss_information()


def handle_on_weigh_click(item: TowarNaWage):
    global should_weigh_item

    if should_weigh_item:
        should_weigh_item = False
        item.weighed = True
        ui.show_item(item.name + " " + str(item.weight) + " kg")


def show_next_item():
    global items_counter, current_item_index, items_list

    current_item_index += 1
    if current_item_index != len(items_list):
        set_current_item_info(current_item_index)
        show_towar_na_wage_item(current_item) if type(current_item) == TowarNaWage else show_towar_na_sztuki_item(
            current_item)
    else:
        show_end_screen()


def increase_items_count_from_towar_na_sztuki(item: TowarNaSztuki):
    global items_counter
    items_counter += item.quantity


def show_end_screen():
    global validating_finished, start_time, items_counter

    validating_finished = True
    difference = (datetime.now() - start_time)
    total_seconds = difference.total_seconds()
    avg_item_time = total_seconds/items_counter
    ui.show_end_information("Average time to validate one item: " + "{:.3f}".format(avg_item_time) + "s")


def handle_towar_na_sztuki_click(item: TowarNaSztuki, entry_quantity):
    global user_lost

    try:
        if item.quantity - entry_quantity < 0:
            raise ItemTooMuchError()
        else:
            if item.quantity - entry_quantity == 0:
                increase_items_count_from_towar_na_sztuki(current_item)
                ui.clear_entry()
                show_next_item()
            else:
                item.quantity -= entry_quantity
                ui.clear_entry()
                ui.show_item(item.name + " x" + str(item.quantity))

    except ItemTooMuchError:
        user_lost = True
        ui.show_loss_information()


main()
