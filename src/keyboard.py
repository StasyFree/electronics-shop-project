from src.item import Item


class MixinLanguage:

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self.__language

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLanguage, Item):

    pass

