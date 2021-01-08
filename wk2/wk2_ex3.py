def val_list(st):
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


def stat_calc():
    print("Menu")
    print("\n  1. Mean")
    print("  2. Mode")
    print("  3. Median")
    print("  4. Variance\n")

    cont = 'y'

    while cont != 'N' and cont != 'n':
        choice = int(input("Please make a choice:? "))
        amt = int(input("Please enter the amount of values you wish to calculate: "))
        val = input("please enter the values separated by commas:")
        val = val_list(val)
        val = [int(a) for a in val]

        if choice == 1:
            print(f'The mean is {mean(amt, val)}.\n')

        if choice == 2:
            print(f'The mode is {mode(amt, val)}.\n')

        if choice == 3:
            print(f'The median is {median(amt, val)}.\n')

        if choice == 4:
            print(f'The variance is {variance(amt, val, mean(amt, val))}.\n')

        cont = input("Do you wish to continue?(y/n): ")
        print('\n')


def mean(x, y):
    return sum(y)/x


def mode(x, y):
    a = 0
    y = sorted(y)
    val_ct = 0
    v_val = []
    mode_val = []
    while a < x:
        val = y[a]
        for b in y:
            if val == b:
                val_ct += 1
        v_val.append(int(val_ct))
        val_ct = 0
        a += 1
    for b in range(len(v_val)):
        if v_val[b] == max(v_val):
            mode_val.append(int(y[b]))

    return mode_val


def median(x, y):
    y = sorted(y)
    if x % 2 == 0:
        return (y[int((x/2) - 1)] + y[int(x/2)])/2
    else:
        return y[int(x/2)]


def variance(x, y, m):
    sq_diff = []
    for a in y:
        diff = a-m
        sq_diff.append(pow(diff, 2))
    sum_sq_diff = sum(sq_diff)
    return sum_sq_diff/(x-1)


stat_calc()
