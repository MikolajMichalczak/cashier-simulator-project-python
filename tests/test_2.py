import time
import unittest

import app
import interface


class TowarNaSztukiValidateAtOnceTest(unittest.TestCase):
    """Test polegający na Skasowaniu towaru na sztuki wpisując jego liczność i klikając raz. Wymagane jest
    resetowanie pola do wartosci 1. """

    def test2(self):
        ui = interface.Ui(app.start, app.on_item_click, app.on_weigh_click)
        window = ui.window
        window.geometry('1000x500')
        window.resizable(False, False)
        window.title("Symulator kasjera")
        window.update()

        app.ui = ui
        app.start()
        app.ui.hide_next_client_btn_and_start()
        app.items_list[1] = app.TowarNaSztuki()
        app.show_next_item()
        window.update()
        time.sleep(1)
        current_item: app.TowarNaSztuki = app.current_item

        app.on_item_click(current_item.quantity)
        window.update()
        time.sleep(1)

        self.assertEqual(app.current_item_index, 2)  # sprawdzenie przejścia do następnego indeksu na liście
        self.assertEqual(int(app.ui.ent_weigh.get()), 1)  # sprawdzenie resetowania pola do wartości 1
