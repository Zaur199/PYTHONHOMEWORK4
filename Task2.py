with open('file1.txt', 'r', encoding='utf-8') as f1:
    num_1 = f1.read()
num_1 = num_1[:num_1.find('=')].split('+')

with open('file2.txt', 'r', encoding='utf-8') as f2:
    num_2 = f2.read()
num_2 = num_2[:num_2.find('=')].split('+')

num_all = num_1 + num_2

my_dict = {}

for elem in num_all:
    if 'x' not in elem:
        key = 0
    elif '^' not in elem:
        key = 1
    else:
        key = int(elem[elem.find('^') + 1:])
        
    if key > 0:
        if key in my_dict:
            my_dict[key] += int(elem[:elem.find('*')])
        else:
            my_dict[key] = int(elem[:elem.find('*')])
    else:
        if key in my_dict:
            my_dict[0] += int(elem)
        else:
            my_dict[0] = int(elem) 
    #print(my_dict)

my_str = '' 
for key, value in sorted(my_dict.items(),reverse=True):
    if key == 0:
        my_str += str(value)
    elif key == 1:
        my_str += f'{value}*x + '
    else:
        my_str += f'{value}*x^{key} + '
    
my_str = my_str + ' = 0'
print(my_str)

with open('sum.txt', 'w', encoding='utf-8') as my_file:
    my_file.write(my_str)
