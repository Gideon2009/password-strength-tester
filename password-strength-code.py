def password_checker():
    score = 0
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    symbols = ['=', '+', '-', '_', '/', '@', '&', '(', ')', '#', "`", "~"]
    password_char = []
    up_flag = False
    low_flag = False
    num_flag = False
    sym_flag = False
    while True:
        menu = input("Would you like to 1) check the strength of a password or 2) quit? ")
        if '1' in menu:
            password = input("What is the password you would like to check? ")
            password_length = len(password)
            if 8 <= password_length <= 24:
                for char in password:
                    password_char.append(char)
                for character in password_char:
                    if character in upper:
                        score += 5
                        up_flag = True
                        break
                if up_flag == False:
                    score -= 5
                for character in password_char:
                    if character in lower:
                        score += 5
                        low_flag = True
                        break
                if low_flag == False:
                    score -= 5
                for character in password_char:
                    if character in numbers:
                        score += 5
                        num_flag = True
                        break
                if num_flag == False:
                    score -= 5
                for character in password_char:
                    if character in symbols:
                        score += 5
                        sym_flag = True
                        break
                if sym_flag == False:
                    score -= 5
                if password_char in upper and password_char in lower and password_char in numbers and password_char in symbols:
                    score += 5
                score += password_length
                if score == 0:
                    print("Your password is a mediocre password.")
                elif 11 <= score <= 44:
                    print("You have an okay password.")
                elif 45 <= score <= 59:
                    print("Your password is amazing. It would be very hard to crack.")
                elif 1 <= score <= 10:
                    print("You have a weak password.")
                elif score == -1 or score == -2:
                    print("You have a very weak password.")
            else:
                print("Your entered password doesn't fit in the required range of characters, which is 8 to 24.")
        else:
            break
