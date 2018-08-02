'''
    part (d)
'''

def MergeSortWithInversion (A, p, r):
    count = 0
    if (p < r):
        q = (p + r)/2
        count += MergeSortWithInversion(A, p, q)
        count += MergeSortWithInversion(A, q+1, r)
        count += MergeWithInversion(A, p, q, r)
    return count

def MergeWithInversion (A, p, q, r):
    count = 0
    n1, n2 = q - p + 1, r - q
    L, R = A[p: q+1], A[q+1: r]
    i, j = 1, 1
    for k in range (p, r):
        if l[i] <= r[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            count += n1 - i + 1
    return count
