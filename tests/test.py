import main
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
    assert(main.emojify(argument) == expected)

