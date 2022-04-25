import unittest #importing the unittest module
from user import User  #importing the user class

class TestUser(unittest.TestCase):


      '''
      Test class that defines test cases for the contact class behaviours.

      Args:
        unittest.TestCase: TestCase class that helps in creating test cases
      '''
      def setUp(self):
          """
          Set up method to run before each test cases.
          """
          self.new_user = User("Oscarero","oscar9181") # create user object

      def test__init(self):
          """
          test__init test case to test if the object is initialized properly
          """
          self.assertEqual(self.new__user.user_name,"Oscarero")
          self.assertEqual(self.new__user.pass_word,"oscar9181")


      def test_save_user(self):
          '''
          test_save_contact test case to test if the user object is saved into
          the user list
          '''
          self.new_user.save_user() # saving the new user
          self.assertEqual(len(User.user_list),1)




      def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Sharon","shaz") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)



      def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


      def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Sharon","shaz") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2) 


      def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a contact from our user list
        '''
        self.new_user.save_user()
        test_user = User("Sharon","shaz") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)
  




if __name__ == '__main__':
    unittest.main()





    



