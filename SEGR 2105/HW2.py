from datetime import datetime
current_hour = int(datetime.now().strftime("%H"))
if current_hour < 12:
    dayPeriod = "morning"
elif current_hour < 18:
    dayPeriod = "afternoon"
else:
    dayPeriod = "evening"
print(f"\nGood {dayPeriod} Dr. Alaimo!")

while True:
    problemChoice = input("Which problem would you like? (1,2,4,5,7, or say 'stop' to quit): ")
    if problemChoice.lower() == 'stop':
        break
    elif problemChoice == "1":
        #Problem 1 - have a number n and step size x that sums the difference of both numbers as x goes down by 1 for each iteration
        #ex: n=5 x=2 -> output = 5+(5-2)+(5-4) = 9
        ans = 0
        while True:
            n = input("What is the initial number 'n'?: ")    #input value n
            if n.isdigit() is True:                 #is it a whole number?
                n = int(n)                #makes it an integer rather than string and breaks the loop
                break
            else:
                print("Error, make the 'n' a valid whole number.")         #not a whole number, or number. error pops up, runs through loop again
        while True:
            x = input("What is the step size 'x'?: ")     #input value x
            if x.isdigit() is True and int(x)>0:            #is it a whole number?  Also keeps the step size being 0
                x = int(x)               #makes it an integer rather than string and breaks loop
                break
            else:
                print("Error, make the 'x' a valid whole number.")        #not a whole number, or number. error pops up, runs through loop again      
        tempX = 0     #this is a temporary x that will change
        while True:
                if tempX<=n:
                    ans += (n-tempX)        #the answer will change until the if statement is false
                    tempX += x       #temporary x will go up by x
                else:
                    print("Final answer:", ans)      #prints final answer
                    break
    elif problemChoice == "2":
        #Problem 2: write a loop that adds all numbers in a str
        ans2 = 0
        string_val = input("Enter numbers you want added: ")
        for i in string_val:
            if i.isdigit() is True:
                i = int(i)
                ans2 += i
            else:
                continue
        print(ans2)

    elif problemChoice == "4":
        # Problem 4: Make a function to remove duplicates and one to return common elements
        L1 = [1,2,3,4,5,6]
        tempList = L1.copy()       #makes another list so L1 can be changed without complications
        L2 = [1,2,3,7,8]
        while True:
            choice = input("Which function would you like to use? (1 or 2)"
                        "\n1. Remove duplicates from List 1 that are in List 2" \
                        "\n2. Make List 1 only values that are in both lists.\n")        #choose which function you would like
            if choice == "1":
                for i in tempList:
                    for j in L2:               #nested for loop to iterate through tempList (L1) and L2
                        if i==j:
                            L1.remove(i)         #if i and j are the same, it removes "i" from L1, keeping tempList the same to avoid errors                
                break
            elif choice == "2":
                bothList = []          #new list for values that contains values from both lists
                for i in L1:
                    for j in L2:          #nested for loop to iterate through L1 and L2 (list not being broken, no need for tempList)
                        if i==j:
                            bothList.append(i)        #adds i to bothList if i and j are the same
                L1 = bothList.copy()              #turns L1 into a copy of bothList for final answer
                break
            else:
                print("Enter valid choice.")          #choice does not equal '1' or '2'
        print("L1 =",L1)         #prints the final answer

    elif problemChoice == "5":
        # Problem 5: Find how many times an object appears in a list
        # I assume you only mean these 4 object types
        numInt = 0       #this will be number of integers, and same for next 3 lines for string, floats, and lists respectively
        numStr = 0
        numFloat = 0
        numList = 0
        lst = [1, "one", 2.0, [1,2,3], 2]          #list named lst that contains objects we will find
        for i in lst:               #iterate through lst
            if type(i)==int:
                numInt += 1             #if iteration 'i' is an integer, it adds 1 to number of integers
            elif type(i)==str:
                numStr += 1          #if i is string, +1 to numStr
            elif type(i)==float:
                numFloat += 1               #if i is float, +1 to numFloat
            elif type(i)==list:
                numList += 1         #if i is list, +1 to numList
        print(f"{{int: {numInt}, str: {numStr}, float: {numFloat}, list: {numList}}}")    #double curly brackets for printing one because of the f string, prints all the numbers of objects inside


    elif problemChoice == "7":
        # Problem 7: dictionary that has functionalities to: modify/remove grade, add student/grade pair, create a 10-point grade scale for letter grades
        grades = {
            "quiz1": {"student1": 88, "student2": 91, "student3": 77, "student4": 81},
            'hw1': {'student1': 90, 'student2': 98, 'student3': 82, 'student4': 85},
            'test1': {'student1': 85, 'student2': 92, 'student3': 86, 'student4': 84}
        }    #main grades
        letterGradeDic = {}
        def modify():
            while True:
                modAssignment = input("Which assignment would you like modified?: ")
                if modAssignment not in grades:
                    print("Please select valid assignment to modify.")
                else:
                    break
            while True:
                modStudent = input("Which student's grade would you like modified? (student1 / student2 / student3 / student4): ")
                if modStudent not in grades[modAssignment]:
                    print("Please select which student's grade you would like modified.")
                else:
                    break
            while True:
                newGrade = input(f"{modStudent} grade in {modAssignment} is: {grades[modAssignment][modStudent]}. What would you like to change it to?: ")
                try:
                    float(newGrade)
                    break
                except ValueError:
                    print("Please enter a valid grade.")
            grades[modAssignment][modStudent] == newGrade
            print(f"Changed {modStudent} grade in {modAssignment} to {newGrade}")

        def remove():
            while True:
                remAssignment = input("Which assignment would you like changed?: ")
                if remAssignment not in grades:
                    print("Please select valid assignment.")
                else:
                    break
            while True:
                remStudent = input("Which student's grade would you like removed? (student1 / student2 / student3 / student4): ")
                if remStudent not in grades[remAssignment]:
                    print("Please select which student's assigment grade you would like removed.")
                else:
                    print(f"{remStudent} {remAssignment} grade was removed.")
                    grades[remAssignment][remStudent] = None
                    break
        def add():
            while True:
                addAssignment = input("Which assignment is getting added?: ")
                if addAssignment not in grades:
                    break
                else:
                    print("Assignment is already created.")
            while True:
                try:
                    addS1Grade = float(input(f"What grade did student1 get on {addAssignment}?: "))
                    break
                except ValueError:
                    print("Enter valid grade for student1 grade.")
            while True:
                try:
                    addS2Grade = float(input(f"What grade did student2 get on {addAssignment}?: "))
                    break
                except ValueError:
                    print("Enter valid grade for student2 grade.")
            while True:
                try:
                    addS3Grade = float(input(f"What grade did student3 get on {addAssignment}?: "))
                    break
                except ValueError:
                    print("Enter valid grade for student3 grade.")
            while True:
                try:
                    addS4Grade = float(input(f"What grade did student4 get on {addAssignment}?: "))
                    break
                except ValueError:
                    print("Enter valid grade for student4 grade.")
            newAssignment = {
                addAssignment: {"student1": addS1Grade, "student2": addS2Grade, "student3": addS3Grade, "student4": addS4Grade}
            }
            grades.update(newAssignment)

        def letterGrade():
            for i in grades:    #itertate assignments in gradesDictionary
                letterGradeDic[i] = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}   #creates a letter grade dictionary with each iteration (assignment) of grades

            for assignment in grades:      #this is for actually making the integers go up (the problem)
                for student in grades[assignment]:
                    g = grades[assignment][student]
                    if g == None:
                        pass
                    elif g >= 90:
                        letterGradeDic[assignment]["A"] += 1
                    elif g >= 80:
                        letterGradeDic[assignment]["B"] += 1
                    elif g >= 70:
                        letterGradeDic[assignment]["C"] += 1
                    elif g >= 60:
                        letterGradeDic[assignment]["D"] += 1
                    else:
                        letterGradeDic[assignment]["F"] += 1

        while True:
            print("Here are the options available:\n1. Modify a grade for a student.\n2. Remove a grade for a student." \
            "\n3. Add an assignment and assign grades for each student." \
            "\n4. Make a new dictionary full of letter grades for each assignment." \
            "\n'Stop'. Stops running the file.\n'View'. You can view the grades dictionary.") #lays out options and numbers/value assigned
            p7Options = input("Which option would you like? (1/2/3/4/'Stop'/'View'): ").lower()
            if p7Options == "stop":  
                break
            elif p7Options == "view":
                print("Here are all the grades:\n", grades)
            elif p7Options == "1":
                modify()
            elif p7Options == "2":
                remove()
            elif p7Options == "3":
                add()
            elif p7Options == "4":
                letterGrade()
                print("Here are all the letter grades:\n", letterGradeDic)
            else:
                print("Invalid option, please try again.")
    else:
        print("Enter valid choice.")