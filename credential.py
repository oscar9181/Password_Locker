
class Credential:
    """
    Class that generates new instances of credential.
    """

    credential_list = [] # Empty credential list

    def __init__(self,account_name,user_name,pass_word):

      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.pass_word = pass_word

    def save_credential(self):

        '''
        save_credential method saves credential objects into credential_list
        '''

        Credential.credential_list.append(self)



