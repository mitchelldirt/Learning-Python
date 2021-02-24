def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    data_list = []
    a = 1
    sorted_data = sorted(data, key=lambda x: x['price'], reverse=True)
    for i in sorted_data:
        if a <= limit:
            data_list.append(i)
            a += 1
        else:
            break
    return data_list


# THIS IS A SOLUTION THAT I FOUND THAT IS SHORTER AND CLEARER.
# from operator import itemgetter
# def bigger_price2(limit: int, data: list) -> list:
#
#     return sorted(data, key=itemgetter('price'), reverse=True)[0:limit]


print(bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]))