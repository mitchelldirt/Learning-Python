def func(p1, p2, *args, k, **kwargs):
    """
    This is an example of how different parameter types work.
    :param p1: 1
    :param p2: 2
    :param args: 3, 4, 5, 9
    :param k: 6
    :param kwargs: Key1, Key2, Key3
    :return: Outputs the inputs
    """
    print("positional-or-keyword:.....{}, {}".format(p1, p2))
    print("var-positional (*args):... {}".format(args))
    print("keyword:...................{}".format(k))
    print("var-keyword:...............{}".format(kwargs))


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8, key3="Hello")
