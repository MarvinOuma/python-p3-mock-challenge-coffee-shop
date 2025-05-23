import pytest

from classes.many_to_many import Coffee
from classes.many_to_many import Customer
from classes.many_to_many import Order


class TestCoffee:
    """Tests for the Coffee class"""

    @pytest.fixture(autouse=True)
    def setup(self):
        yield
        Coffee.instances = []
        Customer.instances = []
        Order.instances = []

    def test_has_name(self):
        """Coffee should be initialized with a name"""
        coffee = Coffee("Mocha")
        assert coffee.name == "Mocha"

    def test_name_is_immutable(self):
        """Name of Coffee should be immutable"""
        coffee = Coffee("Mocha")
        with pytest.raises(AttributeError):
            coffee.name = "Peppermint Mocha"

    def test_has_many_orders(self):
        """Coffee should have many orders"""
        coffee_1 = Coffee("Hazelnut Latte")
        coffee_2 = Coffee("Mocha")
        customer = Customer("Steve")
        order_1 = Order(customer, coffee_1, 2.0)
        order_2 = Order(customer, coffee_1, 5.0)
        order_3 = Order(customer, coffee_2, 5.0)

        assert len(coffee_1.orders) == 2
        assert len(coffee_2.orders) == 1
        assert order_1 in coffee_1.orders
        assert order_2 in coffee_1.orders
        assert order_3 not in coffee_1.orders
        assert order_3 in coffee_2.orders

    def test_orders_of_type_order(self):
        """Orders of Coffee should be of type Order"""
        coffee = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        Order(customer, coffee, 2.0)
        Order(customer, coffee, 5.0)

        assert isinstance(coffee.orders[0], Order)
        assert isinstance(coffee.orders[1], Order)

    def test_has_many_customers(self):
        """Coffee should have many customers"""
        coffee = Coffee("Flat White")
        customer = Customer("Steve")
        customer_2 = Customer("Dima")
        customer_3 = Customer("Luca")
        Order(customer, coffee, 2.0)
        Order(customer_2, coffee, 5.0)

        assert customer in coffee.customers()
        assert customer_2 in coffee.customers()
        assert customer_3 not in coffee.customers()

    def test_has_unique_customers(self):
        """Coffee should have a unique list of customers"""
        coffee = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        customer_2 = Customer("Dima")
        Order(customer, coffee, 2.0)
        Order(customer_2, coffee, 2.0)
        Order(customer, coffee, 5.0)

        assert len(set(coffee.customers())) == len(coffee.customers())
        assert len(coffee.customers()) == 2

    def test_customers_of_type_customer(self):
        """Customers of Coffee should be of type Customer"""
        coffee = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        customer_2 = Customer("Dima")
        Order(customer, coffee, 2.0)
        Order(customer_2, coffee, 5.0)

        assert isinstance(coffee.customers()[0], Customer)
        assert isinstance(coffee.customers()[1], Customer)

    def test_get_number_of_orders(self):
        """Coffee should track the number of orders"""
        coffee_1 = Coffee("Mocha")
        coffee_2 = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        Order(customer, coffee_1, 2.0)
        Order(customer, coffee_1, 5.0)

        assert coffee_1.num_orders() == 2
        assert coffee_2.num_orders() == 0

    def test_average_price(self):
        """Coffee should calculate the average price of its orders"""
        coffee_1 = Coffee("Mocha")
        coffee_2 = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        customer_2 = Customer("Dima")
        Order(customer, coffee_1, 2.0)
        Order(customer_2, coffee_1, 5.0)
        Order(customer, coffee_2, 5.0)

        assert coffee_1.average_price() == 3.5
