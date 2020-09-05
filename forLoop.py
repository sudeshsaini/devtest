

#print ('hi ')
#print ('sudesh')

list = ['sudesh ', '1', 'sudesh']

print(min(list))
#list. add('kumar')
# for loop for a range - index starts from 0
for value in range(5):
    print (value)
#prints from 0 to 4

# we can start the first index by providing the starting index
for value in range(3,6):
    print(value)

# we can pass in a list object to iterate throgh
for value in list:
    print (value)

# we can iterate through a range in reverse order as well by providing the increment value as third input
for value in range (10,0,-1):
    print (value)
