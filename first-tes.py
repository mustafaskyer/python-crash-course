pointPossivle = 37;
score = 90;
studentName = "Mu";

'''
A - 100 - 90%
B - 89 - 80%
C - 79 - 70%
D - 69 - 60%
F - 59 - 0%
'''

grade = ""
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("{}: - {} ".format(studentName, grade))
