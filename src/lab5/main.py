from orders_manager import OrdersManager


def main():
    order_manager = OrdersManager(
    "orders.txt",
    "order_country.txt",
    "non_valid_orders.txt"
    )

    order_manager.write_valid_orders()
    order_manager.write_non_valid_orders()

    print("order_country.txt:")
    order_manager.print_valid_orders()

    print("\nnon_valid_orders.txt:")
    order_manager.print_non_valid_orders()

if __name__ == "__main__":
    main()