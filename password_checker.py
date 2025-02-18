import re

def passwrd_checker():
    try:
        first_name = input("What's your first name? ")  #check for first and last name
        last_name = input("What's your last name? ")  
        num = ["1234", "2468", "123", "007", "123456789", "987654321", "456", "567", "789", "678", "3456", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
        good_patterns = ["-", "!", "@", "#", "$", "%", "^", "&", "*"]

        password = input("What's your password? ")  

        weak_password = False  # Flag to track if the password is weak

        if len(password) < 12:
            weak_password = True
        else:
            for i in num:
                if re.search(i, password):
                    weak_password = True
                    break  # Exit the inner loop early if a number pattern is found

            if not weak_password: # only checks for special char if no number patterns are found
                for i1 in good_patterns:
                    if re.search(i1, password):
                        break # exit loop once a special character is found
                else: # if the inner loop doesn't break then no special chars are found
                    weak_password = True

            if re.search(first_name, password, re.IGNORECASE):
                weak_password = True

            if re.search(last_name, password, re.IGNORECASE):
                weak_password = True

        if weak_password:
            print("Your password is weak")
        else:
            print("Your password is strong")

    except ValueError as e:
        print("You somehow messed this up")

passwrd_checker()
