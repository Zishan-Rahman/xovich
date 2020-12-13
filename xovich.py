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
        self.firstnamefield.insert(0,"Named")
        self.firstnamefield.pack()
        Label(self, text="Second name").pack()
        self.secondnamefield = Entry(self, width=35)
        self.secondnamefield.pack()
        Label(self).pack()
        self.is_ilya = False
        self.addilyabox = Checkbutton(self, text="Add \"Ilya\" in the middle", variable=self.is_ilya)
        self.addilyabox.pack()
        self.setfirstaslast = Checkbutton(self, text="Set last name as first name")
        self.setfirstaslast.pack()
        Label(self).pack()
        self.processbutton = Button(self, text="Confirm selection")
        self.processbutton.pack()

    def confirmclosure(self):
        """Asks the user if they really want to close the program (before actually closing it)"""
        if messagebox.askokcancel("End","Are you sure you want to exit?!"):
            self.master.destroy()

    def checkmiddleilya(self):
        """Checks whether Ilya should be added or not."""
        pass

    def checksecondname(self):
        """Determines whether the second name button and/or entry field should be greyed out, depending on the user's choice."""
        pass

    def makeovich(self, name, if_ilya):
        """The function for actually making the new name"""
        pass

"""TODO
Create the actual processing functions
Implement the Ivanovich program in Tkinter
Change the font view on tkinter to something either better or worse
Devise some unit tests"""

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