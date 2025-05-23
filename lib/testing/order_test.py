import pytest

from classes.many_to_many import Coffee
from classes.many_to_many import Customer
from classes.many_to_many import Order


class TestOrders:
    '''Tests for the Order class'''

    @pytest.fixture(autouse=True)
    def setup(self):
        yield
        Coffee.instances = []
        Customer.instances = []
        Order.instances = []

    def test_has_price(self):
        '''Order is initialized with a price'''
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2.0)
        order_2 = Order(customer, coffee, 5.0)

        assert order_1.price == 2.0
        assert order_2.price == 5.0

    def test_price_is_valid(self):
        """Price is of type float and between 1.0 and 10.0"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2.0)
        order_2 = Order(customer, coffee, 5.0)

        assert isinstance(order_1.price, float)
        assert isinstance(order_2.price, float)

        # Check if price validation works
        with pytest.raises(Exception):
            Order(customer, coffee, 0.99)

        with pytest.raises(Exception):
            Order(customer, coffee, 10.01)

    def test_price_is_immutable(self):
        """Price is immutable"""
        coffee = Coffee("Mocha")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee, 2.0)

        # Check if price remains unchanged
        order_1.price = 3.0
        assert order_1.price == 2.0

    def test_has_a_customer(self):
        '''Order has a customer'''
        coffee = Coffee("Mocha")
        customer_1 = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer_1, coffee, 2.0)
        order_2 = Order(customer_2, coffee, 5.0)

        assert order_1.customer == customer_1
        assert order_2.customer == customer_2

    def test_customer_of_type_customer(self):
        '''Customer is of type Customer'''
        coffee = Coffee("Vanilla Latte")
        customer_1 = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer_1, coffee, 2.0)
        order_2 = Order(customer_2, coffee, 5.0)

        assert isinstance(order_1.customer, Customer)
        assert isinstance(order_2.customer, Customer)

    def test_has_a_coffee(self):
        '''Order has a coffee'''
        coffee_1 = Coffee("Mocha")
        coffee_2 = Coffee("Peppermint Chai")
        customer = Customer('Wayne')
        order_1 = Order(customer, coffee_1, 2.0)
        order_2 = Order(customer, coffee_2, 5.0)

        assert order_1.coffee == coffee_1
        assert order_2.coffee == coffee_2

    def test_coffee_of_type_coffee(self):
        '''Coffee is of type Coffee'''
        coffee_1 = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Peppermint Chai")
        customer = Customer('Steve')
        order_1 = Order(customer, coffee_1, 2.0)
        order_2 = Order(customer, coffee_2, 5.0)

        assert isinstance(order_1.coffee, Coffee)
        assert isinstance(order_2.coffee, Coffee)

    def test_get_all_orders(self):
        '''Order class all attribute'''
        Order.all = []
        coffee = Coffee("Mocha")
        customer = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, coffee, 2.0)
        order_2 = Order(customer_2, coffee, 5.0)

        assert len(Order.all) == 2
        assert order_1 in Order.all
        assert order_2 in Order.all