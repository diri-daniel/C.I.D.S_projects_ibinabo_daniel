def num_dict_gen():
    num_dict = {x: pow(x, 2) for x in range(1, 21)}
    num_dict_keys = [x for x in num_dict.keys()]
    print(num_dict_keys)


num_dict_gen()
