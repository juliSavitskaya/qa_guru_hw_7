import pytest


class TestCartNegative:
    @pytest.mark.parametrize("count", [0, -2])
    def test_add_product_invalid_count(self, product, cart, count):
        """Тест на добавление невалидного числа товаров в корзину
        ОР: Ошибка ValueError"""
        with pytest.raises(ValueError):
            cart.add_product(product, count)

    def test_buy_not_enough(self, product, cart):
        """Тест проверяет возможность покупки большего числа товаров чем есть в наличии
        ОР: Ошибка ValueError"""
        cart.add_product(product, product.quantity + 1)
        with pytest.raises(ValueError):
            cart.buy()
