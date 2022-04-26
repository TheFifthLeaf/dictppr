def _check_nesting(items: list) -> int:
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
            count += _check_nesting(item)
    return count


def _get_new(item: any) -> any:
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
        item = _flatten(item)
        item = _get_new(item)
        if isinstance(item, list) and len(keys) > 1:
            if not _check_nesting(item):
                item = map(lambda k, i: f"{k}:{i}", keys, item)
                item = map(lambda i: i.replace("'", ""), item)
                item = list(item)
    elif isinstance(item, list):
        if _check_nesting(item):
            item = _flatten(item)
    return item


def _flatten(item: list | dict) -> list | dict:
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
        _flattened = ""
    elif length == 1:
        if isinstance(item, list):
            _flattened = item[0]
        elif isinstance(item, dict):
            _flattened = list(item.values())[0]
    elif length > 1:
        if isinstance(item, list):
            _flattened = [_get_new(elem) for elem in item]
        elif isinstance(item, dict):
            _flattened = list(item.values())
    return _flattened


def _to_string(item: any) -> str:
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


def dictppr(dictionary: dict) -> dict:
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
    dictionary = {key: _get_new(val) for key, val in dictionary.items()}
    dictionary = {key: _to_string(val) for key, val in dictionary.items()}
    return dictionary
