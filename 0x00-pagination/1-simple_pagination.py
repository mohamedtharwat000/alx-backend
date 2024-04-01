#!/usr/bin/env python3
"""0x00. Pagination"""

import csv
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)
        return dataset[start_idx:end_idx]


def index_range(page: int, page_size: int) -> tuple:
    """Calculates start and end indexes for pagination."""
    return ((page - 1) * page_size, page * page_size)
