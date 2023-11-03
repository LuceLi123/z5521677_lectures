
import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
# Attribute - value associate with an object which is referenced by name using the dot notation
# Method: A function inside a class

df.to_csv('qan_stk_prc.csv')

# Use to delete invalid variable and debug
str = 5
str(5) # become invalid callable
del(str)

# Search in Built-in FUnction

# upper function does not exist, need to first go to the main folder, and then to the sub folder
x = str('abc')
xup = str.upper(x)
print(xup)


