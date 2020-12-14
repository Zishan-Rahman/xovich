from tkinter import *
from tkinter import messagebox#, font

class Main(Frame):
    """The GUI"""
    
    def __init__(self, GUIman):
        """Initalises the GUI itself"""
        super(Main, self).__init__(GUIman)
        self.master.protocol("WM_DELETE_WINDOW",self.confirmclosure)
        self.pack()
        self.create()
    
    def create(self):
        """Create the fields for the user to play with."""
        Label(self, text="Enter a name and (optionally) a second name. Expect an -ovich at the end!\nYou can also add an \"Ilya\" at the middle!").pack()
        Label(self).pack()
        Label(self, text="First name").pack()
        self.firstnamefield = Entry(self, width=35)
        self.firstnamefield.insert(0,"Example")
        self.firstnamefield.pack()
        Label(self, text="Last name").pack()
        self.lastnamefield = Entry(self, width=35)
        self.lastnamefield.insert(0, "Named")
        self.lastnamefield.pack()
        Label(self).pack()
        self.ilya = IntVar()
        self.addilyabox = Checkbutton(self, text="Add \"Ilya\" in the middle", variable=self.ilya)
        self.addilyabox.pack()
        self.fal = IntVar()
        self.setfirstaslast = Checkbutton(self, text="Set last name as first name", command=self.greyout, state=NORMAL, variable=self.fal)
        self.setfirstaslast.pack()
        Label(self).pack()
        Button(self, text="Confirm selection", command=self.confirm_makeovich).pack()

    def greyout(self):
        """Greys out the "last name" field if the user wants it to be the same as their first name"""
        #print(self.fal.get())
        if self.fal.get() == 1:
            self.lastnamefield.config(state=DISABLED)
        else:
            self.lastnamefield.config(state=NORMAL)

    def confirmclosure(self):
        """Asks the user if they really want to close the program (before actually closing it)"""
        if messagebox.askyesno("End","Are you sure you want to exit?!"):
            self.master.destroy()

    def confirm_makeovich(self):
        """Checks if the user wants \"Ilya\" in the middle of their name"""
        if messagebox.askyesno("Confirm Xovich Processing", "Are you sure you want to try the Xovich program?\nClick \"Cancel\" to go back and change it."):
            messagebox.showinfo("New name", f"Your new name is {self.makeovich()}!")

    def makeovich(self):
        """The function for actually making the new name"""
        firstname = self.firstnamefield.get()
        if self.lastnamefield.cget('state') == DISABLED:
            lastname = firstname
        else:
            lastname = self.lastnamefield.get()
        if self.ilya.get() == 1:
            newname = firstname + " Ilya " + lastname
        elif len(firstname) != 0 and len(lastname) != 0:
            newname = firstname + " " + lastname
        elif len(firstname) == 0:
            newname = lastname
        elif len(lastname) == 0:
            newname = firstname
        newname += "ovich"
        #print(newname)
        return newname

"""TODO
Change the font view on tkinter to something either better or worse
Devise some unit tests and try to automate the creation of names for unit testing purposes"""

def createGUI():
    """Creates the, well, GUI!"""
    root = Tk()
    root.title("Xovich")
    root.geometry("500x325")
    xovich = Main(root)
    return root

if __name__ == "__main__":
    """What to run when executed"""
    createGUI().mainloop()