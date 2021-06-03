import time
import unittest

import app
import interface


class TowarNaSztukiTooMuchTest(unittest.TestCase):

    def test3(self):
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

        app.handle_towar_na_sztuki_click(app.current_item, current_item.quantity + 1)

        self.assertEqual(app.user_lost, True)