
happy = 5
happy = True   # True and numbers (other than 0, None, Empty containers) returned to the same results
if happy:
    print("I am happy")

if not None:
    print("---")


var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']

var3 is var4  # False

name = input("123")
print("Hello,", name)

working_hrs = int(input("Enter the working hours: "))
normal_rate = 52.45
overload_rate = 88.9
if working_hrs <= 35:
    pay = (35 * normal_rate) + ((working_hrs - 35) * overload_rate)
else:
    pay = working_hrs * normal_rate
print(f'The weekly payment is {pay}')


# Loops - For Loops

    ## Dictionaries
d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
# d.values()
# d.items()
for key_value_tuple in d.items():
    print(f"key_value_tuple is {key_value_tuple}")
    # Unpacking
    key, value = key_value_tuple
    print(f"KEY: {key} VALUE: {value}")


# Range
for i in range(0, 5):
    print(f"i is now {i}")

    ##
for i in range(5, 0):
    print("This will not execute because start is greater than stop.")

for i in range(5, 0, -1):
    print("This message will self-destruct in {} secs...".format(i))


numbers = [3, 9, 1, 5, 7, 2, 11,\
           0, 3, 12, 3, 15]
i = 0
for x in numbers:
    if numbers[{i}]<numbers[{i+1}]:
    print(f"{x} is the largest number")
    else:
    i += 1

## While loops

# Nested Structures
for i in range(1,4):
    for j in range (1,4):
        if 1<= j:
            print(i,j)


## Continue & Break

for even in range  (0, 10, 2):
    #print(even)
    if even > 2:
        break ## will pause at even=4 since it meets the if condition
        #continue
    print(even) ## will only return 0, 2
print(even)  ## will only return 8, outside the loops


for odd in range(1, 10, 2):
    for even in range(0, 10, 2):
        if even > 2:
            # break
            continue
    print(even, odd)  # return of combinations



lst1 = ['a']
lst2 = ['b', lst1]
lst2[1].append('c')
lst2[1].remove('c')
lst3 = ['b', ['a']]


l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
for lst in l:
    if lst not in l[8:11]:
        print (lst)



f_suburbs = dict()
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

for key,value in f_suburbs.items():
    if value is not None and "Forest" not in key.split()[0]:
        print(f"{key}: {value}")



for i in range(1,101,1):
    if i % 3 == 0 and i % 5 != 0:
        print(f"{i}: Fizz")
        continue
    elif i % 3 != 0 and i % 5 == 0:
        print(f"{i}: Buzz")
        continue
    elif i % 3 == 0 and i % 5 == 0:
        print(f"{i}: FIZZ BUZZ")
        continue
    else: ## i % 3 != 0 and i % 5 != 0:
        print(i)

s = {'a', 'c'}
if 'a' in s or 'b' not in s
    print("True")

if 'a' not in s：
    print(s)



l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]
i = 0
for lst in l:
    print(f"{i}: {lst}")
    i = i + 1



first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']

i = 0
j = 0
for i in range(0,5):
    for j in range(0,5):
        if middle_names[j] is None:
            print(f"{first_names[i]} {last_names[i]}")
        if middle_names[j] is not None:
            print(f"{first_names[i]} {middle_names[j]} {last_names[i]}")


## Order is wrong

for last_name in last_names:
    for first_name in first_names:
        for middle_name in middle_names:
            if middle_name is not None:
                print(f"{first_name} {middle_name} {last_name}")
            if middle_name is None:
                print(f"{first_name} {last_name}")