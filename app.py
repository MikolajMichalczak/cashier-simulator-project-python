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
should_weigh_item = False  # flaga odpowiedzialna za wymuszanie na użutkowniku zważenia towar \
# (w przeciwnym razie przegrana)
user_lost = False  # flaga ustawiana gdy uzytkownik przegra
validating_finished = False  # flaga ustawiana gdy użytkownik skasuje wszystkie towary
global current_item_index
global ui
global current_item_type
global current_item


class Towar:
    """Klasa bazowa towarów"""

    def __init__(self):
        self.append_time = datetime.now()
        self.validate_time = datetime.now()
        self.name = random.choice(item_names)


class TowarNaSztuki(Towar):
    """Klasa reprezentująca towar na sztuki"""

    def __init__(self):
        super().__init__()
        self.quantity = self.getQuantity()

    @staticmethod
    def getQuantity():
        """Metoda przydzielająca oraz zwracająca ilość towaru (50% szansy na wylosowanie pojedynczego - w przeciwnym
        razie ilość z zakresu 1-50

        Return:
            ilość towaru
        """

        is_more_than_one = random.choice([True, False])
        return random.randint(2, 50) if is_more_than_one else 1


class TowarNaWage(Towar):
    """Klasa reprezentująca towar na wagę"""

    def __init__(self):
        super().__init__()
        self.weight = round(random.uniform(0.05, 2), 2)
        self.weighed = False


def start():
    """Metoda rozpoczynająca "grę" - zerowanie globalnych zmiennych, tworzenie listy towarów, ustawianie aktualnego (
    pierwszego) towaru oraz wyświtlanie go na ekranie """

    global items_counter, start_time, items_size, items_list, current_item_index, user_lost, validating_finished

    user_lost = False
    validating_finished = False
    items_counter = 0
    start_time = datetime.now()
    items_size = random.randint(10, 20)
    items_list = generate_items_list(items_size)
    current_item_index = 0
    set_current_item_info(current_item_index)
    show_towar_na_wage_item(current_item) if current_item_type == TowarNaWage else show_towar_na_sztuki_item(
        current_item)


def main():
    """Metoda uruchamiana jako pierwsza w całej aplikacji - tworzenie interfejsu"""

    global ui

    if __name__ == "__main__":  # nie jest uruchamiana w przypadku testu
        ui = interface.Ui(start, on_item_click, on_weigh_click)
        window = ui.window
        window.geometry('1000x500')
        window.resizable(False, False)
        window.title("Symulator kasjera")
        window.mainloop()


def shuffle_list_and_return(x):
    """Metoda mieszająca kolejność towarów z listy

    Attributes:
        x - lista towarów

    Return:
        pomieszana lista towarów
    """

    random.shuffle(x)
    return x


def generate_items_list(size):
    """Metoda generująca listę towarów

    Attributes:
        size - wielkość listy

    Return:
        lista towarów
    """

    unshuffled_list = shuffle_list_and_return([TowarNaSztuki() if x < int(size / 2)
                                               else TowarNaWage() for x in range(size)])  # połowa towarów na sztuki
    return shuffle_list_and_return(unshuffled_list)


def set_current_item_info(index):
    """Metoda aktualizująca aktualny towar i dane o nim

        Attributes:
            index - aktualny indeks na towaru z listy
        """

    global current_item_type, current_item

    current_item = items_list[index]
    current_item.append_time = datetime.now()
    current_item_type = type(current_item)


def show_towar_na_wage_item(item: TowarNaWage):
    """Metoda ta wywołuje metodę w interfejsie - pokazującą kolejny towar(towar na wagę) """

    ui.show_item(item.name + " ?kg")


def show_towar_na_sztuki_item(item: TowarNaSztuki):
    """Metoda ta wywołuje metodę w interfejsie - pokazującą kolejny towar(towar na sztuki) """

    ui.show_item(item.name + " x" + str(item.quantity))


def on_item_click(quantity):
    """Metoda wywoływana po kliknięciu przycisku towaru

    Attributes:
        quantity - ilość pobrana z okienka interfejsu
    """

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
    """Metoda sprawdzająca czy towar na wagę został już zważony czy nie (na podstawie flagi ustawianej w obiekcie)

    Attributes:
        item - aktualny towar (na wagę)

    Return:
        True - towar został już zważony
        False - towar nie został jeszcze zważony
    """

    return True if item.weighed else False


def on_weigh_click():
    """Metoda obsługująca kliknięcie przycisku odpowiedzialnego za ważenie towaru"""

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
    """Metoda obsługująca klikniecię przycisku odpowiedzialnego za ważenie towaru podczas gdy aktualnym towarem jest
    towar na wagę - ustawienie wagi na przycisku

    Attributes:
        item - aktualny towar (na wagę)"""

    global should_weigh_item

    if should_weigh_item:
        should_weigh_item = False
        item.weighed = True
        ui.show_item(item.name + " " + str(item.weight) + " kg")


def show_next_item():
    """Metoda odpowiedzialna za wywoływanie metody interfejsu odpowiedzialnej za pokazywanie kolejnego towaru"""

    global items_counter, current_item_index, items_list

    current_item_index += 1
    if current_item_index != len(items_list):
        set_current_item_info(current_item_index)
        show_towar_na_wage_item(current_item) if type(current_item) == TowarNaWage else show_towar_na_sztuki_item(
            current_item)
    else:
        show_end_screen()


def increase_items_count_from_towar_na_sztuki(item: TowarNaSztuki):
    """Metoda zwiększająca licznik towarów o ilość aktualnego towaru na sztuki

        Attributes:
            item - aktualny towar (na sztuki)
    """
    global items_counter
    items_counter += item.quantity


def show_end_screen():
    """Metoda wywołująca metodę interfejsu odpowiedzialną za pokazanie ekranu końcowego (po skasowaniu wszystkich
    towarów)
    """

    global validating_finished, start_time, items_counter

    validating_finished = True
    difference = (datetime.now() - start_time)
    total_seconds = difference.total_seconds()
    avg_item_time = total_seconds / items_counter
    ui.show_end_information("Average time to validate one item: " + "{:.3f}".format(avg_item_time) + "s")


def handle_towar_na_sztuki_click(item: TowarNaSztuki, entry_quantity):
    """Metoda obsługująca klikniecie przycisku z towarem na sztuki

    Attributes:
        item - aktualny towar (na sztuki)
        entry_quantity - ilość pobrana z okienka interfejsu
    """

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
