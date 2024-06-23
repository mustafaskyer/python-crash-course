try:
  age = int(input("Enter your age: "))
  print("I see that you are %d years old." % age)
except Exception:
  print("You entered an invalid value.")