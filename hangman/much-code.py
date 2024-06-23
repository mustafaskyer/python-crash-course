lives = 19;

stringword = "Apple"
word = list(stringword.lower())
winner = False

inCorrectLetters = [];

def printScore(word):
  print("Score: " + str(word))

while lives > 0 and winner == False:
  # print out the current scoreboard
  # Ask the user for a letter
  # check if they won
  lives -= 1
  printScore(word)
  print("Lives: " + str(lives))
  
if lives <= 0:
  print("eYou lost! The word was: " + "", word);
else:
  print("You won! The word was: " + "", word);