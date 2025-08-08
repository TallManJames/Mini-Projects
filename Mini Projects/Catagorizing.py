
nameList = []
ageList = []
genderList = []

def peopleInfo(name, age, gender):
    nameList.append(name)
    ageList.append(age)
    genderList.append(gender)

x=0

print("\nAdd information on each patient so it may be organized accordingly:" \
    "\nNOTE: When adding information, ages must be numerical and genders must be either 'Male' or 'Female'")
while x == 0:
    peopleInfo(input("Name: "),input("Age: "),input("Gender: "))
    y=0
    while y==0:
        more = input("Would you like to add more people?: ")
        if more.lower() == "yes":
            print("Ok, then describe the next person:")
            y+=1
        elif more.lower() == "no":
            print("Then that wraps up everbody!\n")
            x+=1
            y+=1
        else:
            print("Could you repeat that?")

pediMaleNameList = []
pediFemaleNameList = []
physMaleNameList = []
physFemaleNameList = []

intAgeList = []
for i, a in enumerate(ageList):
    z=0
    while z==0:
            if a.isdigit() and int(a) >= 0 and int(a) <= 100:
                intAgeList.append(int(a))
                z+=1
            else:
                print(f"There seems to have been a mistake for the age of {nameList[i]}!")
                a = input("(Numerical Values ONLY) How old are they?: ")
    g = genderList[i].lower()
    while z==1:
            if int(a) >= 18:
                if g == "male":
                    physMaleNameList.append(nameList[i])
                    z+=1
                elif g == "female":
                    physFemaleNameList.append(nameList[i])
                    z+=1
                else:
                    print(f"There seems to have been a mistake for the gender of {nameList[i]}!")
                    g = input("(Male OR Female) What gender are they?: ")
            else:
                if g == "male":
                    pediMaleNameList.append(nameList[i])
                    z+=1
                elif g == "female":
                    pediFemaleNameList.append(nameList[i])
                    z+=1
                else:
                    print(f"There seems to have been a mistake for the gender of {nameList[i]}!")
                    g = input("(Male OR Female) What gender are they?: ")

# Last stage of project unless I want to do more:
# Create Pediatrician and Physician doctors and evenly spread out patients to them

femalePediatricians = ['Jackie','Rachael','Lily']
jackiePatients = []
rachaelPatients = []
lilyPatients = []

femalePhysicians = ['Cerveza','Poppy']
cervezaPatients = []
poppyPatients = []

malePediatricians = ['Josh','Preston']
joshPatients = []
prestonPatients = []

malePhysicians = ['Dylan','Bobby','Jackson','Mason']
dylanPatients = []
bobbyPatients = []
jacksonPatients = []
masonPatients = []  


