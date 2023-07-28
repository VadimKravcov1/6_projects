

from src.item import Item


class Mixin:

    __language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, Mixin):
    pass















# class MixinLog:
#     #language_keyb = ["EN", "RU"]
#     def __init__(self):
#         self.language = "EN"
#
#     def change_lang(self):
#         if self.language == "EN":
#             self.language = "RU"
#             return self
#
#         else:
#             self.language = "EN"
#             return self
#
#
#     @property
#     def language(self):
#         return self.language
#
#     @language.setter
#     def language(self, smth):
#         self.language = smth
#
#
# class Keyboard(Item, MixinLog):
#
#     def __init__(self,  name: str, price: float, quantity: int):
#         super().__init__( name, price, quantity)
#         self.__language = "EN"
#
#     def __str__(self):
#         return f'{self.name}'
#
#
#     @property
#     def language(self):
#         return self.__language
#
#     # @language.setter
#     # def language(self, smth):
#     #     self.__language = smth
#
#
#
#
# kb = Keyboard('Dark Project KD87A', 9600, 5)
#
# # print(kb.change_lang().ch)
# print(kb.language)
# kb.change_lang()
# print(kb.language)












# kb.change_lang()
# print(kb.language)











