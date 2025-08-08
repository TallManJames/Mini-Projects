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
    problemSelect = input("\nWhich problem would you like to test? " \
    "\n1. Changing all lowercase numbers in a string to uppercase and vice versa" \
    "\n2. Create a triangle of stars" \
    "\n3. Input a string, and see smallest number and letter latest in the alphabet within that string" \
    "\n4. Unit conversions" \
    "\n5. Repetitive inputs of numbers, with results on all of them after" \
    "\nOr are you done? (1/2/3/4/5/'done'): ")      #which problem would you like?
    print()

    if problemSelect.lower() == "done":         #this will make everything finish
        break

    try:
        problemSelect = int(problemSelect)            #attempts to make it an integer
    except:
        print("Please make your problem selection a whole number.")            #error when problem select isn't a number

    if (problemSelect < 1) or (problemSelect > 5):
        print("Please select a problem from 1 to 5.")           #this happens if problemSelect isn't 1-5
    
    
    elif problemSelect == 1:     #Runs Problem 1
        #Problem 1 - string converter (upper to lower and lower to upper)
        #ex: "This Example" --> "tHIS eXAMPLE"
        str1 = input("What text would you like converted?: ") #original text
        newStr = "" #empty string to add new and final letters
        for i in str1:
            if i.isupper():
                newStr += i.lower()     #if its uppercase, this will convert it to lowercase and add to the new string
            elif i.islower():
                newStr += i.upper()     #this does the opposite
            else:
                newStr += i        #this brings miscillaneous into the new string
        print(newStr)         #prints new string, final answer

    
    elif problemSelect == 2:      #runs problem 2
        #Problem 2 - Print a triangle with height "n"
        while True:
            try:
                n = int(input("How long would you like the triangle?: "))        #input how long you want the triangle
                break
            except ValueError:
                print("Error, please try again with a whole number.")       #try again

        numStars = 1      #this value will change, not n
        for i in range(2*n-1):     #2*n-1 means n rows twice, but minus one because I don't want 2 of the max stars
            if numStars != n:       #this is as numStars increases
                for j in range(numStars):
                    print("*", end=' ')      #prints however many stars is in the range of numStars
                numStars += 1          #adds so it will have another star next row
                print()
            elif numStars == n:          #this means we've hit max length (n)
                for j in range(numStars):
                    print("*", end=' ')            #same deal, prints number of stars
                numStars -= 1              
                n -= 1              #n and numStars going down together makes it so that they stay the same and decrease each row by 1
                print()
    
   
    elif problemSelect == 3:
        #Problem 3: find smallest number and letter latest in alphabet within string
        numList = []      #where all numbers will go
        letterList = []       #where all letters will go
        notOrderStr = input("Find smallest number and latest letter in alphabet. Enter a string: ")     #input str
        for i in notOrderStr:
            if i.isdigit():
                numList.append(i)                  #if it's a number (digit), then it will be added to numList
            elif i.isalpha():
                letterList.append(i)               #if it's a letter (alpha), then it will be added to letterList

        if len(numList) != 0:       
            smallestNum = min(numList)       #min finds smallest number, so i can print in next line
            print(f"The smallest number in the string is '{smallestNum}'")
        else:
            print("No numbers in the string.")          #prints if no numbers

        if len(letterList) != 0:     #will print latest letter if there are letters
            for i in letterList:
                if i.isupper():
                    letterList.append(i.lower())      #for some reason uppercase letters don't work in next function so this (sorta) makes everything lower
            latestLetter = max(letterList, key = str)                  #the key makes it possible to do a max function on letterList
            print(f"The letter latest in the alphabet in the string is '{latestLetter}'")
        else:
            print("No letters in this string.")         #prints if no letters

    
    elif problemSelect == 4:
        #Problem 4: unit conversions
        while True:
            try:
                ftInput = float(input("How many feet would you like converted? (only numerical vaules): "))     #feet input as floater
                break
            except ValueError:
                print("Invalid input, please enter a number.")         #error
        while True:
            while True:
                try:
                    print("What would you like it to be converted to? Again, numerical values only.\n1. Centimeters" \
                    "\n2. Meters\n3. Inches\n4. Miles")                                  #options
                    conversion = int(input("Conversion: "))             #conversion options input
                    break
                except ValueError:
                    print("Invalid input, whole numbers only (1/2/3/4).")           #not number value
            if (conversion >= 1) and (conversion <= 4):                     #insures these number values work (1,2,3,4) because they are already numbers
                match conversion:                                       #match function for cases to get final answer
                    case 1:
                        conversion = "centimeters"           #changing for print function at end, same with rest
                        ans = ftInput * 30.48                        #ft to cm conversion (not gonna put the rest cause it's the same)
                    case 2:          
                        conversion = 'meters'
                        ans = ftInput * .3048
                    case 3:          
                        conversion = 'inches'
                        ans = ftInput * 12
                    case 4:          
                        conversion = 'miles'
                        ans = ftInput * .000189394
                break
            else:
                print("Please enter a valid number. (1/2/3/4)")
        print(f"{ftInput} feet is {ans} {conversion}.")


    elif problemSelect == 5:
        #Problem 5: Input numbers
        posNum = []               #this is where positive numbers will go to be used later
        while True:
            while True:
                try:
                    tempNum = float(input("Enter a number: "))           #inputs for numbers
                    break
                except ValueError:
                    print("Error, please enter a numerical value.")
            if tempNum >= 0:
                posNum.append(tempNum)          #if number is >= 0, it gets added to the list
            else:
                break
        if len(posNum) == 0:
            print("No positive numbers inputed.")
        else:
            product = 1              #1*x = x so this makes it easier
            for i in posNum:
                product = product * i           #each posNum value multiplies
            #final answers
            print(f"The product of all positive numbers that were input is {product}.")
            print(f"The maximum positive number that was input is {max(posNum)}.")
            print(f"The minimum positive number that was input is {min(posNum)}.")
            print(f"{len(posNum)} positive numbers were input in total.")