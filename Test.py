""" yf_example2.py

Example of a function to download stock prices from Yahoo Finance.
"""


def yf_prc_to_csv(tic, pth, start=None, end=None):
    """ Downloads analysts recommendation from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)

    # Example
import yfinance as yf
tic = 'QAN.AX'
pth = 'qan_stk_prc.csv'
yf_prc_to_csv(tic, pth)


if __name__ == "__main__":
    ## datadir = 'E:\\Program Files\\PycharmProjects\\toolkit\\Week Lecture'
    import os
    datadir = r'E:\Program Files\PycharmProjects\toolkit\Week Lecture'
    pth = os.path.join(datadir, 'qan_stk_prc.csv')
    yf_prc_to_csv(tic,pth)

PRJDIR = 'E:\Program Files\PycharmProjects\toolkit\Week Lecture'

from Lectures.config import APIKEY
print(APIKEY)  # Print 123

from config import APIKEY
print(APIKEY)  # Print 123

import config as cfg
print(cfg.APIKEY)  # Print 123

from Lectures import config as cfg
print(cfg.APIKEY)  # Print Nothing since utils is not a module name, but a package name


def my_function(y):
    y = y + x
    x = 2
    y = y + x
    return y

x = 3
y = 10
y = my_function(x)
# Error since cannot access local variable 'x'\
# where it is not associated with a value
