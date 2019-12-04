import pytest


def test_true() -> None:
    assert True


@pytest.mark.skip("Do not run this")
def test_false() -> None:
    assert False


@pytest.mark.dicttest
def test_key() -> None:
    a = ["a", "b"]
    b = ["b"]
    assert a == b
