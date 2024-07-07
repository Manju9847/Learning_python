
# WAP to merge 2 list without using + operator
L1= [1,2,3,4]
L2=[5,6,7,8]

print("List1 before Concatenation:\n" + str(L1))
for x in L2 : 
    L1.append(x) 

print ("Concatenated list i.e. list1 after concatenation:\n" + str(L1))