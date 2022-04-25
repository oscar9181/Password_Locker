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


        def test_save_multiple_credential(self):
           '''
           test_save_multiple_credential to check if we can save multiple credential
           objects to our credential_list
           '''
           self.new_credential.save_credential()
           test_credential = Credential("Biggie","view","5555") # new credential
           test_credential.save_credential()
           self.assertEqual(len(Credential.credential_list),2) 


        def tearDown(self):
           '''
           tearDown method that does clean up after each test case has run.
           '''
           Credential.credential_list = []

        def test_delete_credential(self):
           '''
           test_delete_credential to test if we can remove a credential from our credential list
           '''
           self.new_credential.save_credential()
           test_credential = Credential("Biggie","view","555") # new credential
           test_credential.save_credential()

           self.new_credential.delete_credential()# Deleting a credential object
           self.assertEqual(len(Credential.credential_list),1) 

        def test_find_credential_by_account_name(self):
           '''
           test to check if we can find a credential by accout name and display information
           '''

           self.new_credential.save_credential()
           test_credential = Credential("Biggie","view","555") # new credential
           test_credential.save_credential()

           found_credential = Credential.find_by_account_name("Biggie")

           self.assertEqual(found_credential.pass_word,test_credential.pass_word) 

        def test_credential_exists(self):
           '''
           test to check if we can return a Boolean  if we cannot find the credential.
           '''

           self.new_credential.save_credential()
           test_credential = Credential("Facebook","George","George420") # new credential
           test_credential.save_credential()

           credential_exists = Credential.credential_exist("Facebook")

           self.assertTrue(credential_exists) 




if __name__ == '__main__':
    unittest.main()





