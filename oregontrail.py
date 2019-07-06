class Person:
  def __init__(self,name,health,disease,hunger):
    self.name = name
    self.health = health
    self.disease = disease
    self.hunger = hunger

class Wagon:
  def __init__(self,name,brokenPart):
    self.name = name
    self.brokenPart = brokenPart
#inventory = []
team=[]
wagon = Wagon(None,None)

def makeTeam():
  global team
  global wagon
  choices=["first",'second','third','fourth','fifth']
  i=0  
  while i<len(choices):
    cont = False
    person = Person('name',100,'healthy',100)
    name = input("Enter the name of the %s person on your team\n"%choices[i])
    for x in team:
      if x.name == name:
        print("You can't use the same name twice in your team\n")
        cont = True
    if cont == True:
      continue
    person.name = name
    team.append(person)
    i+=1
  wagon.name = input("Enter the name of your Wagon\n");


def areYouSure():
  done = False
  while done != True:
    choices=[]
    print("\nYou will start Text-Based Trail with \n1.) Wagon Name: %s" % wagon.name)
    choices.append('1')
    for x in range(len(team)):
      print("%d.) %s" % (x+2,team[x].name))
      choices.append(str(x+2))
    choice = input("Enter the number of the name you would like to change. \nOtherwise, enter \"yes\"\n")
    if choice == '1':
      wagon.name = input("Enter the new name of your Wagon.\nOld Wagon Name: %s\n" % wagon.name)
    else:
      if choice.lower() == 'yes' or choice.lower() == 'y':
        done = True
      elif choice.isdigit():
        team[int(choice)-2].name = input("Enter a new name for your team member.\nOld name: %s\n" % team[int(choice)-2].name)


makeTeam()
areYouSure()
