class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] #Empt user list

    def __init__(self,user_name,password):


        """
      The __init__ method helps us define proprties of our objects
      Args:
      self.user_name = user_name
      self.password = password
        """

        self.user_name = user_name
        self.password = password


    
    
