from dataclasses import dataclass


@dataclass()
class Product:
    """Класс, представляющий товар в интернет-магазине"""
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity: int) -> bool:
        """Метод проверки количества товара"""
        return self.quantity >= quantity

    def buy(self, quantity: int):
        """Метод покупки указанного количества товара, уменьшает его общий остаток
        Исключения: ValueError: Если товара недостаточно для покупки"""
        if not self.check_quantity(quantity):
            raise ValueError("Not enough items in stock")
        self.quantity -= quantity

    def __hash__(self) -> int:
        """Возвращает хеш-значение товара по его имени и описанию"""
        return hash(self.name + self.description)


class Cart:
    """Класс корзины"""

    products: dict[Product, int]

    def __init__(self) -> None:
        self.products = {}

    def add_product(self, product: Product, buy_count: int = 1) -> None:
        """Метод добавления товара в корзину"""
        if buy_count <= 0:
            raise ValueError("buy_count должно быть больше 0")
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count: int | None = None) -> None:
        """Метод удаления товара из корзины"""
        if product not in self.products:
            return
        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self) -> None:
        """Метод очищения корзины"""
        self.products.clear()

    def get_total_price(self) -> float:
        """Метод, возвращающий сумму стоимости всех товаров в корзине"""
        total = 0.0
        for product, count in self.products.items():
            total += product.price * count
        return total

    def buy(self) -> None:
        """Метод для покупки всех товаров в корзине"""
        # Сначала проверим, хватает ли всех товаров
        for product, count in self.products.items():
            if not product.check_quantity(count):
                raise ValueError(f"Not enough '{product.name}' in stock")

        # Покупаем (уменьшаем количество у товаров)
        for product, count in self.products.items():
            product.buy(count)
        # Корзину очищаем
        self.clear()
