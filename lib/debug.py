#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Customer
from classes.many_to_many import Order
from classes.many_to_many import Coffee

if __name__ == '__main__':
    print("Starting debug session. Use 'n' for next line, 's' for step into, 'c' for continue, and 'q' for quit.")

    try:
        ipdb.set_trace()
    except ImportError:
        print("Could not start debug session. Please install ipdb: pip install ipdb")


