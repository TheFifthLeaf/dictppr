def check_nesting(items: list) -> int:
    """
    Checks how many nests are left.

    Parameters
    ----------
    items
        List of items to be checked.

    Returns
    ----------
    The number of nests remaining.
    """
    count = 0
    for item in items:
        if isinstance(item, dict):
            count += 1
        if isinstance(item, list):
            count += check_nesting(item)
    return count


def get_new(item: any) -> any:
    """
    Checks whether the given item
    is as flattened as possible.

    Parameters
    ----------
    item
        Item to be checked.

    Returns
    ----------
    New item.
    """
    if isinstance(item, dict):
        keys = list(item.keys())
        item = flatten(item)
        item = get_new(item)
        if isinstance(item, list) and len(keys) > 1:
            if not check_nesting(item):
                item = map(lambda k, i: f"{k}:{i}", keys, item)
                item = map(lambda i: i.replace("'", ""), item)
                item = list(item)
    elif isinstance(item, list):
        if check_nesting(item):
            item = flatten(item)
    return item


def flatten(item: list | dict) -> list | dict:
    """
    Flattens the given item.

    Parameters
    ----------
    item
        The item to be flattened.

    Returns
    ----------
    A flattened item.
    """
    length = len(item)
    if length == 0:
        flattened = ""
    elif length == 1:
        if isinstance(item, list):
            flattened = item[0]
        elif isinstance(item, dict):
            flattened = list(item.values())[0]
    elif length > 1:
        if isinstance(item, list):
            flattened = [get_new(elem) for elem in item]
        elif isinstance(item, dict):
            flattened = list(item.values())
    return flattened


def to_string(item: any) -> str:
    """
    Converts the given item to a string.

    Parameters
    ----------
    item
        The item to be converted.

    Returns
    ----------
    A converted item.
    """
    if isinstance(item, list):
        item = ", ".join(map(lambda i: str(i), item))
    else:
        item = str(item)
    return item
