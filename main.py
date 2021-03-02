running = True
# Loops forever
while running:
# If he says yes it will keep on going if he says no it will cancel if he says somthing else it would print error
    Check_if_want_sign_up = input("Hello welcome to this sign up page to sign up type yes to cancel type no: ")
    if Check_if_want_sign_up == "no":
        print("Bye bye hopefully we see you again")
        running = False
    elif Check_if_want_sign_up == "yes":
        print("Ok, lets start by setting up your username and password")
        Sign_up_username = input("Create your username: ")
        Sign_up_password = input("Create a password")
        print("Now enter the credentials you just made")
        Username = ""
        Password = ""
        Tries = 0
        Out_of_tries = 5
        Show_tries = 5
        while Username != Sign_up_username or Password != Sign_up_password and Tries < Out_of_tries:
            Tries += 1
            Username = input("Enter your username: ")
            Password = input("Enter your password: ")
# If he gets it right the loop will end and will say hello to the user
            if Username == Sign_up_username and Password == Sign_up_password:
                print("Hello " + Username + " you successfully signed up")
                running = False
# If he gets it wrong it will show how many attempts he has and will cancel if he gets it wrong in less than 5 tries
            elif Username != Sign_up_username or Password != Sign_up_password:
                Show_tries -= 1
                print("You have " + str(Show_tries) + " attempts left")
    else:
        print("Error")
# Made by Abadjula#4856
