class TestProducts:
    def test_product_check_quantity(self, product):
        """Тест на проверку количества товара в наличии"""
        assert product.check_quantity(10) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        """Тест на проверку покупки товара
        ОР: Остаток после покупки равен разнице между начальным числом товаров и числом купленных товаров"""
        start_quantity = product.quantity
        product.buy(10)

        assert product.quantity == start_quantity - 10
