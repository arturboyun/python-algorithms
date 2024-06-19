def boyer_moore(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if n < m:
        return -1

    last = {}
    for i, c in enumerate(pattern):
        last[c] = i

    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            i -= 1
            k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1

    return -1