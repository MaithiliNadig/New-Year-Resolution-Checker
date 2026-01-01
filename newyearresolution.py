from datetime import date

name = input("What is your name? ")

today = date.today()

while True:
    resolution = input("What is one New Year resolution you have for 2026? ")

    confidence = int(input("On a scale of 1-5, how confident are you that you can reach this goal? "))

    if confidence >= 4:
        print("That's amazing! You seem very confident—keep going!")
    elif confidence == 3:
        print("That’s a great start. If you put in effort, you will achieve this!")
    else:
        print("That’s okay. You can still meet your goal if you keep trying!")

    
    file = open("resolutions.txt", "a") # Opens new flie and adds text
    file.write(name + "\n") # Saves the user's name
    file.write(str(today) + "\n") # Saves the date
    file.write(resolution + "\n") # Saves the user's resolution
    file.write("Confidence: " + str(confidence) + "/5\n") # Saves how confident the user is about meeting their goal out of 5
    file.write("--------------------\n") # Ending line 
    file.close()

    again = input("Do you want to add another resolution? (yes/no): ").lower()

    if again == "no":
        print("Good luck with your 2026 goals!")
        break

    print()
