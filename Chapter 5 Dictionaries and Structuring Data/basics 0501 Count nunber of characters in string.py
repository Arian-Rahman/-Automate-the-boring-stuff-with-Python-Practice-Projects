import pprint

print("Enter your message : ")
message =input()
#message ="It was a bright sunnay day in April , and the clocks were strking thirteeen ."
count ={}

for char in message :
    count.setdefault(char,0)
    count[char]=count[char]+1

pprint.pprint (count)

