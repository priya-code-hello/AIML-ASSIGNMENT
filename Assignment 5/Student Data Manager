students = {}


for i in range(5):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks


average = sum(students.values()) / len(students)


topper = max(students, key=students.get)

print("\nStudent Data")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(name, ":", marks, "Grade:", grade)

print("\nTopper:", topper)
print("Class Average:", average)
