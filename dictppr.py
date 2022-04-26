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
