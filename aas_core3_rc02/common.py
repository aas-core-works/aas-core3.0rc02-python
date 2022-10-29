"""Provide common functions shared among the modules."""


# This code has been automatically generated by aas-core-codegen.
# Do NOT edit or append.


from typing import NoReturn


def assert_never(value: NoReturn) -> NoReturn:
    """
    Signal to mypy to perform an exhaustive matching.

    Please see the following page for more details:
    https://hakibenita.com/python-mypy-exhaustive-checking
    """
    assert False, f"Unhandled value: {value} ({type(value).__name__})"


# This code has been automatically generated by aas-core-codegen.
# Do NOT edit or append.
