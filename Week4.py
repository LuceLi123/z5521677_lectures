## Create a function
def mk_csv_name(tic):
    tic = tic.lower()
    tic_base = tic.split('.')[0]
    csv_name = f'{tic_base}_stk_prc.csv'
    return csv_name  # what this function will produce as a result

def qan_tic():  # (1)
    # tic = "QAN.AX"  # (2) Here tic is a local namespace
    print(tic)  # (3)
    return tic  # return function is not compulsory
tic = "WES.AX"
qan_tic()  # Need to call a function then it can be executed
print(qan_tic)   # Only print the object of function instance
print(tic)   # Error of tic is not defined

res = qan_tic()
print(res) # Print QAN.AX twice

def qan_tic():
    tic = "QAN.AX" # Prior for local namespace
    print(tic)
    return tic
tic = "WES.AX" # Remove will cause error
print(tic)
qan_tic()

def mk_csv_name(tic, show = True)
    tic = tic.lower()

tic = 'QAN.AX'                        #                       (1)
tic = tic.lower()                     # --> 'qan.ax'          (2)
tic_base = tic.split('.')[0]          # --> 'qan'             (3)
csv_name = f'{tic_base}_stk_prc.csv'  # --> 'qan_stk_prc.csv' (4)
print(csv_name)

l = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
def evenfun(l):
    evennum = []
     for n in l:
        if n % 2 == 0:
            evennum.append(n)
        return evennum
print(evenfun(l))


evens = [] # execute faster

# Comprehension for lists, Dict & Sets
pairs = [
    ('a',1),
    ('b',2),
    ('c',3)
]
dic = {key:value for key, value in pairs}  # More concise and direct way

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
square = [x**2 for x in lst if x**2 > 150]

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
result = list({x for x in numbers if x % 2 == 0})

# Alternative choice
result = [i for i in set(numbers) if i % 2 == 0]
result.sort()
print(result)

## Working with Modules

# Change the directory path
def my_function(x):
    x = x + 1
    return x

x = 3
# my_function(x)
x = my_function(x)

def my_function(y):
    y = y + x
    x = 2
    y = y + x
    return y

x = 3
y = 10
y = my_function(x)

def process_string(s):
    spt = s.split()
    process_spt = [spt.lower() for spt in spt]
    return process_spt

def process_string(s):
    spt = s.split()
    process_spt = [spt.lower() if index % 2 == 0 else spt.upper() for index, spt in enumerate(spt) ]
    return process_spt

print(process_string("This is my test String"))

def fizz_buzz_sumz(i):
    sumi = sum([3 * x if (x % 3 == 0 and x % 5 != 0) else\
                5 * x if (x % 3 != 0 and x % 5 == 0) else\
                0 if (x % 3 == 0 and x % 5 == 0) else x for x in range(0, i+1)])
    return sumi

print(fizz_buzz_sumz(10))

prc_dic = {
    '3000-01-15': 7.0400, '2020-01-14': 7.1100, '2020-01-13': 7.0200,
    '2020-01-02': 7.1600, '2020-01-03': 7.1900, '2020-01-06': 7.0000,
    '2020-01-07': 7.1000, '2020-01-08': 6.8600,
    '2020-01-09': 6.9500, '2020-01-10': 7.0000 }
sorted_keys = sorted(keys for keys in prc_dic)
prc_dic['2020-01-15'] = prc_dic.pop('3000-01-15')  ## Without explicitly mention the value of specific key


print('The copyright symbol is: \u00A9')
print('The copyright symbol has Unicode hex value: \\u00A9')  # With the output as the exact strings


def get_and_print_five():
    five = get_five()
    print(f'Called get_five(): result is {five}')
def get_five():
    return 5
get_and_print_five()