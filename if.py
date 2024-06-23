status = 1

if status == 1:
  print("Status is 1")
elif status == 2:
  print("Status is 2")
else :
  print("Status is 3")


year = 1830 # When you check your solution, don't change this number

if year >= 2100 <= 2000:
    print("Welcome to the 21st century!")
else:
    print("You are before or after the 21st century")

# And -- Or

name = "John"
age = 40

if name == "John" and age == 40:
    print("Your name is John, and you are also 40 years old.")
else:
    print("You are not John, nor are you 40 years old.")

if name == "John" or name == "Rick":
    print("Your name: ", name)
else:
    print("Your name is neither John nor Rick.")