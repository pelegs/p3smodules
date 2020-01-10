import numpy as np

class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 0.5
    format = '{random}'

    def random(self):
        number = np.random.randint(0, 0xFFFFFF)
        color = '#{}'.format(hex(number)[2:]).upper()
        return {
            'color': color,
            'full_text': self.py3.safe_format(self.format, {'random': color}),
            'cached_until': self.py3.time_in(self.cache_timeout)
        }

if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
