import unittest #importing the unittest module
from credential import Credential  #importing the user class

class TestCredential(unittest.TestCase):
        '''
    Test class that defines test cases for the credential class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    
        def setUp(self):
          '''
          Set up method to run before each test cases.
          '''
          self.new_credential = Credential("tenten","scar","2580") # create credential object

        def test_init(self):
          '''
          test_init test case to test if the object is initialized properly
          '''

          self.assertEqual(self.new_credential.account_name,"tenten")
          self.assertEqual(self.new_credential.user_name,"scar")
          self.assertEqual(self.new_credential.pass_word,"2580")

        def test_save_credential(self):
          '''
        test_save_credential test case to test if the user user is saved into the credential list
          '''  
          self.new_credential.save_credential() #saving the credential
          self.assertEqual(len(Credential.credential_list),1)  

if __name__ == '__main__':
    unittest.main()





