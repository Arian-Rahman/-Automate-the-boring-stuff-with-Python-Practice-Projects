#01  LISTS
'''
spam = [['cat','bat'],['lol',1,2,3,4,5]]
print("First element "+str(spam[0]))   #convert to STRING to print with other strings
print('First element 2nd '+str(spam[0][1]))
print('Second element 5th '+str(spam[1][5]))
print('Second element 2nd from last '+str(spam[1][-2]))
print('The '+str(spam[0][0])+'is Afraid of  ' + str(spam[0][1]))
'''

#02 Sublist with slices
"""
scam = [0,1,2,3,4,5,6,7]
print('All elements  '+str(scam[0:9]))
print(' 2nd to 4th  '+str(scam[1:4]))    #the last limiting one won't print
print(' 0th to -1 th   '+str(scam[0:-1]))
print(' some extra  \n' +str(scam[2:]) +" \n "+ str(scam[:3]) + "\n"+str(scam[:]) )
print(len(scam))


"""


#03 Changing Values
"""

spam =['cat','elephant','bat','rat']
spam[1] = 'LED'
print(spam)
spam= spam + ['A', 'B']*2
print("After concat "+ str(spam))
del spam [4]
print("AFTER DELETION " +str(spam))

"""

#04 Loops and lists
"""
supplies = ['pen','dictionary ']

for i in range(len(supplies)):
    print("Index:" +str(i)+"\n Item:"+ supplies[i])

print('pen' in supplies)
print("pen and bottle " not in supplies)

"""

#05 Multiple assignement           **
'''
cat = ['lily','black']
name,color = cat
print(name)
print(color)
'''

#06 Methods
'''
spam = ['a','B','b','C','c','d','a','a']
print(spam.index('a'))
spam.append('e')
spam.insert(0,'A')
spam.remove('a')
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)
spam.sort(key=str.lower)
print(spam)
'''

#07 Strings and tuples
'''
name = 'Zoey'
for i in name.upper() :
    print("*****"+i+"*****")

    #concat sting (Strings are immuteable , so need to slice it to edit it
newName = name[0:4]+ " The Cat"
print(newName)

#del and append function for list 
eggs=[1,2,4]
del eggs[2]
eggs.append(3)
print(eggs)
'''

#08 Tuple data type
'''
eggs =('hello ',9,76)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))
  #conversion
tuple(['cat','kitty'])
list("hello")
list(('cat',4,5))
'''

#09 References

a = [0,1,2,3,4]
b=a
b[0]=1
print(b)    #a changes if b is changed
    #passing ref
def egg(parameter) :
    parameter.append("HEllo There !!! ")
egg(a)
print(a)
    #copy
# c= copy.copy(a)    //does not work for some reason


















































































