import Item1,Item2,Item3,Item4

print("Welcome to our project")
print("Here is our items:")
print("Item 1: Patient Network")
print("Item 2: Specialist Network")
print("Item 3: Superimposed Network")
print("Item 4: All Reachable Marking")
item = int(input("Choose item: "))
if item != 4:
  firing = int(input("Input the number of firing: "))
print("Input the initial marking: ")
if item == 1:
    Item1.Item1(firing)
elif item == 2:
    Item2.Item2(firing)
elif item == 3:
    Item3.Item3(firing)
elif item == 4:
    Item4.Item4()
else: 
    print("No item like this one")
