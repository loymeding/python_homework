'''
Создайте программу, которая будет моделировать систему учёта товаров на складе. Программа должна включать следующие классы:

Товар (Product):
атрибуты: название, количество, цена;
методы: увеличение количества, уменьшение количества, расчёт стоимости.

Склад (Warehouse):
атрибуты: список товаров;
методы: добавление товара, удаление товара, расчёт общей стоимости товаров.

Продавец (Seller):
атрибуты: имя;
методы: продажа товара (уменьшение количества и расчёт выручки), отчёт о продажах.

Программа должна позволять добавлять товары на склад, удалять товары со склада, продавать товары и формировать отчёт о продажах в виде списка проданных товаров с указанием их количества и стоимости.
Также программа должна вести логирование всех операций с товарами, чтобы можно было отслеживать историю изменений количества товаров на складе и продаж.
'''


class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def increase_quantity(self, amount):
        self.quantity += amount
        self.log_operation(f"Увеличено количество товара '{self.name}' на {amount}. Текущее количество: {self.quantity}.")

    def decrease_quantity(self, amount):
        if amount > self.quantity:
            raise ValueError(f"Недостаточно товара '{self.name}' на складе. Доступно: {self.quantity}, запрашиваемое: {amount}.")
        self.quantity -= amount
        self.log_operation(f"Уменьшено количество товара '{self.name}' на {amount}. Текущее количество: {self.quantity}.")

    def calculate_cost(self):
        return self.quantity * self.price

    def log_operation(self, message):
        with open("inventory_log.txt", "a") as log_file:
            log_file.write(message + "\n")


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        product.log_operation(f"Добавлен товар '{product.name}' на склад. Количество: {product.quantity}, Цена: {product.price}.")

    def remove_product(self, product_name):
        product = self.find_product(product_name)
        if product:
            self.products.remove(product)
            product.log_operation(f"Удален товар '{product.name}' со склада.")

    def find_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def calculate_total_value(self):
        total_value = sum(product.calculate_cost() for product in self.products)
        return total_value


class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_report = []

    def sell_product(self, warehouse, product_name, quantity):
        product = warehouse.find_product(product_name)
        if product:
            product.decrease_quantity(quantity)
            sale_value = product.price * quantity
            self.sales_report.append((product.name, quantity, sale_value))
            product.log_operation(f"Продан товар '{product.name}', Количество: {quantity}, Выручка: {sale_value}.")
        else:
            raise ValueError(f"Товар '{product_name}' не найден на складе.")

    def generate_sales_report(self):
        return self.sales_report


# Пример использования
if __name__ == "__main__":
    warehouse = Warehouse()
    seller = Seller("Никита")

    # Добавление товаров на склад
    product1 = Product("Яблоки", 100, 15)
    product2 = Product("Бананы", 50, 10)
    warehouse.add_product(product1)
    warehouse.add_product(product2)

    # Продажа товара
    try:
        seller.sell_product(warehouse, "Яблоки", 5)
        seller.sell_product(warehouse, "Бананы", 2)
    except ValueError as e:
        print(e)

    # Отчет о продажах
    sales_report = seller.generate_sales_report()
    print("Отчет о продажах:")
    for item in sales_report:
        print(f"Товар: {item[0]}, Количество: {item[1]}, Выручка: {item[2]}")

    # Общая стоимость товаров на складе
    total_value = warehouse.calculate_total_value()
    print(f"Общая стоимость товаров на складе: {total_value}")
