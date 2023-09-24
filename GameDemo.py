import time
from os import system, name

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def slowprint(sentence, tim):
  parsing = False
  curr = ""
  for letter in sentence:
    if letter == "<":
      parsing = True
      num = ""
      continue
    if not parsing:
      clear()
      curr += letter
      print(curr)
      time.sleep(tim / len(sentence))
    else:
      if letter != ">":
        num += letter
      else:
        parsing = False
        time.sleep(int(num))

def death():
  slowprint("I gave you your chances<1>.<1>.<1>.<1>", 10)

while True:
  dead = False
  lives = 3
  slowprint(OKCYAN + """you wake up to your alarm at 6 am. You have to go to school at 8 a jog in before then, but you're still sleepy. <3>

                                                            do you:
                                          press snooze        or        wake up

  """, 8)
#----------------------------------------------------------------------------------------------
  
  #--------
  while True:
    option = input().lower()
    
    if option not in "press snooze,wake up".split(","):
      lives -= 1
      if lives == 0:
        dead = True
        break
      slowprint("""please input one of the two options
        
                                   do you:
                press snooze        or        wake up""", 8)
    else:
      break
  #--------
  if dead:
    death()
    continue
  #make it so that if they input incorrectly they lose one of their lives. One level will require you to die to proceed onwards.
#----------------------------------------------------------------------------------------------

  if option == "press snooze":
    slowprint("""You continue sleeping in, making an exception for your morning jog today. You sleep for another hour, and you get out of bed.<3>
    
                                                                  do you:
                                                  make your bed     or     brush your teeth""", 6)
    lives = 3
    option = input()
#----------------------------------------------------------------------------------------------
    if option == "brush your teeth":
      lives = 3
      clear()
      time.sleep(3)
      slowprint(OKCYAN + """you go straight to brushing your teeth, leaving your parents to do your bed. It's time to make breakfast.
                                                    
                                                    do you:
          wait for your mom to make you breakfast     or     make eggs""", 6)
      lives = 3
      dead = False
      #--------
      while True:  
        option = input()
        if option not in "wait for your mom to make you breakfast,make eggs".split(","):
          lives -= 1
          if lives == 0:
            dead = True
            break
          slowprint("""please input one of the two options
        
                                                  do you:
        wait for your mom to make you breakfast     or     make eggs""", 8)
        else:
          break
      #--------
      if dead:
        death()
        continue
#----------------------------------------------------------------------------------------------
      if option == "wait for your mom to make you breakfast":
        lives = 3
        clear()
        slowprint(".<1>.<1>.<2>", 3)
        slowprint(FAIL + """do you believe in ghosts
                       
                      yes   or   no""", 5)
        #--------
        while True:
          option = input().lower()
          if option not in "yes,no".split(","):
            lives -= 1
            if lives == 0:
              dead = True
              break
            slowprint("""please input one of the two options
            
                yes   or   no""", 3)
          else:
            break
        #--------
        if dead:
          death()
          continue
#----------------------------------------------------------------------------------------------    
    elif option == "make your bed":
      lives = 3
      slowprint("""Phew! You saved yourself from some trouble. You make your bed and then head onto breakfast. You whip up some quick cereal, and get ready for school. You realize you forgot to do your homework.
      
                                                                                      do you:
                                                        quickly make up some answers     or     leave it and make excuses at school""", 10)
      #--------
      while True:
        option = input()
        if option not in "quickly make up some answers,leave it and make excuses at school".split(","):
          lives -= 1
          if lives == 0:
            dead = True
            break
          slowprint("""please input one of the two options
        
                                    do you:
     quickly make up some answers     or     leave it and make excuses at school""", 8)
        else:
          break
      #--------
      if dead:
        death()
        continue
#----------------------------------------------------------------------------------------------
  elif option == "wake up":
    lives = 3
    slowprint("""You wake up at your normal time and make your bed shortly after. You are considering your breakfast choices.<3>
                                                                
                                                                do you:
                                                    make eggs     or     eat a quick cookie""", 8)
    #--------
    while True:
      option = input()
      if option not in "make eggs,eat a quick cookie".split(","):
        lives -= 1
        if lives == 0:
          dead = True
          break
        slowprint("""please input one of the two options
        
                                    do you:
                        make eggs     or     eat a quick cookie""", 8)
      else:
        break
    #--------
    if dead:
      death()
      continue
#----------------------------------------------------------------------------------------------
    if option == "make eggs":
      lives = 3
      slowprint("""You approach the fridge, and take out two eggs. You whip up a nice egg breakfast with toast on the side. You gobble up your breakfast in minutes, and head out for your run. Midway through your run, you encounter an old lady. She asks you a question, but you can't hear her properly. What do you reply with?<3>
      
                                                        do you:
                                      ask her to repeat   or    answer with yes""", 20)
      #--------
      while True:
        option = input()
        if option not in "ask her to repeat,answer with yes".split(","):
          lives -= 1
          if lives == 0:
            dead = True
            break
          slowprint("""please input one of the two options
          
                                      do you:
                  ask her to repeat     or     answer with yes""", 8)
        else:
          break
      #--------
      if dead:
        death()
        continue
#----------------------------------------------------------------------------------------------

    if option == "eat a quick cookie".split(","):
      lives = 3
      slowprint("""You go to eat a quick cookie as to maximize your excercise duration. You gobble up the cookie and go on for your run. You note an old lady crossing an intersection behind you. For some reason you feel relived<1>.<1>.<1>.<3> You finish your run and get back home. You debate wether or not to check your school bag.
                                                       
                                                       do you:
                                          check your bag   or   play games until school""", 20)
      #--------
      while True:
        option = input()
        if option not in "check your bag,play games until school".split(","):
          lives -= 1
          if lives == 0:
            dead = True
            break
          slowprint("""please input one of the two options
          
                                      do you:
                      check your bag    or   play games until school""", 8)
        else:
          break
      #--------
      if dead:
        death()
#----------------------------------------------------------------------------------------------