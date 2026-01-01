while True:
    resolution = input("What is one New Year resolution you have for 2026? ")

    confidence = int(input("On a scale of 1–5, how confident are you that you can reach this goal? "))

    if confidence >= 4:
        print("That's amazing! You seem very confident keep going!")
    elif confidence == 3:
        print("That’s an awesome start. If you put in effort, then you will definitely achieve this! ")
    else:
        print("That’s ok. Even if you start weak you can still end strong and meet your goal as long as you persist")

    again = input("Do you want to add another resolution? (yes/no): ").lower()

    if again == "no":
        print("Good luck with your 2026 goals! 🌟")
        break

    print()
