import pytest
from solution import lovefunc

@pytest.mark.parametrize("a, b, expected", [
    (2, 4, False),   # чёт + чёт
    (3, 5, False),   # нечёт + нечёт
    (2, 3, True),    # чёт + нечёт
    (3, 2, True),    # нечёт + чёт (другой порядок)
    (0, 1, True),    # граница: ноль чётный
    (0, 0, False),   # граница: два нуля
    (1, 1, False),   # граница: две единицы
    (2999, 3000, True),  # большие числа
])
def test_lovefunc(a, b, expected):
    assert lovefunc(a, b) is expected
