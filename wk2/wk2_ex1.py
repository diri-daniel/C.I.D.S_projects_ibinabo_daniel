def string_split(st):
    n_st = []
    word = ""
    x = 0
    while x < len(st):
        ch = st[x]
        while ch != ',' and ch != ' ':
            word += ch
            if x < len(st) - 1:
                x += 1
                ch = st[x]
            else:
                break
        n_st.append(word)
        word = ""
        x += 1
    return n_st


n = input()
n = string_split(n)
n = sorted(n)
print(*n, sep=',')
