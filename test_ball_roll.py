import pytest
from ball_roll import degree

tests = (
    (1, 1, 1, 1, 13.6783597917156),
    (1, 2, 3, 4, 30.39635509270133),
    (3, 10, 5, 1, 291.8050088899328),
    (8, 4, 6, 11, 164.1403175005872),
    (5, 7, 2, 9, 845.7785804544146),
)

@pytest.mark.parametrize('a, t, r, V, expected', tests)
def test_degree(a, t, r, V: float, expected: float) -> None:
    assert degree(a, t, r, V) == expected