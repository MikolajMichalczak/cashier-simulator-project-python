import time
import unittest

import app
import interface


class TowarNaWageUnweightedTest(unittest.TestCase):

    def test5(self):
        ui = interface.Ui(app.start, app.on_item_click, app.on_weigh_click)
        window = ui.window
        window.geometry('1000x500')
        window.resizable(False, False)
        window.title("Symulator kasjera")
        window.update()

        app.ui = ui
        app.start()
        app.ui.hide_next_client_btn_and_start()
        app.items_list[1] = app.TowarNaWage()
        app.show_next_item()
        window.update()
        time.sleep(1)

        app.on_item_click(1)
        app.on_item_click(1)

        window.update()
        time.sleep(1)

        self.assertEqual(app.user_lost, True)