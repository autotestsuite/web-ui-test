def with_args(by: tuple, *args) -> tuple:
    by_, value = by
    return by_, value.format(*args)
