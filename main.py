import random, replit, json
gameOver = 0
yes = {"yes","yea","y",}
no = ("n","no")
def pickWord():
  with open('wordList.json') as json_file:
      data = json.load(json_file)

  wordChoice = data[random.choice(list(data))]
  return

while 1==1:
  pickWord()
  print(wordChoice)
  startOver = input("Would you like to play again?\n \n Y/N\n").lower()
  if (startOver in yes):
    gameOver = 0
    replit.clear()
  elif (startOver in no):
    print
    exit()