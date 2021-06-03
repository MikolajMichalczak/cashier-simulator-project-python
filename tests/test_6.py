import time
import unittest

import app
import interface


class ValidateAllItemsTest(unittest.TestCase):

    def test6(self):
        ui = interface.Ui(app.start, app.on_item_click, app.on_weigh_click)
        window = ui.window
        window.geometry('1000x500')
        window.resizable(False, False)
        window.title("Symulator kasjera")
        window.update()

        app.ui = ui
        app.start()
        app.ui.hide_next_client_btn_and_start()
        window.update()
        time.sleep(1)

        for i in range(len(app.items_list)):
            if app.current_item_type == app.TowarNaWage:
                app.on_item_click(1)
                app.on_weigh_click()
                window.update()
                time.sleep(0.4)

                app.on_item_click(1)
                window.update()
                time.sleep(0.4)

            else:
                current_item: app.TowarNaSztuki = app.current_item
                app.on_item_click(current_item.quantity)
                window.update()
                time.sleep(0.4)

        window.update()
        time.sleep(1)

        self.assertEqual(app.validating_finished, True)
