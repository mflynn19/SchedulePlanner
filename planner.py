#Initial interaction with user
print("Hello! Welcome to the Schedule Planner 2000!")

def questionList():
    what = input("Please tell us what task you would like to do today!\n")
    priority = input("How important is this task to you on a scale of 1-5?\n")
    time = input("How long do you estimate this task will take you in minutes?\n")
    return {"task": what, "priority": priority, "length": time}


userTask = []
priortized = []

start = True
while start:
    userTask.append(questionList())
    
    continueAsk = True
    while continueAsk:
        askUser = input("Would you like to add anything to your list? Yes or No?\n")
        if askUser.lower() == "yes":
            userTask.append(questionList())
        else:
            continueAsk = False
    
    organize = input("How would you like to sort your To-Do list? By time, task, or priority?\n")
    if (organize.lower() == "time"):
        prioritized = sorted(userTask, key = lambda i: i["length"], reverse = True)
    elif (organize.lower() == "task"):
        prioritized = sorted(userTask, key = lambda i: i["task"])
    elif(organize.lower() == "priority"):
        prioritized = sorted(userTask, key = lambda i: i["priority"], reverse = True)
    else:
        print("Sorry try again next time.")
    
    
    
    count = 0
    totalLength = 0
    print("\nHere is your To Do list!")
    for duty in prioritized:  
        
        print(str(count+1) + ". " + duty["task"].title()  + " for " + str(duty["length"]) + " minutes.")
        totalLength += int(duty["length"])
        count += 1
    print("\nIt will take you " + str(totalLength) + " minutes to complete your To Do list!")
    start = False
    
