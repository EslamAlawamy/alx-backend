#!/usr/bin/env python3
""" Deletion-resilient hypermedia pagination Module """

import csv
import math
from typing import List, Dict


class Server:
    """ Cass to paginate a database of popular baby names """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """ Dataset indexed by sorting position, starting in 0 """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {i: dataset[i]
                                      for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        return a dictionary with the following key-value pairs:
        index: the current start index of the return page
        next_index: the next index to query with
        page_size: the current page size
        data: the actual page of the dataset
        """
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        indexed_dataset = self.indexed_dataset()
        indexed_dataset_count = len(indexed_dataset)
        assert index < indexed_dataset_count

        next_index = index

        data = []
        for _ in range(page_size):
            while next_index not in indexed_dataset:
                next_index += 1
            data.append(indexed_dataset[next_index])
            next_index += 1
        page_size = len(data)

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
        }
