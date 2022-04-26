#!/usr/bin/env python3.9
from user import User
from credential import Credential

# Create user function
def create_user(uname,password):
    '''
    Function to create a new user
    '''
    new_user = User(uname,password)
    return new_user

def login_user(user_name,pass_word):
    '''
    Function that allows an existing user to login
    '''
    new_entry = User.authenticate_user(user_name,pass_word)
    return new_entry

def save_users(user):
    '''
    Function to save a user
    '''
    user.save_users()  

def delete_users(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

    
def find_user(username):
    '''
    Function that find a user by their username and returns the user
    '''
    return User.find_by_username(username)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()



# Create credential functions
def create_credential(account,username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account,username,password)
    return new_credential

def save_credentials(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()
    
def delete_credential(credential):
    '''
    Function to delete credential
    '''
    credential.delete_credential()
    
def find_credentials(account):
    '''
    Function that finds a Credentials account name and returns the credential
    '''
    return Credential.find_by_account(account)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

    



def main():
    print("Hello Welcome to your credential list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, ex -exit the credential list ")

        short_code = input().lower()

        if short_code == 'cc':
                print("New Credential")
                print("-"*20)

                print ("account name ....")
                account_name = input()

                print ("user name ....")
                u_name = input()

                print("password ...")
                password = input()

                


                save_credentials(create_credential(account_name,u_name,password)) # create and save new credential.
                print ('\n')
                print(f"New Credential {account_name},{u_name} {password} created")
                print ('\n')

        elif short_code == 'dc':

                if display_credentials():
                        print("Here is a list of all your credentials")
                        print('\n')

                        for credential in display_credentials():
                                print(f"{credential.account_name} {credential.user_name} {credential.pass_word}")

                        print('\n')
                else:
                        print('\n')
                        print("You dont seem to have any credentials saved yet")
                        print('\n')

        elif short_code == 'fc':

                print("Enter the account name you want to search for")

                search_account_name = input()
                if check_existing_credential(search_account_name):
                        search_credential = find_credential(search_account_name)
                        print(f"{search_credential.account_name} ")
                        print('-' * 20)

                        print(f"account_name.......{search_credential.account_name}")
                        print(f"account_name.......{search_credential.account_name}")
                else:
                        print("That credential does not exist")

        elif short_code == "ex":
                print("GoodBye it was great having yout time.......")
                break
        else:
                print("I really didn't get that. Please use the short codes")
                    
if __name__ == '__main__':

    main()                               