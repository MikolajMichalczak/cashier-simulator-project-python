import unittest
import app


class SignleItemProbabilityTest(unittest.TestCase):

    def test7(self):
        test_item_list = app.generate_items_list(200)
        towary_na_sztuki_list = [towar for towar in test_item_list if type(towar) == app.TowarNaSztuki]
        pojedyncze_towary = []
        for towar in towary_na_sztuki_list:
            current_towar: app.TowarNaSztuki = towar
            if current_towar.quantity == 1:
                pojedyncze_towary.append(current_towar)

        self.assertGreater(len(pojedyncze_towary)/len(towary_na_sztuki_list), 0.3)
