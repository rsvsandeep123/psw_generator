import random


def generatepassword(pwlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for i in range(len(pwlength)):  # Iterate over the length of pwlength
        password = ""
        for j in range(pwlength[i]):  # Use pwlength[i] instead of i
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]

        password = replacewithnumber(password)
        password = replacewithuppercaseletter(password)

        passwords.append(password)

    return passwords


def replacewithnumber(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword  # Moved outside the loop


def replacewithuppercaseletter(pword):
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword  # Moved outside the loop


def main():
    numpasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numpasswords) + " passwords")

    passwordlengths = []

    print("Minimum length of password should be 3")

    for i in range(numpasswords):
        length = int(input("Enter the length of Password #" + str(i + 1) + " "))
        if length < 3:
            length = 3
        passwordlengths.append(length)

    password = generatepassword(passwordlengths)

    for i in range(numpasswords):
        print("Password #" + str(i + 1) + " = " + password[i])


main()
