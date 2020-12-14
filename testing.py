import unittest
from xovich import *

class TestXovich(unittest.TestCase):
    """Tests the class"""
    
    def setUp(self):
        """Creates a new Xovich window to be tested"""
        self.roor = createGUI()
        #return super().setUp()    #I don't know, that line might probably be pointless

    def testMakeGUI(self):
        self.roor.mainloop()

    def testMakeName(self):
        pass

    def tearDown(self):
        """Cleans up the test area after it's done"""
        try:
            self.roor.destroy()
        except:
            pass
        return super().tearDown()

if __name__ == "__main__":
    unittest.main(verbosity=2)