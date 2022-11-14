# title Merge two sorted arrays
# description На входе есть два отсортированных массива в неубывающем порядке, объединить эти два массива в один отсортированный в неубывающем порядке
#<!---end--->
def merge(left, right):
    len_left = len(left)
    len_right = len(right)
    result = [0] * (len_left + len_right)
    pA = pB = pC = 0

    while pA != len_left and pB != len_right:

        if left[pA] <= right[pB]:
            result[pC] = left[pA]
            pC += 1
            pA += 1
        else:
            result[pC] = right[pB]
            pC += 1
            pB += 1

    while pA != len_left:
        result[pC] = left[pA]
        pC += 1
        pA += 1

    while pB != len_right:
        result[pC] = right[pB]
        pC += 1
        pB += 1

    return