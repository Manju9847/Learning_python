# Python program to swap two elements in a list

# Working without using function
a= [1,2,3,4]
temp= a[2]
a[2]= a[3]
a[3]= temp
# print(a)

# Working using function
def swap_element(list, position):

    if(len(list) >= position[0] and len(list) >= position[1]):
        position_first = position[0]
        position_second = position[1]

        temp= list[position_first]

        list[position_first]= list[position_second]
        list[position_second]= temp
     
        return list
    else:
        return("List Out of Range")
b= [5,6,7,8]
swap_position = (1,8)

get_exchanged_data = swap_element(b , swap_position)
# print(get_exchanged_data)


count = 0
c = ["apple","ball","cat"]
for i in c:
    count=count+1
print(count)
    