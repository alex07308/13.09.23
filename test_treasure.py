import pytest
from treasure  import get_path
test_data = (
    (
        [['x', 0],
        [0, 't'],]
        {'E':1, 'S':1}
    ),
    (
        [[0, 0, 't'],
        [0, 0, 0],
        ['x', 0, 0],]
        {'E':2, 'N':2}
    ),
    (
        [[0, 0, 0, 'x'],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        ['t', 0, 0, 0],]
        {'W':3, 'S':3}
    ),
    (
        [['t', 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 'x'],]
        {'W':4, 'N':4}
    )
)
@pytest.mark.parametrize('map, expected', test_data)
def test_gwr_path(map: list, expected: dict) -> None:
    path = get_path(map)
    valid_path = True

    for key, value in expected.items():
        if path.count(key) != value:
            valid_path = False
            break

    assert valid_path and (set(path) == set(expected.keys()))

    #valid_path = all([path.count(key) == value for key, value in expected.items()])