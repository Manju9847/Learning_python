# Python | Ways to find length of list

count = 0
c = ["apple","ball","cat"]
for i in c:
    count=count+1
print(count)



#also by using len()function
# l= [1,2,3,4]
# print(len(l))


#using function

def find_length(my_string):
    count = 0    
    for i in my_string:
        count=count+1
    return(count)

animals = ["apple","ball","cat"]
val= find_length(animals)
print(val)

