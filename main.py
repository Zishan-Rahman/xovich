from tkinter import *
from tkinter import messagebox

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
        self.firstnamefield.pack()
        Label(self, text="Second name").pack()
        self.secondnamefield = Entry(self, width=35)
        self.secondnamefield.pack()
        Label(self).pack()
        self.addilyabox = Checkbutton(self, text="Add \"Ilya\" in the middle")
        self.addilyabox.pack()
        Label(self).pack()
        self.processbutton = Button(self, text="Confirm selection")
        self.processbutton.pack()

    def confirmclosure(self):
        if messagebox.askokcancel("End","Are you sure you want to exit?!"):
            self.master.destroy()

"""TODO
Create the actual processing functions
Implement the Ivanovich program in Tkinter"""

def createGUI():
    """Creates the, well, GUI!"""
    root = Tk()
    root.title("Xovich")
    root.geometry("500x300")
    xovich = Main(root)
    root.mainloop()

if __name__ == "__main__":
    createGUI()