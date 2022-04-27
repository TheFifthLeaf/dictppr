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
    nests = 0
    for item in items:
        if isinstance(item, dict):
            nests += 1
        if isinstance(item, list):
            nests += check_nesting(item)
    return nests


def check_item(item: any) -> any:
    """
    Checks whether the given item
    is as flattened as possible.

    Parameters
    ----------
    item
        Item to be checked.

    Returns
    ----------
    Ensured item.
    """
    if isinstance(item, dict):
        keys = list(item.keys())
        item = flattener(item)
        item = check_item(item)
        if isinstance(item, list) and len(keys) > 1:
            if not check_nesting(item):
                item = map(lambda k, i: f"{k}:{i}", keys, item)
                item = map(lambda i: i.replace("'", ""), item)
                item = list(item)
    elif isinstance(item, list):
        if check_nesting(item):
            item = flattener(item)
    return item


def flattener(item: any) -> any:
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
            flattened = [check_item(elem) for elem in item]
        elif isinstance(item, dict):
            flattened = list(item.values())
    return flattened


def string(item: any) -> str:
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


def dictppr(dictionary: dict) -> str:
    """
    Flattens nested dictionaries.

    Parameters
    ----------
    dictionary
        A nested dictionary.

    Returns
    ----------
    A flattened dictionary.
    """
    dictionary = {key: check_item(val) for key, val in dictionary.items()}
    dictionary = {key: string(val) for key, val in dictionary.items()}
    result = check_item(dictionary)
    result = string(result)
    return result
