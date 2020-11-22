import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials("davido","henry","99999","dehenry@yahoo.com")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """  
        Credentials.credentials_list = [] 

    def test_init(self):
        """
        To test if the objects are initialized properly
        """  
        self.assertEqual(self.new_credentials.credentials_name,"davido")
        self.assertEqual(self.new_credentials.name,"henry")
        self.assertEqual(self.new_credentials.password,"99999")
        self.assertEqual(self.new_credentials.email, "dehenry@yahoo.com")
