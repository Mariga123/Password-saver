import unittest # importing the unittest module
from account import Account # importing the class account

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.new_account = Account("clinton","Facebook","232323","clin@g.com") #created account object

    def test_init(self):
        """
        test_init is to test if the objects are initialized properly
        """ 
        self.assertEqual(self.new_account.user_name,"Mariga")
        self.assertEqual(self.new_account.account_name,"insta")
        self.assertEqual(self.new_account.password,"12345")
        self.assertEqual(self.new_account.email,"johnmariga8@gmail.com")