class Error(Exception):
    """Klasa bazowa dla innych wyjątków"""
    pass


class ItemUnweightedError(Error):
    """Rzucany w momencie gdy towar na wagę nie zostanie zważony przed skasowaniem

    Attributes:
        message -- opis błędu
    """

    def __init__(self, message="Towar na wagę nie został zważony przed skasowaniem"):
        self.message = message
        super().__init__(self.message)
