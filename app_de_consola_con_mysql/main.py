"""
Python and MySQL project:
- Open wizard
- Login or registration
- If I choose registration, it will create a user in the database
- If we choose login, it will identify the user and ask
    Create note show note, delete note.
"""

from users import actions

print("""
Available actions:
      - sign up
      - log in
""")

do = actions.Actions()
option = input("What do you want to do?: ")

if option == "sign up":
    do.sign_up()
    
elif option == "log in":
    do.log_in()