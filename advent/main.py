f = open("input.txt", "r")
numbers = {"1", "2", "3", '4', '5', '6', '7', '8', '9', '0'}
numbers2 = {"one", 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', "1", "2", "3", '4', '5',
            '6', '7', '8', '9', '0'}
dict = {"1": 1
    , "2": 2,
        "3": 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0,
        "one": 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'zero': 0

        }
sum = 0
first_number = 0
last_number = 0
for line in f:
    for symbol in line:
        if symbol in numbers:
            if first_number == 0:
                first_number = int(symbol)
                last_number = int(symbol)
            else:
                last_number = int(symbol)
    sum += first_number * 10 + last_number
    first_number = 0
    last_number = 0
print(sum)

f = open("input.txt", "r")

sum = 0
for line in f:
    newlist = []
    for number in numbers2:
        if number in line:
            x = line.split(number)
            y = -len(x[0])
            #print(range( len(x) - 1,0, -1))
            for i in range(len(x) - 2,0, -1):
                #print(i)
                #print(x)
                x[i]+=x[i + 1]
                x[i]+=number
                newlist.append([dict[number], len(x[i])])
            newlist.append([dict[number], len(x[-1])])
    newlist.sort(key=lambda a: a[1], reverse=True)
   #print(newlist)
    number = newlist[0][0] * 10 + newlist[-1][0]
    sum += number
    #print(number)
print(sum)
