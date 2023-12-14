import utils
import pytest

@pytest.mark.parametrize(
    "argument, expected",
    [ 
        ('a', '🕡'),
        ('A', '🕁'),
        ('abcdefgh', '🕡🕢🕣🕤🕥🕦🕧🕨')
    ]
)
def test_emojify(argument : str, expected : str):
    assert(utils.emojify(argument) == expected)


@pytest.mark.parametrize(
    "argument, expected",
    [ 
        ('a🔫', '🕡?'),
        ('🔚', '?'),
        ('ab📠d🕡🕢h', '🕡🕢?🕤??🕨')
    ]
)
def test_emojify_invalid(argument : str, expected : str):
    assert(utils.emojify(argument) == expected)


