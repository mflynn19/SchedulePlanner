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
            print("\nHere is your To Do list!")
            continueAsk = False
                
    prioritized = sorted(userTask, key = lambda i: i["priority"], reverse = True)
    
    
    count = 0
    totalLength = 0
    for duty in prioritized:  
        print(str(count+1) + ". " + duty["task"].title()  + " for " + str(duty["length"]) + " minutes.")
        totalLength += int(duty["length"])
        count += 1
    print("It will take you " + str(totalLength) + " minutes to complete your To Do list!")
    start = False
    
