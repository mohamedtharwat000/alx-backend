#!/usr/bin/env python3
"""0x00. Pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """index_range"""
    return ((page - 1) * page_size, page * page_size)
