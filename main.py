import time
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def herosturn(hh,cpuh, sword):
  print('It\'s your turn!')
  print('Your health is:', hh)
  print('Monster\'s health is', cpuh)
  time.sleep(5)
  choice=input('Make a choice (Sword) (Pike) (Heal) ')
  
  if choice == 'Sword' or choice == 'sword':
    attack = True
    print('\nYou chose', choice)
    damage = random.randint(15, 25)
    if 'sword' in sword:
      if 'diamond' in sword:
        damage = damage * 2
      elif 'gold' in sword:
        damage = damage * 1.8
      elif 'silver' in sword:
        damage = damage * 1.6
      elif 'iron' in sword:
        damage = damage * 1.4
      elif 'wooden' in sword:
        damage = damage * 1.2
    print('You did', damage, 'damage!')
    cpuh = cpuh - damage
    print('Monster\'s health is now:', cpuh)
    time.sleep(4)
    cls()
    return attack , cpuh

  elif choice == 'Pike' or choice == 'pike':
    attack = True
    print('\nYou chose', choice)
    damage = random.randint(5, 35)
    print('You did', damage, 'damage!')
    cpuh = cpuh - damage
    print('Monster\'s health is now:', cpuh)
    time.sleep(4)
    cls()
    return attack , cpuh

  elif choice == 'Heal' or choice == 'heal':
    attack = False
    print('\nYou chose', choice)
    healamount = random.randint(10, 30)
    print('You healed', healamount, 'health!' )
    hh = hh + healamount
    print('Your health is now:', hh )
    time.sleep(4)
    cls()
    return attack , hh

  elif choice == 'Defeat' or choice == 'defeat':
    attack = True
    print('\nYou chose', choice)
    damage = 1099
    print('You did', damage, 'damage!')
    cpuh = cpuh - damage
    print('Monster\'s health is now:', cpuh)
    time.sleep(4)
    cls()
    return attack , cpuh

  else:
    print("You chose nothing and the monster laughed")
    return cpuh



def computersturn(cpuh, hh, shield):
  print('It\'s the monster\'s turn!')
  print('Your health is:', hh)
  print('Monster\'s health is', cpuh)
  time.sleep(5)
  choice = random.randint(1,3)

  if choice == 1:
    print("\nMonster chooses sword!")
    attack = True
    damage = random.randint(15, 25)
    if 'shield' in shield:
      if 'diamond' in shield:
        damage = damage * .2
      elif 'gold' in shield:
        damage = damage * .4
      elif 'silver' in shield:
        damage = damage * .6
      elif 'iron' in shield:
        damage = damage * .8
      elif 'wooden' in shield:
        damage = damage * .9
    print('Monster did', damage, 'damage!')
    hh = hh - damage
    print('Your health is now:', hh)
    time.sleep(4)
    cls()
    return attack , hh

  if choice == 2:
    print('\nMonster chooses pike!')
    attack = True
    damage = random.randint(5, 35)
    if 'shield' in shield:
      if 'diamond' in shield:
        damage = damage * .2
      elif 'gold' in shield:
        damage = damage * .4
      elif 'silver' in shield:
        damage = damage * .6
      elif 'iron' in shield:
        damage = damage * .8
      elif 'wooden' in shield:
        damage = damage * .9
    print('Monster did', damage, 'damage!')
    hh = hh - damage
    print('Your health is now:', hh)
    time.sleep(4)
    cls()
    return attack , hh

  if choice == 3:
    print('\nMonster chooses heal!')
    attack = False
    healamount = random.randint(10, 30)
    print('Monster healed', healamount, 'health!' )
    cpuh = cpuh + healamount
    print('Monster\'s health is now:', cpuh )
    time.sleep(4)
    cls()
    return attack , cpuh

gamestart = input('Type start to start ')
if gamestart == 'skip':
  herosturn(hh=100, cpuh=100)

while gamestart not in ('start', "Start", 'skip', 'Skip'):
  print('Type Start to start ')
  gamestart = input()

print('\nYou have woken up in a dungeon')
time.sleep(3)
print('\nYou hear monsters ahead')
time.sleep(3)
print('\nYou have to fight')
time.sleep(3)
print('\nAs you progress the monsters will become more difficult to defeat')
time.sleep(3)
print('\nGood luck!')
time.sleep(5)
cls()


hh= 100
cpuh=100
level = 1
material = 'wooden', 'iron', 'silver', 'gold', 'diamond'
items = 'shield', 'sword'
sword = 'basic sword'
shield = 'no shield'





while True:
  placehold = 0
  placehold = herosturn(hh,cpuh, sword)
  
  if placehold[0] == True:
    cpuh = placehold[1]
  else:
    hh = placehold[1]



  if hh < 0:
    print('Oh no you died')
    break

  if cpuh < 0:
    print('\ncongradulations you killed the monster')
    time.sleep(3)
    print('Prepare for the next monster, this one will be tougher')
    break

  placehold = computersturn(cpuh,hh, shield)

  if placehold[0] == True:
    hh = placehold[1]
  else:
    cpuh = placehold[1]

  if hh <= 0:
    print('Oh no you died')
    break

  if cpuh <= 0:
    print('\ncongradulations you killed the monster')
    time.sleep(3)
    print('Prepare for the next monster, this one will be tougher')
    break


hitem1 = random.randint(0,4)
hmat1 = random.randint(0,1)

hitem = material[hitem1]
hmat = items[hmat1]

herositem = hitem + ' ' + hmat

print('\nYou got a',herositem+'!','\n')

if 'sword' in herositem:
  sword = herositem
elif 'shield' in herositem:
  shield = herositem



hh = 100
cpuh = 120
level = 2

while True:
  placehold = 0
  placehold = herosturn(hh,cpuh, sword)
  
  if placehold[0] == True:
    cpuh = placehold[1]
  else:
    hh = placehold[1]



  if hh < 0:
    print('Oh no you died')
    break

  if cpuh < 0:
    print('\ncongradulations you killed the monster')
    time.sleep(3)
    print('Prepare for the next monster, this one will be tougher')
    break

  placehold = computersturn(cpuh,hh, shield)

  if placehold[0] == True:
    hh = placehold[1]
  else:
    cpuh = placehold[1]

  if hh <= 0:
    print('Oh no you died')
    break

  if cpuh <= 0:
    print('\ncongradulations you killed the monster')
    time.sleep(3)
    x = random.randint(0,5)
    y=random.randint(0,5)
    print('Prepare for the next monster, this one will be tougher')
    break

hitem1 = random.randint(0,4)
hmat1 = random.randint(0,1)

hitem = material[hitem1]
hmat = items[hmat1]

herositem = hitem + ' ' + hmat

print('\nYou got a',herositem+'!','\n')

