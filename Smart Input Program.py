

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")


if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 35:
    category = "Young Adult"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"


print("\n--- Personalized Message ---")
print(f"Hello {name}!")
print(f"You are {age} years old and belong to the {category} category.")
print(f"It's great that you enjoy {hobby}!")
print("Keep learning and have a wonderful day!")