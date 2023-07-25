from src.item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

        # if self.number_of_sim <=0 or type(self.number_of_sim) != int:
        #     raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        # else:
        #     print(1000)


    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"


    def __add__(self, other):
        if isinstance(other,self.__class__):
            return self.quantity + other.quantity
        raise ValueError('Складывать можно только объекты Employee и Phone.')

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if number <=0 or type(number) != int:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = number











































