toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(item):
   toDoList.append(item)
   return toDoList

def deleteItem(item):
    toDoList.remove(item)
    return toDoList
    

userAns = input("Do you want to change your list or quit? A/Q")
while userAns == "A":
   item = input("What item do you want to add?")
   addItem(item)
   item1 = input("What item do you want to remove")
   deleteItem(item1)
   userAns = input("Do you want to add to your list or quit? A/Q")