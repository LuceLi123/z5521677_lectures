""" yf_example3.py
 It is created to download stock data of Qantas"""
import os
import toolkit_config as cfg
import yf_example2


def qan_prc_to_csv(year):
    """ Download stock price data from Yahoo Finance and save in the csv file
    Parameter
    -----
    year: int
        year for download (YYYY)
    """
    tic = 'QAN.AX'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    df = yf_example2.yf_prc_to_csv(tic=tic, pth=pth, start=f'{year}-01-01', end=f'{year}-12-31')

if __name__ == "__main__":
    year = 2020
    qan_prc_to_csv(2020)
