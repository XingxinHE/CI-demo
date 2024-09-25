def is_even(n):
    if not isinstance(n, int):
        return False
    return n % 2 == 0