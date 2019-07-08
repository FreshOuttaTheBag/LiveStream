import os
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
#inventory

team=[]
inventory = {
  "Dollars" : 1600,
}
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
        print("You can\'t use the same name twice in your team\n")
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

def beforeJourney():
  print("A 100% totally long journey awaits you, you may want to buy some supplies")
  print("What you would like to do.")
  print("1.) View your inventory")
  print("2.) Go to the store")
  print("3.) Start your journey")
  print("4.) View the map")
  choice = input("Enter the number of what you would like to do\n")
  if choice == '1':
    viewInventory(beforeJourney)
  elif choice == '2':
    os.system('clear')
    store(previousFunc)
    
    
  

storeDict = {
  "Ox" : 400,
  "Bullets" : 20,
  "Food (100 lbs)" : 100,
  "Clothing (sets)" : 10,
  "Spare Axel" : 50,
  "Spare Wheel" : 50,
  "Spare Toungue" : 50
}
def store(previousFunc):
  print("What would you like to buy?\n")
  print("It\'s recommended to bring 6 oxen, 3 pairs of clothing per person, 50 bullets, 200 lbs of food per person\n")
  print("Item : Price")
  for x,y in storeDict.items():
    print(x,y)
  choice = input('When you\'re done, enter \"yes\"\n')
  if choice.lower == 'yes' or choice.lower == 'y':
    previousFunc()
  
  

def  viewInventory(previousFunc):
  print(inventory)
  i = input("\nPress the enter key when you are done")
  os.system('clear')
  previousFunc()
  

makeTeam()
os.system('clear')
areYouSure()
os.system('clear')
beforeJourney()
