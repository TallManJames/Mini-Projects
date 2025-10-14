
class Person:
  def __init__(self, dadFname, lname):
    self.dadfirstname = dadFname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

dad = Person("Mark","Hatch")

class Child(Person):
  def __init__(self, dadFname, lname, kidFname, year):
    super().__init__(dadFname, lname)
    self.kidFirstname = kidFname
    self.graduationyear = year

  def welcome(self):
    print(f"Welcome, {self.kidFirstname +' '+ self.lastname}, son of {self.dadfirstname + " " + self.lastname} to the class of", self.graduationyear)

me = Child(dad.dadfirstname, dad.lastname, "James", 2024)
me.welcome()