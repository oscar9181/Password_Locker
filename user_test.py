import unittest #importing the unittest module
from user import User 

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

    
  


