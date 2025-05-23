import pytest

from classes.many_to_many import Coffee
from classes.many_to_many import Customer
from classes.many_to_many import Order


class TestCustomer:
    """Tests for the Customer class"""

    @pytest.fixture(autouse=True)
    def setup(self):
        yield
        Coffee.instances = []
        Customer.instances = []
        Order.instances = []

    def test_has_name(self):
        """Customer should be initialized with a name"""
        customer = Customer("Steve")
        assert customer.name == "Steve"

    def test_name_is_mutable_string(self):
        """Name of Customer should be mutable string"""
        customer = Customer("Steve")
        customer.name = "Stove"

        assert customer.name == "Stove"

        # Check if name remains string
        customer.name = 1
        assert customer.name == "Stove"
        assert isinstance(customer.name, str)

    def test_name_length(self):
        """Name of Customer should be between 1 and 15 characters"""
        customer = Customer("Steve")
        assert len(customer.name) == 5

        # Check if empty name is ignored
        customer.name = ""
        assert customer.name == "Steve"

        # Check if too long name is truncated
        customer.name = "TooLongForAName!"
        assert customer.name == "Steve"

    def test_has_many_orders(self):
        """Customer should have many orders"""
        coffee = Coffee("Vanilla Latte")
        customer_1 = Customer("Steve")
        customer_2 = Customer("Dima")
        order_1 = Order(customer_1, coffee, 2.0)
        order_2 = Order(customer_1, coffee, 5.0)
        order_3 = Order(customer_2, coffee, 5.0)

        assert len(customer_1.orders) == 2
        assert len(customer_2.orders) == 1
        assert order_1 in customer_1.orders
        assert order_2 in customer_1.orders
        assert order_3 not in customer_1.orders
        assert order_3 in customer_2.orders

    def test_orders_of_type_order(self):
        """Orders of Customer should be of type Order"""
        coffee = Coffee("Vanilla Latte")
        customer = Customer("Steve")
        Order(customer, coffee, 2.0)
        Order(customer, coffee, 5.0)

        assert isinstance(customer.orders[0], Order)
        assert isinstance(customer.orders[1], Order)

    def test_has_many_coffees(self):
        """Customer should have many coffees"""
        coffee_1 = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")
        coffee_3 = Coffee("Mocha")
        customer = Customer("Steve")
        Order(customer, coffee_1, 2.0)
        Order(customer, coffee_2, 5.0)

        assert coffee_1 in customer.coffees()
        assert coffee_2 in customer.coffees()
        assert coffee_3 not in customer.coffees()

    def test_has_unique_coffees(self):
        """Customer should have a unique list of coffees they have ordered"""
        coffee = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")
        customer = Customer("Steve")
        Order(customer, coffee, 2.0)
        Order(customer, coffee, 2.0)
        Order(customer, coffee_2, 5.0)

        assert len(set(customer.coffees())) == len(customer.coffees())
        assert len(customer.coffees()) == 2

    def test_coffees_of_type_coffee(self):
        """Coffees of Customer should be of type Coffee"""
        coffee_1 = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")
        customer = Customer("Steve")
        Order(customer, coffee_1, 2.0)
        Order(customer, coffee_2, 5.0)

        assert isinstance(customer.coffees()[0], Coffee)
        assert isinstance(customer.coffees()[1], Coffee)

    def test_create_order(self):
        """Creates a new order for a customer"""
        coffee_1 = Coffee("Vanilla Latte")
        coffee_2 = Coffee("Flat White")
        customer_1 = Customer("Steve")
        customer_2 = Customer("Dima")
        order_1 = customer_1.create_order(coffee_1, 2.0)
        order_2 = customer_2.create_order(coffee_2, 5.0)

        # Check that the order is of type Order
        assert isinstance(order_1, Order)
        assert isinstance(order_2, Order)

        # Check that the order has the correct customer and coffee
        assert order_1.customer == customer_1
        assert order_1.coffee == coffee_1
        assert order_2.customer == customer_2
        assert order_2.coffee == coffee_2