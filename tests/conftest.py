import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def another_product():
    return Product("pen", 10, "Blue ink pen", 20)


@pytest.fixture
def cart():
    return Cart()


@pytest.fixture
def shopping_cart(product, another_product):
    cart = Cart()
    cart.add_product(product, 2)
    cart.add_product(another_product, 3)
    return cart
