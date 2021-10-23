import random, replit, json
gameOver = 0
yes = {"yes","yea","y",}
no = ("n","no")
x = 1
def pickWord(x):
  x = random.choice(open("wordList.txt").read().split())
  print (x)
  return x
while 1==1:
  x = pickWord(x)
  print(x)
  startOver = input("Would you like to play again?\n \n Y/N\n").lower()
  if (startOver in yes):
    gameOver = 0
    replit.clear()
  elif (startOver in no):
    print
    exit()