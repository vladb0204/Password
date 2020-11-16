import random
import pandas
import os
import string

columns = ['WEBSITE', 'PASSWORD']

class password:


    def __init__(self, website):
        self.website = website


    # Needed to truncate code
    def renew_databse(self, password_database, password_text):
        pass


    # Basic length of password
    def create_password(self, length=30):
        letters = string.ascii_letters + string.digits + string.punctuation
        list_of_letters = [str(random.choice(letters)) for _ in range(length)]
        return ''.join(list_of_letters)


    # For creating new password
    def insert_password(self, length):
        global columns

        password_text = password.create_password(length)
        password_database = pandas.read_csv("password_files/password_database.csv", index_col=0).T
        data_dict = password_database.to_dict()

        data_dict[self.website.upper()] = dict()

        data_dict[self.website.upper()]['WEBSITE'] = self.website.title()
        data_dict[self.website.upper()]['PASSWORD'] = password_text

        password_data = pandas.DataFrame(data=data_dict, index=columns).T
        password_data.to_csv("password_files/password_database.csv")


    # If the password is already existing and you don't have it in the database
    def write_password(self, password_text):
        global columns

        password_database = pandas.read_csv("password_files/password_database.csv", index_col=0).T
        data_dict = password_database.to_dict()

        data_dict[self.website.upper()] = dict()

        data_dict[self.website.upper()]['WEBSITE'] = self.website.title()
        data_dict[self.website.upper()]['PASSWORD'] = password_text

        password_data = pandas.DataFrame(data=data_dict, index=columns).T
        password_data.to_csv("password_files/password_database.csv")


    # For renewing password
    def write_new_password(self, length):
        global columns

        password_text = password.create_password(length)
        password_database = pandas.read_csv("password_files/password_database.csv", index_col=0).T
        data_dict = password_database.to_dict()

        data_dict[self.website.upper()] = dict()

        data_dict[self.website.upper()]['WEBSITE'] = self.website.title()
        data_dict[self.website.upper()]['PASSWORD'] = password_text

        password_data = pandas.DataFrame(data=data_dict, index=columns).T
        password_data.to_csv("password_files/password_database.csv")


    def delete_password(self):
        global columns

        password_database = pandas.read_csv("password_files/password_database.csv", index_col=0).T
        data_dict = password_database.to_dict()

        del data_dict[self.website.upper()]

        password_data = pandas.DataFrame(data=data_dict, index=columns).T
        password_data.to_csv("password_files/password_database.csv")


    def open_file():
        os.startfile("password_files/password_database.csv")



class passwords:


    # For inserting new password you need the following kind of list:
    # password = [['Instagram', 'qwerty12345'], ['Twitter', 'abcdef123456']]

    # Or, if you want to download file or string with passwords, you can upload file with passwords to this repository usign this format:
    # --------------------------------
    # Website_1 a9843hgp938gh83389h
    # Website_2 4ru93g8vh984hg09385gh08h038hg
    # Website_3 r8934hv981hg8391gh380gh038
    # Webiste_4 328ry3479gh493hg3h48gh80gh043
    # Webiste_5 ir3209ru40fu498gh498hg938hg3804h0

    # Type of input_data:
    # file - from file

    # string - from string
    # If your data is ended, then type 0 to end process

    def format_data(choice):
        database = []

        if choice.lower() == 'file':
            file_name = input("Input directory to file: ")
            try:
                file_open = open(file_name, 'r')

                data = [elem.replace('\n', '').split(' ') for elem in file_open.readlines()]
                
                for line in data:
                    database.append([line[0], line[1]])

                file_open.close()
            
            except FileNotFoundError:
                print("Wrong input of file directory")
                passwords.format_data(choice)


        elif choice.lower() == 'string':
            while True:
                string = input()
                if string == '0':
                    break
                
                string = string.split(' ')
                database.append([string[0], string[1]])

        passwords.write_passwords(database)


    def write_passwords(passwords):
        global columns

        password_database = pandas.read_csv("password_files/password_database.csv", index_col=0).T
        data_dict = password_database.to_dict()

        for password in passwords:
            data_dict[password[0].upper()] = dict()
            data_dict[password[0].upper()]['WEBSITE'] = password[0].title()
            data_dict[password[0].upper()]['PASSWORD'] = password[1]

        password_data = pandas.DataFrame(data=data_dict, index=columns).T
        password_data.to_csv("password_files/password_database.csv")