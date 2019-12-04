import pytest


def test_true() -> None:
    assert True


@pytest.mark.skip("Do not run this")
def test_false() -> None:
    assert False


@pytest.mark.fun_with_expr_or
def test_marker_expr_or() -> None:
    assert 1 == 1


@pytest.mark.fun_with_expr_and
def test_marker_expr_and() -> None:
    assert 1 == 1


@pytest.mark.dicttest
def test_key() -> None:
    a = ["a", "b"]
    b = ["b"]
    assert a == b
