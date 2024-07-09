# WAP to change 2D to 1D

a = [
    [1,2,3],
    [3,4,5]
] 

# [1,2,3,3,4,5]
b = []

for i in a:
    # print(i)
    for j in i:
        # print(j)
        b.append(j)

# print(b)


def twoD_oneD(my_list):
    b = []
    for i in my_list:
        # print(i)
        for j in i:
            b.append(j)

    return(b)

val= twoD_oneD(a)
print(val)