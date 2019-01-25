#!/usr/bin/env python3
import json
from pathlib import Path
import re
from typing import Tuple


from addict import Dict as DotDict
from colr import color, hex2rgb, rgb2hex

SCRIPT_PATH = Path(__file__)
COLORSCHEMES_DIR = SCRIPT_PATH.parent / 'colorschemes'


class Color(object):
    def __init__(self, hex_or_rgb):
        self._rgb, self._hex = None, None
        if Color.is_rgb(hex_or_rgb):
            self._rgb = hex_or_rgb
        elif Color.is_hex(hex_or_rgb):
            self._hex = hex_or_rgb
        else:
            raise TypeError('Expected tuple or string, got: ', type(hex_or_rgb))

    @staticmethod
    def is_rgb(c: Tuple[int]) -> bool:
        if any(isinstance(c, t) for t in (tuple, list)):
            if len(c) == 3:
                return all(0 < f < 255 for f in c)
        return False

    @staticmethod
    def is_hex(c: str) -> bool:
        if isinstance(c, str):
            return bool(re.match(r'#[0-9a-eA-E]{6}', str(c)))
        return False

    @property
    def rgb(self):
        return self._rgb or hex2rgb(self._hex)

    @property
    def hex(self):
        return self._hex or f'#{rgb2hex(*self._rgb)}'


if __name__ == '__main__':
    pass
