name = input("What's your name? \n")
favorite_color = input("What is your favorite color? \n")

with open("example.txt", "w") as file:
    file.write(f"{name} created this file. ")
    file.write(f"{name}'s favorite is {favorite_color}")
