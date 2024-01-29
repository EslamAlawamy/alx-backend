#!/usr/bin/env python3
""" Hypermedia Module """
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    next_page: int = page * page_size
    prev_page: int = next_page - page_size
    return (prev_page, next_page)


class Server:
    """ Class to paginate a database of popular baby names """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialize """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get the page list using page num and page_size """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        (start, end) = index_range(page, page_size)

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ get the page list using page num and page_size """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        (start, end) = index_range(page, page_size)
        data_set = self.dataset()
        data = data_set[start:end]

        total_pages = math.ceil(len(data_set) / page_size)
        page_size = len(data)
        next_page = None if page + 1 > total_pages else page + 1
        prev_page = None if page - 1 == 0 else page - 1
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
