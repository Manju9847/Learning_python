# how to take list as input from user

get_list_len = int(input('Length of List?'))
b = []

for i in range(get_list_len):
    data = input('Enter your value: ')
    b.append(data)

print(b)