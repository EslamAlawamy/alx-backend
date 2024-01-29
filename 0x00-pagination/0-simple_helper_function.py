#!/usr/bin/env python3
""" Simple helper function Module """


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    next_page: int = page * page_size
    prev_page: int = next_page - page_size
    return (prev_page, next_page)
