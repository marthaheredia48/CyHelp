# CyHelp Starter Code
cybersecurityBirthYear = 1970

# Greets user
print("Hello! I'm CyHelp, your guide to the world of Cybersecurity.")
userName = input("What's your name? \n")
print(f"Nice to meet you, {userName}!")

# Recounts start of Cybersecurity
while True:
    todaysYear = input("What year is it? \n")
    if todaysYear.isdigit():
        timePassed = int(todaysYear) - cybersecurityBirthYear
        break
    else:
        print("Please enter a valid year.")

print(f"Wow! That means it has been {timePassed} years since Cybersecurity began!")
print("Cybersecurity started in the 1970s when more information began being stored on computer systems and networks.")
input("Press enter to continue.\n")

# Describes Cybersecurity
print("Cybersecurity refers to practices that protect computer systems and networks from digital threats.")
print("People involved in cybersecurity include governments, companies, organizations, and individuals.\n")

# Introduces CIA Triad
print("The CIA Triad is a model used to discuss cybersecurity. CIA stands for Confidentiality, Integrity, and Availability.")
giveInfo = input("Would you like to learn more about the CIA Triad? Type 'yes' or 'no':\n").lower()

# Explains pillars of CIA Triad
while giveInfo == "yes":
    print("What would you like to learn more about? Enter the letter of the following options: \n(a) Confidentiality\n(b) Integrity\n(c) Availability\n(d) None")
    topic = input().lower()

    if topic == "a":
        print("Confidentiality ensures that sensitive data remains private and is only accessible to authorized individuals.")
        print("Examples include encryption, multi-factor authentication, and access control policies.")

    elif topic == "b":
        print("Integrity ensures that data has not been tampered with and can be trusted.")
        print("Techniques like hashing and checksums help verify data integrity.")

    elif topic == "c":
        print("Availability ensures that data is accessible to authorized users when they need it.")
        print("Common methods to maintain availability include regular system maintenance, backups, and redundancy.")

    elif topic == "d":
        print("Thanks for learning about the CIA Triad!")
        break

    else:
        print("Sorry, I didn't catch that. Please choose (a), (b), (c), or (d).")

# Chatbot ends conversation
print(f"Thanks for chatting with me, {userName}, and I hope you learned something new about cybersecurity!")
