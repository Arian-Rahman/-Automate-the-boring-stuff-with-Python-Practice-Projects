#01 Dictionaries
"""
dictionary01 ={'name': 'Zophie', 'species ': 'Cat'}
dictionary02 = {'species ': 'Cat' ,'name':'Zophie'}
print(dictionary01 == dictionary02)  #unlike lists , the order does not matter
print(dictionary02['name'])
"""
#02 Birthday Dictionary
import pprint

"""
birthdays ={'Arian': 'May 22', 'Maria': 'Jul 28'}
while True :
    print("Please input the name of the person (Enter "Space" to exit )")
    name = input()
    if name == ' ':
        break
    if name in birthdays:
        print(name + "'s Birth day is at "+ birthdays[name])
    else :
        print("I don't have his/her data , please input his birthday for me to store ")
        date = input()
        birthdays[name]=date
        print("Database updated ")
"""

#03 keys , values and items Method                  ***

"""
a= {'color':'Orange','age':'69','name':'Trump'}
print(a.values()) #all at once
print("\n ---Values--- \n ")
for v in a.values() :   #one by one
    print(v)
print("\n---Keys -\n")
for k in a.keys() :
    print(k)
print("\n---Items -\n")
for i in a.items() :
    print(i)
print("\n------Using one loop----------\n ")
for k,i in a.items():
    print("Key --" +k+ "  Item --" +str(i))
"""
#04 the Get() method , it takes two arguments , mainly used for number based dictionaries
"""
items = {'cups': 3 , 'apples' : 4}
print("i'm bringing " +str(items.get('cups',0)) + " Cups  and " +str(items.get('eggs',0))+ ' eggs ')   #without 2 peramemters , it'll crash

items.setdefault('color','black')
print(items['color'])
print(items.items())
"""
#05 count the number of each character in a string
'''
message ="It was a bright sunnay day in April , and the clocks were strking thirteeen ."
count ={}

for char in message :
    count.setdefault(char,0)
    count[char]=count[char]+1

pprint.pprint (count)
'''

#06  NEsted dictionaries and lists
'''
allGuest = {
    'Alice':{'Apples':5 , 'Cream': 19},
    'Bob': {'Android':16, 'Cream' : 91 }
}

def total (guest,item) :
    num = 0
    for k,v in guest.items():
        num = num + v.get(item,0)
    return num

print(" APPLES __ " +str(total(allGuest,'Apples')))
print ("  Cream   "+ str(total(allGuest,'Cream')))
'''
















