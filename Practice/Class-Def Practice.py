
class community:
    def __init__(self, name, age, gender, present):
        self.name = name
        self.age = age
        self.gender = gender
        self.present = present
    def myFunc(self):
        print(f"{self.name} is a {self.age} year old {self.gender}, and their status inside the community is: {self.present}.")


community_members = []
print("Who are the members of this community?")
while True:
    name = input("What is the name of this member? (If you are done, type 'done')\n")
    if name == 'done':
        break

    print("How old are they?")
    try:
        age = int(input())
        if (age < 0) or (age > 100):
            print("Please enter a valid number 0-100.")
            continue
    except ValueError:
        print(f"Please enter a valid age of {name}.")
        continue

    try:
        genderInitial = input("What gender are they? (M/F)\n")
        if genderInitial.lower() == "m":
            gender = "male"
        elif genderInitial.lower() == 'f':
            gender = "female"
    except ValueError:
        print("Enter valid gender.")

    presentStatus = input("Are they currently inside the community? (Yes/No)\n")
    if presentStatus.lower() == 'yes':
        present = True
    else:
        present = False

    new_member = community(name, age, gender, present)
    community_members.append(new_member)


#for a description of members in the community
'''for member in community_members:
    member.myFunc()'''

#for finding number of ppl present
totalMembers = len(community_members)
comPopulation = 0
for member in community_members:
    if member.present == True:
        comPopulation += 1
comPopPercent = (f'{(comPopulation/totalMembers):.2%}')
print(f"So there are {comPopulation} out of {totalMembers} people present in the community as of now, or {comPopPercent}%.")
