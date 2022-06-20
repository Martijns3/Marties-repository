from main import get_none
from main import flatten_dict


def test_get_none():
    assert get_none() == None


def test_flatten_dict():
    assert (
        type(
            flatten_dict(
                {"a": {"inner_a": {"inner_inner_f": 34}, "inner_b": 350}, "b": 3.14}
            )
        )
        == list
    )
