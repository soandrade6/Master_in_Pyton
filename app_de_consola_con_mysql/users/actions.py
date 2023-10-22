import users.user as model

class Actions:

    def sign_up(self):
        print("\nOk, lets to sing up in the system")
        name = input("What is your name?: ")
        last_name = input("What are your last names?: ")
        email = input("Enter  your email: ")
        password = input("Enter a password: ")

        user = model.User(name, last_name, email, password)
        register = user.sign_up()

        if register[0] >= 1:
            print(f"Perfect {register[1].name} you have registered correctly with the email {register[1].email}")
        else:
            print("You have not registered correctly")  

    def log_in(self):
        print("\nOK, login to the system")
        email = input("Enter  your email: ")
        password = input("Enter a password: ")