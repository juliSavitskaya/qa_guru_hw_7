class TestCart:
    def test_add_product(self, product, cart):
        """Тест на проверку добавления товара в корзину
        ОР: Количество товара в корзине корректное"""
        cart.add_product(product, 5)

        assert cart.products[product] == 5, "Некорректное число товаров в корзине"

        # Добавление ещё этого же продукта
        cart.add_product(product, 2)

        assert cart.products[product] == 7, "Некорректное число товаров в корзине"

    def test_remove_product_full(self, product, cart):
        """Тест на проверку полного удаления товаров из корзины
        ОР: Товаров нет в корзине"""
        cart.add_product(product, 5)
        cart.remove_product(product)

        assert product not in cart.products, "Товары остались в корзине"

    def test_remove_product_partially(self, product, cart):
        """Тест на проверку удаления части товаров из корзины
        ОР: Количество товаров в корзине корректное"""
        cart.add_product(product, 5)
        cart.remove_product(product, 2)

        assert cart.products[product] == 3, "Некорректное число товаров в корзине"

    def test_remove_product_removes_if_count_exceeds(self, product, cart):
        """Тест на проверку удаления числа товаров больше чем есть в корзине
        ОР: Товаров нет в корзине"""
        cart.add_product(product, 5)
        cart.remove_product(product, 10)  # Удаляем больше, чем есть

        assert product not in cart.products, "Товары остались в корзине"

    def test_clear(self, shopping_cart):
        """Тест на проверку очистки корзины
        ОР: Товаров нет в корзине"""
        shopping_cart.clear()

        assert shopping_cart.products == {}, "Корзина не пустая"

    def test_get_total_price(self, shopping_cart):
        """Тест на проверку подсчета общей суммы товаров в корзине
        ОР: Сумма товаров посчитана корректно"""
        assert shopping_cart.get_total_price() == 230, "Сумма товаров рассчитана некорректно"

    def test_buy_success(self, product, another_product, shopping_cart):
        """Тест на возможность покупки товаров из корзины
        ОР: Покупка успешна, количество товаров в корзине уменьшилось"""
        start_quantity = product.quantity, another_product.quantity
        shopping_cart.buy()

        assert product.quantity == start_quantity[0] - 2, "Некорректное число товаров в корзине"
        assert another_product.quantity == start_quantity[1] - 3, "Некорректное число товаров в корзине"
        assert shopping_cart.products == {}, "Товары остались в корзине"
