import pytest
from alternative_solution import subtract_sum, fruit

# 1. Конкретные значения (пример из README + границы диапазона)
@pytest.mark.parametrize("number, expected", [
    (10, "apple"),
    (99, "apple"),
    (100, "apple"),
    (325, "apple"),
    (1000, "apple"),
])
def test_subtract_sum_known_values(number, expected):
    assert subtract_sum(number) == expected


# 2. Инвариант: результат всегда фрукт из таблицы
def test_result_always_in_table():
    allowed = set(fruit.values())
    for n in range(10, 10000):
        result = subtract_sum(n)
        assert result in allowed, f"subtract_sum({n}) = {result!r}"


# 3. Инвариант: цикл не зависает и функция возвращает строку
def test_returns_str_for_full_range():
    for n in range(10, 10000):
        assert isinstance(subtract_sum(n), str)