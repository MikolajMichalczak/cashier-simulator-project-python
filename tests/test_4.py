import time
import unittest

import app
import interface


class TowarNaSztukiWeightedTest(unittest.TestCase):

    def test4(self):
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

        app.on_weigh_click()

        self.assertEqual(app.user_lost, True)