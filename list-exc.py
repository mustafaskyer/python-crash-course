shoes = ["Spizikes","Air Force 1","Curry 2","Melo 5"]

def addtofront (list, value) :
    list.insert(0, value)
    return list

addtofront(shoes, "White Vans")

print(shoes)