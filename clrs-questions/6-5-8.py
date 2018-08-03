'''
    Problem 6.5-8:
    Running time: O(log(n))
'''

def HeapDelete(A,i):
    if (len(A) < i):
        print("Heap does not have i'th item.")
    last = A[len(A)-1]
    
