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


@pytest.mark.parametrize('test_input, expected', [
    ([123, 123, 123], True),
    ((12, 12, 12), True),
    ('#123123', False),
    ('#eee123', False),
])
def test_is_rgb(test_input, expected):
    assert colorscheme.Color.is_rgb(test_input) is expected


@pytest.mark.parametrize('test_input, expected', [
    ([123, 123, 123], False),
    ((12, 12, 12), False),
    ('#123123', True),
    ('#eee123', True),
])
def test_is_hex(test_input, expected):
    assert colorscheme.Color.is_hex(test_input) is expected


@pytest.mark.parametrize('test_input, expected', [
    ((123, 123, 123), (123, 123, 123)),
    ((12, 12, 12), (12, 12, 12)),
    ('#123123', (18, 49, 35)),
    ('#eee123', (238, 225, 35)),
])
def test_conversion_to_rgb(test_input, expected):
    assert colorscheme.Color(test_input).rgb == expected


@pytest.mark.parametrize('test_input, expected', [
    ((123, 123, 123), '#7b7b7b'),
    ((12, 12, 12), '#0c0c0c'),
    ('#123123', '#123123'),
    ('#eee123', '#eee123'),
])
def test_conversion_to_hex(test_input, expected):
    assert colorscheme.Color(test_input).hex == expected
