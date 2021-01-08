""" Question 2 doesnt have an example but here's my interpretation:
    input a = 4
    process is 4+44+444+4444
    output 4936."""


def digit_multp(t, v):
    b = 1
    v = str(v)
    p = v
    while b < t:
        p += v
        b += 1
    return int(p)


def incr_n(n):
    n_n = 0
    for x in range(1, n+1):
        n_n += digit_multp(x, n)
    return n_n


a = int(input())
print(incr_n(a))
