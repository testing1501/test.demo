def unpack_list(var):
    first, *middle, last = var
    avg = sum(middle)/len(middle)
    print(avg)

unpack_list([33, 22, 11, 1, 101, 21, 70])