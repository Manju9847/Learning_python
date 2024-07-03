#Maximum and Minimum of two numbers in Python


a= [6,8,2,7,1,2,3,4,5,6,7,8,9,1]
minimum= None
maximum= None
for i in range(len(a)):
    if(minimum==None and maximum== None):
        minimum= a[i]
        maximum=a[i] 

    else:
        if(minimum>a[i]):
            minimum=a[i]

        if(maximum<a[i]):
            maximum=a[i]
print(minimum)
print(maximum)

print('__________')

for i in a:
    if(minimum==None and maximum== None):
        minimum= i
        maximum= i
    
    else:
        if(minimum>i):
            minimum= i

        if(maximum<i):
            maximum=i

print(minimum)
print(maximum)