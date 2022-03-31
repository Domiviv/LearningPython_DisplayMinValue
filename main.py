ages = []
names = []
while True:  # Infinite loop
    # Ask for persons' name
    name = input("What's the name of this person? ")
    if name == "":
        break

    # Ask for persons' age
    age = input("Enter his age? ")
    if age == "":
        break

    names.append(name)
    ages.append(int(age))

# Setup the youngest one
minAge = ages[0]
i = 0
for age in ages:
    if age < minAge:
        minAge = age
        youngestPersonIndex = i
    i = i + 1

print(f"Youngest Person : {names[youngestPersonIndex]} is {ages[youngestPersonIndex]} yo.")

