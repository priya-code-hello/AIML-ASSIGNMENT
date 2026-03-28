
names = ["Priya", "Rahul", "Anu", "Priya", "", "Kiran"]
marks = [85, 90, None, 85, 70, 90]


unique_names = []
unique_marks = []

for i in range(len(names)):
    if names[i] not in unique_names:
        unique_names.append(names[i])
        unique_marks.append(marks[i])


for i in range(len(unique_names)):
    if unique_names[i] == "":
        unique_names[i] = "Unknown"
    if unique_marks[i] is None:
        unique_marks[i] = 0


for i in range(len(unique_names)):
    unique_names[i] = unique_names[i].capitalize()


print("Cleaned Dataset")
for i in range(len(unique_names)):
    print(unique_names[i], unique_marks[i])