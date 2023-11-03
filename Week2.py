
# Quotation: can use single, double, triple quotation

# 2 ways for format
a = True
b = 5
print(f"The value of a is {a}. and the value of b is {b}")
print(f'The value of a is {a} and the value of b is {b}')
print('The value of a is {} and the value of b is {}'.format(a,b))

# Scientific Notation is permissible
x = 1e6 # x = 1 million
y = 2/4 # Process Casting, conversion from division of integer to floating number

# Check Type
y = type(x)
print(y)

# Upper & Lower Case
w = "What"
i = "IS"
c = "CamelCase?"
print('{} {} {}'.format(w,i.lower(),c))

asx_value = 7111.4
date = '2021-01-25'
units = 1
currency = 'AUD'
print("The closing value of {} unit of the All\
 Ordinaries on {} was {} {}".format(units,date,asx_value,currency))

# Strip function
# str.strip()

# ' some text '.strip Not work since it only states the build in method
' some text '.strip()
' some text '.strip(None)
' some text '.strip(' ')

# Into Modules and Packages: Downloads Qantas share price beginning 1 January 2020
import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
# df = yfinance.download(tic, start, None)
print(df)
df.to_csv('qan_stk_prc.csv')

import yfinance as df
df.download("QAN.AX", '2020-01-01', None).to_csv('qan_stk_prc.csv')

# Json library
import json
help(json.load)

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(l[2:10])
print(l[-9:-6])

t = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[:-5])
print(t[:5])

t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[-7:12])
print(t[2:10])

# Equivalent Python Value Assignment
b, s, i = True, 'string', 1
b, s, i = (True, 'string', 1)
(b, s, i) = (True, 'string', 1)
(b, s, i) = True, 'string', 1

## List
lst_a = ['a']
lst_b = ['b', lst_a]
print(lst_b)
lst_c = ['b', ['a']]
lst_c[1]
lst_b[1]
lst_b[1].append("c")
lst_c[1].append("c")

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
f_suburbs.remove("Randwick")
print(f_suburbs)
f_suburbs.add("Fairfield", "Fairfield East", "Fairfield Heights", "Fairfield West", \
                 "Fairlight", "Fiddletown", "Five Dock", "Forest Glen", "Forest Lodge", \
                 "Forestville", "Freemans Reach", "Freshwater")


## Tuple
current = 21
last = 13
Fibonacci_Seq = (last, current, last+current)
(omitted,last,current) = Fibonacci_Seq
print(f"the value of 'last' is {last}, and the value of 'current' is {current}")
## Dictionaries

dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
print(dic1)
print(dic0[0])

dic = { ['a', 'b']: 1, 'c': 2,} # Not valid
dic = { ('a', 'b'): 1, 'c': 2, } # Valid

tup = (1, 2, ['a', 'b'])
tup = (1, 2, ('a', 'b'))
dic = {tup: 'value'}

print(l[2:4])
t = ('a','b','c','d','e')
print(t[2:4])

b = 'problem'
a = 'this is called'
a = f'{a} Parsons {b}'
b = print
b(a)

f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop("Randwick")
f_suburbs.pop("Kensington")
f_suburbs["Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Flemington"] = None
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Frenchs Forest"] = 13473
f_suburbs["Freshwater"] = 8866
print(f_suburbs)

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
f_suburbs.remove("Randwick")
f_suburbs.remove("Kensington")

f_suburbs.add("Fairfield")
f_suburbs.add("Fairfield East")
f_suburbs.add("Fairfield Heights")
f_suburbs.add("Fairfield West")
f_suburbs.add("Fairlight")
f_suburbs.add("Fiddletown")
f_suburbs.add("Five Dock")
f_suburbs.add("Flemington")
f_suburbs.add("Forest Glen")
f_suburbs.add("Forest Lodge")
f_suburbs.add("Forestville")
f_suburbs.add("Freemans Reach")
f_suburbs.add("Frenchs Forest")
f_suburbs.add("Freshwater")

print(f"The value of 'f_suburbs' is {f_suburbs}.")