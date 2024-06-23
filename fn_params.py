def sum(num1, num2):
  try:
    num1 = int(num1)
    num2 = int(num2)
    sumResult = num1 + num2
    if(sumResult > 10):
      print("Gt 10")
  except Exception:
    print("Invalid input")
  else:
    print("Not gt 10")
sum(1, 2)