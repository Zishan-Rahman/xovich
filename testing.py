"""
For creating several unit tests for the Xovich program.
"""

import unittest
#import mock
from xovich import *

class TestXovich(unittest.TestCase):
    """Tests of the main Xovich program are stored in this class"""
    
    def setUp(self):
        """Creates a new Xovich window to be tested"""
        self.roor = createGUI()
        return super().setUp()

    def test1_MakeName(self):
        """TEST 1. EXPECTED: \"Play Ilya Testovich\""""
        #self.testMakeGUI()
        self.roor.firstnamefield.delete(0,END)
        self.roor.firstnamefield.insert(0,"Play")
        self.roor.lastnamefield.delete(0,END)
        self.roor.lastnamefield.insert(0,"Test")
        self.roor.addilyabox.invoke()
        #self.roor.setfirstaslast.invoke()
        self.assertEqual(self.roor.makeovich(),"Play Ilya Testovich")
        #self.roor.processbutton.invoke()

    def test2_MakeNameWithNothing(self):
        """TEST 2. EXPECTED: \"I Don't Got No Nameovich\" then \"Ilya I Don't Got No Nameovich\""""
        self.roor.firstnamefield.delete(0,END)
        self.roor.lastnamefield.delete(0,END)
        self.assertEqual(self.roor.makeovich(),"I Don't Got No Nameovich")
        #self.roor.processbutton.invoke()
        self.roor.addilyabox.invoke()
        self.assertEqual(self.roor.makeovich(),"Ilya I Don't Got No Nameovich")
        #self.roor.processbutton.invoke()

    def test3_MakeNameSameFirstName(self):
        """TEST 3. EXPECTED: \"Testing Ilya Testingovich\""""
        self.roor.firstnamefield.delete(0,END)
        self.roor.firstnamefield.insert(0,"Testing")
        self.roor.addilyabox.invoke()
        self.roor.setfirstaslast.invoke()
        self.assertEqual(self.roor.makeovich(),"Testing Ilya Testingovich")
        #self.roor.processbutton.invoke()

    def tearDown(self):
        """Cleans up the test area after it's done"""
        try:
            self.roor.master.destroy()
        except:
            pass
        return super().tearDown()

if __name__ == "__main__":
    """Runs all the tests when executed from main"""
    unittest.main(verbosity=2)