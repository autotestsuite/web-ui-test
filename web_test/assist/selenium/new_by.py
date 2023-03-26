def with_args(locator: tuple, *args) -> tuple:
    by_, value = locator
    return by_, value.format(*args)
