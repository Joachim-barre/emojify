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

@pytest.mark.parametrize(
    "expected, argument",
    [ 
        ('a', '🕡'),
        ('A', '🕁'),
        ('abcdefgh', '🕡🕢🕣🕤🕥🕦🕧🕨')
    ]
)
def test_demojify(argument : str, expected : str):
    assert(utils.demojify(argument) == expected)

@pytest.mark.parametrize(
    "expected, argument",
    [ 
        ('?', '('),
        ('A?', '🕁b'),
        ('?b??ef??', 'a🕢?d🕥🕦£*')
    ]
)
def test_demojify_invalid(argument : str, expected : str):
    assert(utils.demojify(argument) == expected)

