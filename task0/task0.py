# Митранкова Мария
# 1.

def diagonalSum(mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    result = 0
    for i in range(len(mat)):
        result += mat[i][i]
        if i != len(mat) - i - 1:
            result += mat[i][len(mat) - i - 1]

    return result

    # 2


def merge(first, second):
    f = 0
    s = 0
    out = []
    while f < len(first) and s < len(second):
        if first[f] <= second[s]:
            out.append(first[f])
            f += 1
        else:
            out.append(second[s])
            s += 1

    if f < len(first):
        for i in range(f, len(first)):
            out.append(first[i])

    if s < len(second):
        for i in range(s, len(second)):
            out.append(second[i])

    return out


# 3

def squares(s):
    l = 0
    while s[l] <= 0:
        l += 1

    lst1 = [s[i] ** 2 for i in range(l, len(s))]
    lst2 = [s[i] ** 2 for i in range(l - 1, -1, -1)]
    return merge(lst1, lst2)


# 4

def compress(elems):
    ans = ""
    l = 0
    r = 1
    while l < len(elems):
        cnt = 1
        while r < len(elems) and elems[r] == elems[l]:
            cnt += 1
            r += 1
        else:

            ans += elems[l]
            if cnt > 1:
                ans += str(cnt)
            cnt = 0
            l = r
            r += 1
    return ans