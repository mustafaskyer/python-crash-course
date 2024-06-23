age = 1;
print("Age is", age);

age = "Welcome There!";

print("Age is", age);

pi  = 3.14;
radius = 5

area = pi * radius * radius # Area of the circle

print("Area of the circle is", area);

# division

reminder = 12 % 3
print("Reminder is", reminder);

first_name = "John";
last_name = "Doe";

full_name = first_name + " " + last_name;
print("Full Name is", full_name);


# lists operators
even_numbers = [2, 4, 6, 8, 10];
odd_numbers = [1, 3, 5, 7, 9];
all_numbers = even_numbers + odd_numbers;

print("All Numbers are", all_numbers);

# sort list
items = [
  {
  'name': 'John',
  'age': 40
  },
  {   
    'name': 'Mike',
    'age': 45
  },
  {   
    'name': 'Jane',
    'age': 33
  },
  {   
    'name': 'Asa',
    'age': 42
  }
]

def sortFn(dict):
  return dict['age']

items.sort(key=sortFn)

print("Sorted Items are", items);

# exponent operator
print("exponent", 9 ** 3)

# floor division
print("floor division", 10 // 3)

# modular
print("modular", 10 % 3)

# round
print("round", round(3.9))

# absolute
print("absolute", abs(-3.9))

# floor
print("floor", 3.9 // 1)


weeks = round((365.25  / 7), 1)

print("Weeks in a year", weeks)

################# CONVERSIONS ################
float_number = 3.14
int_number = int(float_number)
print("int_number", int_number)