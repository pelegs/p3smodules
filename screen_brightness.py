# -*- coding: utf-8 -*-
"""
Displays current screen brightness.

Configuration parameters:
    empty (temp!)

Format placeholders:
    {layout} brightness (percent)

Requires:
    xkbacklight: a command-line program to retrieve and adjust current screen brightness

@author pelegs pelegs@gmail.com
@license BSD
"""

from math import ceil
import numpy as np
import time
import os.path
from subprocess import call

class color_functions():
    def rgb2hex(self, rgb):
        return '#' + ''.join(hex(c)[2:].zfill(2).upper() for c in rgb)

    def hex2rgb(self, hex_color):
        hc = hex_color[1:]
        arr = [hc[i:i+2] for i in range(0, len(hc), 2)]
        color = np.array([int(c, 16) for c in arr])
        return color

    def interpolate_gradient(self, zero_color, max_brightness_color):
        c1 = self.hex2rgb(zero_color)
        c2 = self.hex2rgb(max_brightness_color)
        return [self.rgb2hex((c1 + t*(c2-c1)).astype(int))
                for t in np.linspace(0, 1, 100)]


class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 0.5
    command = 'xbacklight'
    format = '{brightness}'
    zero_color = '#FF0000'
    max_brightness_color = '#00FF00'
    brightness = 100
    brightness_delta = 10
    button_up = 4
    button_down = 5
    brightness_up   = ['xbacklight', '-inc', str(brightness_delta)]
    brightness_down = ['xbacklight', '-dec', str(brightness_delta)]

    def post_config_hook(self):
        col_funcs = color_functions()
        self.gradient_dict = col_funcs.interpolate_gradient(
                self.zero_color, self.max_brightness_color)

    def kblayout(self):
        self.brightness = ceil(float(self.py3.command_output(self.command).strip()))
        text = '☀: ' + str(self.brightness) + '%'
        if 0 <= self.brightness <= 99:
            color = self.gradient_dict[self.brightness]
        else:
            color = self.gradient_dict[99]
        return {
            'full_text': self.py3.safe_format(self.format, {'brightness': text}),
            'color': color,
            'cached_until': self.py3.time_in(self.cache_timeout)
        }

    def on_click(self, event):
        """
        Brightness up/down.
        """
        button = event['button']
        if button == self.button_up and not self.brightness == 100:
            self.py3.command_run(self.brightness_up)
        elif button == self.button_down and not self.brightness == 0:
            self.py3.command_run(self.brightness_down)


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
