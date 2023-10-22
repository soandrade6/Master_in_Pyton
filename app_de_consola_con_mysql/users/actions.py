import users.user as model
import notes.actions

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
            print(f"\nPerfect {register[1].name} you have registered correctly with the email {register[1].email}")
        else:
            print("\nYou have not registered correctly")  

    def log_in(self):
        print("\nOK, login to the system")

        try:
            email = input("Enter  your email: ")
            password = input("Enter a password: ")

            user = model.User('', '', email, password)
            login = user.log_in()

            if email == login[3]:
                print(f"\nWelcome {login[1]}, you have been register in the system on {login[5]}")
                self.next_actions(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("Incorrect login, try again")

    def next_actions(self, user):
        print("""
        Acailable actions:
              - Create note (create)
              - Show your notes (show)
              - Delete note (delete)
              - Exit (exit)
        """)
        action = input("What do you want to do: ")
        do = notes.actions.Actions()

        if action == "create":
            do.create(user)
            self.next_actions(user)

        elif action == "show":
            do.show(user)
            self.next_actions(user)

        elif action == "delete":
            do.delete(user)
            self.next_actions(user)
        
        elif action == "exit":
            print(f"See you later {user[1]}")
            exit()