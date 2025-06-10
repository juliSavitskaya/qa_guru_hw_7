import pytest


class TestProductsNegative:
    def test_product_buy_more_than_available(self, product):
        """Тест на проверку возможности покупки товаров больше чем есть в наличии
        ОР: Ошибка ValueError"""
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)
