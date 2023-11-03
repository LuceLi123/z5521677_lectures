import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end, ignore_tz=True)
print(df)
df.to.cxv('qan_prc_2020.csv')