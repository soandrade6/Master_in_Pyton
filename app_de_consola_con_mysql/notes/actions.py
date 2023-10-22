import notes.note as model

class Actions:

    def create(self, user):
        print(f"\nOK {user[1]}, lets to create a note...")

        title = input("Enter a title: ")
        description = input("Enter a description of your note: ")

        note = model.Note(user[0], title, description)
        save = note.save()

        if save[0] >= 1:
            print(f"\n Perfect, you  {note.title} has been save sucessfull")
        else:
            print(f"\n Sorry {user[1]}, your note has not been saved correctly")

    def show(self, user):
        print(f"\nOk {user[1]} here are your notes: ")

        note = model.Note(user[0])
        notes = note.show()

        for note in notes:
            print("\n**************************************************")
            print(note[2])
            print(note[3])
            print("*****************************************************") 


    def delete(self, user):
        print(f"\n OK {user[1]}, lets delete notes")

        title = input("Enter de title of the note that you want to delete: ")

        note = model.Note(user[0], title)
        delete = note.delete()

        if delete[0] >= 1:
            print(f"\n We have delete teh note: {note.title}")
        else:
            print(f"We dont have delete the note: {note.title}, try again")