catnames =[]

while True :
    print("Enter the name of cat no " + str(len(catnames)+1) + " :  (enter nothing to exit)" )
    name =input()
    if name == ' ':
        continue
    catnames = catnames+[name]
  print ("Cat names are  : ")
  for name in catnames:
      print(" " + name)