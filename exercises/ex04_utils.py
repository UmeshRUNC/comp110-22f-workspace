"""EX04 - Utils."""

__author__ = "730469023"


def all(set: int, integer: int) -> bool:
    """function to check whether or not all the integers are the same as the given int."""
    if len(set) == 0:
        return False
    i = 0
    while i < len(set):
        if integer == set[i]:
            i += 1
        else: 
            return False
    return True


def max(set: int) -> int:
    """Returns us the biggest integer in the set."""
    if len(set) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        int = set[0]
        i = 1
    while i < len(set):
        if set[i] > int:
            int = set[i]
            i += 1
        else:
            i += 1
    else:
        return int


def is_equal(seta: int, setb: int) -> bool:
    """Returns a value telling us if the sets are equal or not."""
    if seta == setb:
        return True
    else:
        return False