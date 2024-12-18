import unittest

from src.lab5.orders_manager import OrdersManager

class OrdersManagerTestCase(unittest.TestCase):
    def test_orders_manager(self):
        # Given
        order_manager = OrdersManager("orders.txt")

        expected_valid_orders_output = """87459;Молоко x2, Хлеб, Яблоки x2;Иванов Иван Иванович;Московская область. Москва. улица Пушкина;+7-912-345-67-89;MAX
31987;Колбаса x2, Макароны, Сыр x2;Петрова Анна;Ленинградская область. Санкт-Петербург. набережная реки Фонтанки;+7-921-456-78-90;MIDDLE
72901;Кофе x2, Чай x2;Михайлов Сергей Петрович;Англия. Лондон. Бейкер-стрит;+4-207-946-09-58;LOW
48276;Макароны, Яблоки x2;Алексеев Алексей Алексеевич;Лацио. Рим. Колизей;+3-061-234-56-78;MAX
31987;Колбаса x2, Макароны, Сыр x2;Петрова Анна Сергеевна;Иль-де-Франс. Париж. Шанз-Элизе;+3-214-020-50-50;MIDDLE"""

        expected_non_valid_orders_output = """56342;2;+4-989-234-56
65829;2;+34-93-1234-567
84756;1;Япония. Шибуя. Шибуя-кроссинг
84756;2;+8-131-234-5678
90385;1;no data"""

        # When
        valid_orders_output = order_manager.get_valid_orders_output()
        non_valid_orders_output = order_manager.get_non_valid_orders_output()

        # Then
        self.assertEqual(expected_valid_orders_output, valid_orders_output)
        self.assertEqual(expected_non_valid_orders_output, non_valid_orders_output)