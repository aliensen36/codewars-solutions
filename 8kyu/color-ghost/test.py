import pytest
from solution import Ghost


@pytest.mark.parametrize("color", ["white", "yellow", "purple", "red"])
def test_each_color_appears(color):
    ghosts = [Ghost().color for _ in range(100)]
    assert ghosts.count(color) >= 1
