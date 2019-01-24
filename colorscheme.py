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
    def __init__(self, hex_or_rgb, number=None, name=None):
        if Color.is_rgb(hex_or_rgb):
            self._rgb = hex_or_rgb
        elif Color.is_hex(hex_or_rgb):
            self._hex = hex_or_rgb
        else:
            raise TypeError('Expected tuple or string, got: ', type(hex_or_rgb))
        self.number = number
        self.name = name

    @staticmethod
    def is_rgb(c: Tuple[int]) -> bool:
        return bool(type(c) in (list, tuple) and len(c) == 3)

    @staticmethod
    def is_hex(c: str) -> bool:
        return bool(re.match(r'#[0-9a-eA-E]{6}', c))

    @property
    def rgb(self):
        return self._rgb or hex2rgb(self._hex)

    @property
    def hex(self):
        return self._hex or rgb2hex(self.rgb)


if __name__ == '__main__':
    pass
