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



