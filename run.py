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
    user.save_user()  

def delete_user(user):
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
def create_credential(account_name,user_name,pass_word):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(account_name,user_name,pass_word)
    return new_credential

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credentials()
    
def delete_credential(credential):
    '''
    Function to delete credential
    '''
    credential.delete_credential()
    
def find_credential(account):
    '''
    Function that finds a Credentials account name and returns the credential
    '''
    return Credential .find_by_account(account)

def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credential()