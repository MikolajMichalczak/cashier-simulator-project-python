import time
import unittest

import app
import interface


class TowarNaSztukiValidateOneByOneTest(unittest.TestCase):
    """Test polegający na skasowaniu towaru na sztuki po klikając na niego kilka razy."""

    def test1(self):
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

        for i in range(current_item.quantity):
            app.on_item_click(1)
            window.update()
            time.sleep(0.4)

        self.assertEqual(app.current_item_index, 2)  # sprawdzenie przejścia do następnego indeksu na liście
