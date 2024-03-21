print("Welcome to the Hackathon Helper Program")
print("Please answer the following questions to get started.\n")

# Ask user for their name to personalize the program
name = input("What's your name? ")

# Ask user what they want to achieve by participating in a hackathon
goal = input(f"\nHi {name}! What do you hope to achieve by participating in a hackathon? ")


if "learn new skills" in goal.lower():
print("\nGreat goal! Here are some helpful resources you can use to learn new skills:")
