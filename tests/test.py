import main
import pytest

def test_emojify():
    assert(main.emojify('a') == '🕡')
    assert(main.emojify('A') == '🕁')
    assert(main.emojify('abcdefgh') == '🕡🕢🕣🕥🕦🕧🕨')

