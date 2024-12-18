import re

class Order:
    def __init__(self, order_str: str):
        self.__is_adress_valid = True
        self.__is_phone_number_valid = True
        self.__init_from_string(order_str)

    def __init_from_string(self, string: str) -> None:
        """Инициализирование заказа из строки"""
        # i:
        # 0 - order_id
        # 1 - shopping_list
        # 2 - fio
        # 3 - address
        # 4 - phone_number
        # 5 - priority
        order_data = string.split(";")

        # May be non-valid
        self.__set_address(order_data[3])
        self.__set_phone_number(order_data[4])

        self.__set_order_id(order_data[0])
        self.__set_shopping_list(order_data[1])
        self.__set_fio(order_data[2])
        self.__set_priority(order_data[5])

    def is_address_valid(self) -> bool:
        return self.__is_adress_valid
    def is_phone_number_valid(self) -> bool:
        return self.__is_phone_number_valid
    def get_country(self) -> str:
        return self.__country
    def get_priority(self) -> str:
        return self.__priority
    def get_priority_int(self) -> int:
        """Приоритет в числовой тип данных"""
        priority_to_num = {
            "MAX": 1,
            "MIDDLE": 2,
            "LOW": 3
        }
        return priority_to_num[self.__priority]

    def to_string(self) -> str:
        """Преобразование заказа в строку"""
        if self.__is_adress_valid and self.__is_phone_number_valid:
            data = [
                self.__order_id,
                self.__shopping_list,
                self.__fio,
                self.__address,
                self.__phone_number,
                self.__priority
            ]
            return ";".join(data)

        non_valid_strings = []
        if not self.__is_adress_valid:
            data = [
                self.__order_id,
                "1",
                self.__address
            ]
            non_valid_strings.append(";".join(data))
        if not self.__is_phone_number_valid:
            data = [
                self.__order_id,
                "2",
                self.__phone_number
            ]
            non_valid_strings.append(";".join(data))
        return "\n".join(non_valid_strings)

    def __set_order_id(self, order_id: str) -> None:
        self.__order_id = order_id
    def get_order_id(self) -> str:
        return self.__order_id

    def __set_shopping_list(self, shopping_list : str) -> None:
        """Форматирование набора продуктов"""
        shopping_list = shopping_list.split(', ')
        shopping_list_set = set(shopping_list)
        shopping_list_formatted = []
        for goods in sorted(shopping_list_set):
            number_of_goods = shopping_list.count(goods)
            if number_of_goods == 1:
                shopping_list_formatted.append(goods)
            else:
                shopping_list_formatted.append(f"{goods} x{number_of_goods}")
        shopping_list_str = ", ".join(shopping_list_formatted)
        self.__shopping_list = shopping_list_str
    def get_shopping_list(self) -> str:
        return self.__shopping_list

    def __set_fio(self, fio: str) -> None:
        self.__fio = fio
    def get_fio(self) -> str:
        return self.__fio

    def __set_address(self, address: str) -> None:
        """Проверка адреса на вверный формат"""
        # i:
        # 0 - country
        # 1 - region
        # 2 - city
        # 3 - street
        address_data = address.split(". ")

        if not address:
            self.__address = "no data"
            self.__is_adress_valid = False
        elif len(address_data) != 4:
            self.__address = ". ".join(address_data)
            self.__is_adress_valid = False
        else:
            self.__country = address_data[0]
            self.__address = ". ".join(address_data[1:])
    def get_address(self) -> str:
        return self.__address

    def __set_phone_number(self, phone_number: str) -> None:
        """Номер телефона в формате +x-xxx-xxx-xx-xx"""
        phone_number_pattern = re.compile(r'^\+\d-\d{3}-\d{3}-\d{2}-\d{2}$')

        if not phone_number:
            self.__phone_number = "no data"
            self.__is_phone_number_valid = False
        elif not phone_number_pattern.match(phone_number):
            self.__phone_number = phone_number
            self.__is_phone_number_valid = False
        else:
            self.__phone_number = phone_number
    def get_phone_number(self) -> str:
        return self.__phone_number

    def __set_priority(self, priority: str) -> None:
        self.__priority = priority
