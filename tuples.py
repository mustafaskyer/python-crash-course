# A tuple is a list that is immutable. It is defined using parentheses instead of square brackets.
# Immutable means that once a tuple is created, it cannot be changed. You cannot add, remove, or change elements in a tuple.

# faveGames = ("Game 1", "Game 2", "Game 3");
# print(type(faveGames))

shoes = ("Spizikes","Air Force 1","Curry 2","Melo 5")

def appendtotuple(thetuple, value):
    updatedTuple = thetuple + (value,)
    return updatedTuple

shoes = appendtotuple(shoes, "White Vans")
print(shoes)
    