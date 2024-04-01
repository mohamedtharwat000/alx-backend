#!/usr/bin/env python3
"""0x00. Pagination"""


import csv
from typing import List, Optional


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
        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size, len(dataset))
        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary with pagination information."""
        dataset_page = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size + \
            (1 if len(self.dataset()) % page_size > 0 else 0)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

    def get_hyper_index(self, index: Optional[int] = None, page_size: int = 10) -> dict:
        """Returns a dictionary with pagination information based on index."""
        dataset = self.dataset()

        if index is None:
            index = 0
        else:
            assert isinstance(index, int) and index >= 0
            assert index <= len(dataset)

        start_idx = index
        end_idx = min(index + page_size, len(dataset))
        next_index = end_idx

        return {
            "index": start_idx,
            "next_index": next_index,
            "page_size": page_size,
            "data": dataset[start_idx:end_idx]
        }


def index_range(page: int, page_size: int, dataset_length: int) -> tuple:
    """Calculates start and end indexes for pagination."""
    start_idx = (page - 1) * page_size
    end_idx = min(start_idx + page_size, dataset_length)
    return start_idx, end_idx
