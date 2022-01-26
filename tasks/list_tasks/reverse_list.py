"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернут развернутый список
"""


def reverse_list(collection: list) -> list:
    collection.reverse()
    return collection


if __name__ == '__main__':
    assert [1, 2, 3] == reverse_list([3, 2, 1])
    print('Решено!')
