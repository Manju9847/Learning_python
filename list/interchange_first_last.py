# Question: Python program to interchange first and last elements in a list


# Working Without using function
a = [1,2,3,4]
temp = a[0]  # a[0] value of first elemrnt is 1, which will be stored in temp
a[0] = a[-1] #As we have to interchange the last and first element- value of last element will be stored in a[0], as a fisrt element, still the value of last element is not changed
a[-1] = temp #The value of last element is updated with the value on temp- which has hold the value of first element.
print(a) #This will print the interchanged  first and last elements in a list




# Working using functiom

def interchanger(list):
    temp = list[0]

    list[0] = list[-1]
    list[-1] = temp

    return list

c = [1,2,3,4]

get_exchanged_data = interchanger(c)
print(get_exchanged_data)


b = [1,2,3,4,6,8,3,9,7,3]

get_exchanged_data = interchanger(b)
print(get_exchanged_data)
