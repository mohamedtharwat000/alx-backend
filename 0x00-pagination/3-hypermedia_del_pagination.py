#!/usr/bin/env python3
"""0x00. Pagination"""


import csv
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None, page_size: int = 10) -> Dict:
        """Returns a dictionary with pagination information based on index."""
        dataset = self.indexed_dataset()

        if index is None:
            index = 0
        else:
            assert isinstance(index, int) and index >= 0
            assert index < len(dataset)

        start_idx = index
        end_idx = min(index + page_size, len(dataset))
        next_index = end_idx

        return {
            "index": start_idx,
            "next_index": next_index,
            "page_size": page_size,
            "data": [dataset[i] for i in range(start_idx, end_idx)]
        }
