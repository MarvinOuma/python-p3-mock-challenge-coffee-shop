#!/usr/bin/env python3

def customize_test_names(item):
    parent_object = item.parent.obj
    test_function = item.obj

    # Extracting docstrings or names
    parent_prefix = parent_object.__doc__.strip() if parent_object.__doc__ else parent_object.__class__.__name__
    test_suffix = test_function.__doc__.strip() if test_function.__doc__ else test_function.__name__

    # Constructing custom test name
    custom_name = ' '.join((parent_prefix, test_suffix)) if parent_prefix or test_suffix else None

    if custom_name:
        item._nodeid = custom_name

# Registering the function to customize test names
def pytest_itemcollected(item):
    customize_test_names(item)