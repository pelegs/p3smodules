# -*- coding: utf-8 -*-
"""
Display current keyboard layout.

Configuration parameters:
    empty (temp!)

Format placeholders:
    {layout} current layout

Requires:
    xkblaout-state: a command-line program to retrieve current layout

@author pelegs pelegs@gmail.com
@license BSD
"""


import time
import os.path


class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 0.5
    command = 'xkblayout-state print "%s"'
    format = '{layout}'

    def kblayout(self):
        layout = self.py3.command_output(self.command).strip()
        color_dict = {'us': self.py3.COLOR_US,
                      'il': self.py3.COLOR_IL,
                      'de': self.py3.COLOR_DE}
        language = {'us': 'en',
                    'il': 'he',
                    'de': 'de'}
        color = color_dict[layout]
        return {
            'color': color,
            'full_text': self.py3.safe_format(self.format, {'layout': language[layout]}),
            'cached_until': self.py3.time_in(self.cache_timeout)
        }

if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
