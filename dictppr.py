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
