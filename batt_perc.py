# -*- coding: utf-8 -*-
"""
Displays battery info

Configuration parameters:
    empty (temp!)

@author pelegs pelegs@gmail.com
@license BSD
"""

import numpy as np
import time
import os.path
from subprocess import check_output
from time import gmtime, strftime
import re


class ColorFunctions():
    def rgb2hex(self, rgb):
        return '#' + ''.join(hex(c)[2:].zfill(2).upper() for c in rgb)

    def hex2rgb(self, hex_color):
        hc = hex_color[1:]
        arr = [hc[i:i+2] for i in range(0, len(hc), 2)]
        color = np.array([int(c, 16) for c in arr])
        return color

    def interpolate_gradient(self, min_col, max_col):
        c1 = self.hex2rgb(min_col)
        c2 = self.hex2rgb(max_col)
        return [self.rgb2hex((c1 + t*(c2-c1)).astype(int))
                for t in np.linspace(0, 1, 101)]


class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 1
    cmd = ['acpi']
    backend = ColorFunctions()
    gradient_dict = backend.interpolate_gradient('#FF0000', '#00FF00')
    status_dict = {'Charging': 'CHR',
                   'Discharging': 'BAT',
                   'Full': 'FULL'}

    def battery_check(self):
        # Main battery check command (from command line)
        check = check_output(self.cmd).decode('utf-8')

        # Status
        m_status = re.search('Battery 0: ([A-Za-z\-0-9]+),', check)
        if m_status:
            try:
                status = self.status_dict[m_status.group(1)]
            except KeyError:
                status = '<->'
        else:
            status = 'N/A'

        # Percentage
        m_perc = re.search('(\d+)%', check)
        if m_perc:
            perc = int(m_perc.group(1))
        else:
            perc = ''

        # Time
        m_time = re.search('\d\d:\d\d:\d\d', check)
        if m_time:
            time_text = m_time.group(0)
        else:
            time_text = ''

        # Construct text
        text = '{}: {}% ({})'.format(status, perc, time_text)
        # Color
        color = self.gradient_dict[perc]

        # Return
        return {
                'full_text': text,
                'color': color,
                'cached_until': self.py3.time_in(self.cache_timeout)
                }


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
