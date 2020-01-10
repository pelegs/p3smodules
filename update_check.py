# -*- coding: utf-8 -*-
"""
Check for updates in the ubuntu repository

Configuration parameters:
    empty (temp!)

@author pelegs pelegs@gmail.com
@license BSD
"""

from math import ceil
import numpy as np
import time
import os.path
from subprocess import check_output


class updater:
    def setup(self):
        self.foo = 1

    def perform_update(self):
        #cmd = 'i3 restart'
        #self.run_cmd(cmd)
        pass

    def run_cmd(self, cmd):
        return self.parent.py3.command_run(cmd)


class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 3600
    command = ['apt', 'list', '--upgradable']
    no_upgrades_color = '#993300'
    upgrades_available_color = '#00FF00'
    mouse_click = 1
    backend = updater()

    def update_check(self):
        check = check_output(self.command)
        if check != b'Listing...\n':
            text = '!'
            color = self.upgrades_available_color
        else:
            text = '-'
            color = self.no_upgrades_color

        return {
            'full_text': 'u: {}'.format(text),
            'color': color,
            'cached_until': self.py3.time_in(self.cache_timeout)
        }

    def on_click(self, event):
        """
        Perform update
        """
        button = event['button']
        # update
        if button == self.mouse_click:
            self.backend.perform_update()


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
