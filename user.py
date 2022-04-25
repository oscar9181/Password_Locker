class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] #Empt user list

    def __init__(self,user_name,pass_word):
        """
        The __init__ method helps us define proprties of our objects
        Args:
            self.user_name = user_name
            self.password = password
        """
        self.user_name = user_name
        self.pass_word = pass_word


              
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)  



    def save_user(self):
        '''
        save_contact method saves contact objects into contact_list
        '''
        User.user_list.append(self)

    
    
    @classmethod
    def find_by_user_name(cls,user_name):
            '''
            Method that takes in a username and returns a user that matches that username.
            Args:
                username: name to search for
            Returns :
                user of person that matches the username.
            '''

            for user in cls.user_list:
                if user.user_name == user_name:
                    return user        
       
    @classmethod
    def user_exist(cls,user_name):
            '''
            Method that checks if a user exists from the user list.
            Args:
                user_name: user_name to search if it exists
            Returns :
                Boolean: True or false if the user exists
            '''
            for user in cls.user_list:
                if user.user_name == user_name:
                        return True

            return False               

