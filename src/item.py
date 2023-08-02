import csv

class InstantiateCSVError(Exception):
    pass

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        #Item.all.append(f'Item({self.__name},{self.price},{self.quantity})')


    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other,self.__class__):
            return self.quantity + other.quantity
        raise ValueError('Складывать можно только объекты Item и Phone.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self,name_string):
        name_str = ""
        if len(name_string)<=10:
            name_str = name_string
        else:
            count = 0
            word = []
            for i in name_string:
                word.append(i)
            while len(word)!=10:
                word.pop(-1)
            name_str = "".join(word)
        name = name_str
        self.__name = name



# emp1 = Item("Telephone",111.2,10)

#TestCase #1 Setter name
# emp1.name = "1234567891234"
# assert emp1.name == '1234567891'
# print(emp1.name)


    @classmethod
    def instantiate_from_csv(cls, filename='/home/vadim/PycharmProjects/6_projects/src/items.csv'):
        counter = 0

        import os
        path_to_file = filename
        if not os.path.exists(path_to_file):
            raise FileNotFoundError("Отсутствует файл item.csv")

        with open(filename, newline='', encoding="cp1251") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                cls.all.append(Item(row['name'], float(row['price']), int(row['quantity'])))
                counter+=1


            if counter<5:
                raise InstantiateCSVError("Файл item.csv поврежден")


    @staticmethod
    def string_to_number(numb):
        return int(float(numb))








# cl = InstantiateCSVError('Items.csv')
# it = Item
# it.instantiate_from_csv()
# print(it.all)












