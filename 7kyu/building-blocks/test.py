import pytest
from solution import Block


# ---------- Фикстуры ----------

@pytest.fixture
def block():
    """Блок 2×4×6 из примера в условии."""
    return Block([2, 4, 6])


@pytest.fixture
def cube():
    """Куб 3×3×3 — удобен для проверки формул."""
    return Block([3, 3, 3])


# ---------- Конструктор и геттеры ----------

def test_constructor_unpacks_dimensions(block):
    assert block.width == 2
    assert block.length == 4
    assert block.height == 6


def test_get_width(block):
    assert block.get_width() == 2


def test_get_length(block):
    assert block.get_length() == 4


def test_get_height(block):
    assert block.get_height() == 6


# ---------- Вычисления ----------

def test_get_volume_from_example(block):
    assert block.get_volume() == 48


def test_get_surface_area_from_example(block):
    assert block.get_surface_area() == 88


def test_volume_of_cube(cube):
    assert cube.get_volume() == 27


def test_surface_area_of_cube(cube):
    # 6 граней по 9
    assert cube.get_surface_area() == 54


# ---------- Граничные и особые случаи ----------

def test_unit_block():
    b = Block([1, 1, 1])
    assert b.get_volume() == 1
    assert b.get_surface_area() == 6


def test_zero_dimension():
    """Нулевой размер даёт нулевой объём и площадь (проверки ошибок в кате нет)."""
    b = Block([0, 5, 10])
    assert b.get_volume() == 0
    assert b.get_surface_area() == 100  # 2*(0 + 50 + 0)


def test_large_numbers():
    b = Block([10, 21, 33])
    assert b.get_volume() == 6930
    assert b.get_surface_area() == 2466


def test_symmetric_dimensions():
    """Перестановка измерений не меняет объём и площадь."""
    a = Block([2, 3, 4])
    b = Block([4, 2, 3])
    assert a.get_volume() == b.get_volume()
    assert a.get_surface_area() == b.get_surface_area()


# ---------- Параметризация: одна проверка — много данных ----------

@pytest.mark.parametrize(
    "dims, expected_volume, expected_area",
    [
        ([2, 4, 6], 48, 88),
        ([1, 1, 1], 1, 6),
        ([3, 3, 3], 27, 54),
        ([10, 21, 33], 6930, 2466),
        ([0, 5, 10], 0, 100),
        ([1, 2, 3], 6, 22),   # 2*(2+6+3) = 22
    ],
)
def test_volume_and_area_parametrized(dims, expected_volume, expected_area):
    b = Block(dims)
    assert b.get_volume() == expected_volume
    assert b.get_surface_area() == expected_area