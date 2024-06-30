import random
print('''  /$$$$$$                                               /$$      /$$          
 /$$__  $$                                             | $$$    /$$$          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$      | $$$$  /$$$$  /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      | $$ $$/$$ $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$       | $$  $$$| $$| $$$$$$$$
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$      | $$\  $ | $$| $$_____/
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/      | $$ \/  | $$|  $$$$$$$
 \______/  \______/  \_______/|_______/|_______/       |__/     |__/ \_______/
                                                                              
                                                                              
                                                                              ''')


number = random.randint(1,101)
print("I am thinking of a number btw 1 and 100 .")
diff=input("Choose the difficulty . Eary / Hard ")
if diff=="easy" :
  chances=10
else:
  chances=5
while chances >0:
  guess=int(input("Guess the number "))
  if guess>number:
    print("Try lesser number ! ")
    chances-=1
    print(f"You have {chances} chances left ! ")
  elif guess<number:
    print("Try greater number ! ")
    chances-=1
    print(f"You have {chances} chances left ! ")
  elif guess==number :
    print("You Won ! ")
    chances-=1
    print(f"You have {chances} chances left ! ")
    break

print(f"The number is {number}")
# else:
#   print(f"You Loose ! The number is {number}")