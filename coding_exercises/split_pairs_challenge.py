def split_pairs(a):
    x = [a[i:i + 2] for i in range(0, len(a), 2)]
    last_index = x[-1]
    if len(last_index) < 2:
        x.remove(last_index)
        x.append(last_index + "_")
    return x

print(split_pairs("abcdefg"))