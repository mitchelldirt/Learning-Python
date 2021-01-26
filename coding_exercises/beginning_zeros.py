def beginning_zeros(number: str) -> int:
    x = []
    for quantity in number[::1]:
        if quantity == '0':
            x.append(quantity)
        else:
            break
    return int(len(x))


print(type(beginning_zeros('001')))
