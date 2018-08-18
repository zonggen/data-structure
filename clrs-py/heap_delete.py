'''
    CLRS 6.5-8
    A1Q3:
    Running time: O(log(n))
    References:
        heapq - https://github.com/python/cpython/blob/master/Lib/heapq.py
'''

# importing "heapq" to implement heap queue
import heapq

def HeapDelete(A, i):
    if (len(A) <= i):
        raise Exception("Heap does not have ith element.")
    # Exchange i with last element and trim the list
    last = A[len(A) - 1]
    A[i] = A[last]
    A = A[:(len(A) - 1)]
    if A[i] < last:
        # Bubble up the ith element
        heapq._siftdown_max(A, 0, i)
    else:
        # Bubble down the ith element
        heapq._siftup_max_(A, i)
    
