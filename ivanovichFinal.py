# original file
# originally written by Kabilan Thesingarajah (https://github.com/KabilanThesingarajah)
# https://github.com/KabilanThesingarajah/ovich
# not in one line anymore, ha!

def originalXovich():
    """The original \"ovich\" line of code, now placed in its own function!"""
    print("Hello,", ''.join(*[[input("what is your name?:")+" "]*2])[:-1]+"ovich")

if __name__ == "__main__":
    """Runs the original line of code (once) when the file is run from the command line."""
    originalXovich()
