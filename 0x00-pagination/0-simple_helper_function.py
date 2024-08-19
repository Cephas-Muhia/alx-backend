#!/usr/bin/env python3
'''
    Simple helper function.
'''


def index_range(page, page_size):
    '''
        Returns the range of indexes for a given page.
    '''
    start = (page - 1) * page_size
    end = page * page_size
    '''
    In Python, when you slice a list using list[start:end], it includes the element at start but ex    cludes the element at end. So, list[10:20] will include the elements from index 10 to 19.
    '''
    return start, end
    

