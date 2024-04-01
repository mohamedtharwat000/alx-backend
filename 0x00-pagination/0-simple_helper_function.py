#!/usr/bin/env python3
"""docs"""


def index_range(page: int, page_size: int) -> tuple:
    """docs"""
    return ((page - 1) * page_size, page * page_size)
