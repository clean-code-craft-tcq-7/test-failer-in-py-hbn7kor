def size(cms: int):
    if cms < 38:
        return "S"
    elif cms > 42:
        return "L"
    else:
        return "M"
