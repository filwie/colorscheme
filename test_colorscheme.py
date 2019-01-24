import pytest

import colorscheme


@pytest.mark.parametrize('test_input', [
    [123, 123, 123],
    (123, 123, 123),
    '#123123',
])
def test_color_init_correct(test_input):
    assert colorscheme.Color(test_input)


@pytest.mark.parametrize('test_input', [
    (123, 123, 123, 321),
    '#KEKEKE',
    '123123',
    None,
])
def test_color_init_incorrect(test_input):
    with pytest.raises(TypeError):
        colorscheme.Color(test_input)
