# WAP to remove duplicate items from a list


# initializing list
L=[1,2,1,2,3,4,5,3,4]
# print ("The original list is : "+ str(L))

# using set() to remove duplicated from list
# L = (set(L))

# # printing list after removal
# # distorted ordering
# print ("The list after removing duplicates : "+ str(L))

# 1. check each items on a basket
temp_list=[]
# for each item in original basket
for i in L:
    # store items in temporary basket which are not added before in the basket
    if(i in temp_list):
        continue 
    else:
        temp_list.append(i)
        # print(i)

# print(temp_list)


def removal_duplicate(list):
    # 1. check each items on a basket
    temp_list=[]
    # for each item in original basket
    for i in list:
        # store items in temporary basket which are not added before in the basket
        if(i in temp_list):
            continue 
        else:
            temp_list.append(i)
            # print(i)

    return(temp_list)

a= removal_duplicate(L)
print(a)
    








def duplicate_removal(list):
    val = set(list)
    return val
X=duplicate_removal(L)
# print(X)

# print(duplicate_removal(['my','name','is','muna', 'bhusal', 'bhusal', 'is', 'muna']))
    

