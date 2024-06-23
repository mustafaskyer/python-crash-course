# sets is a collection of unique elements
faveGames = {"Game 1", "Game 2", "Game 3", "Game 3"}; # it will only print Game 3 once. meaning it will remove duplicates
faveGames2 = {"Game 4", "Game 5", "Game 6", "Game 7"};
# print(faveGames)
faveGames("Game 4")
for game in faveGames:
    print(game) # it prints in random order

# to remove an item we have remove, or discard
# remove will trhow error if the item is not in the set
# discard will not throw error if the item is not in the set