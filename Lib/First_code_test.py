import pandas as pd


def first_function(stringy: object) -> object:
    """
    :rtype: object
    :param stringy:
    :return: data
    """
    print(stringy)
    data = pd.DataFrame(columns=[stringy])
    return data


stringy = "Hello World"

data = first_function(stringy)
