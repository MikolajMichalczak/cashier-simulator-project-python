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


class ItemTooMuchError(Error):
    """Rzucany podczas próby skasowania towaru na sztuki wpisując zbyt dużą liczność

    Attributes:
        message -- opis błędu
    """

    def __init__(self, message="Podano zbyt dużą ilość"):
        self.message = message
        super().__init__(self.message)


class TowarNaSztukiWeightedError(Error):
    """Rzucany podczas próby zważenia towaru na sztuki

    Attributes:
        message -- opis błędu
    """

    def __init__(self, message="Zważono towar na sztuki"):
        self.message = message
        super().__init__(self.message)
