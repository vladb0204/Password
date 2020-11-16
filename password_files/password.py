import random
import pandas
import os
import string

columns = ['WEBSITE', 'PASSWORD']

# The example of password database:
# data = {
#     'JETBRAINS': {'WEBSITE': 'Jetbrains', 'PASSWORD': 'abcdefg1234567'}
# }

class password:


    def __init__(self, website):
        self.website = website


    # Basic length of password
    def create_password(self, length=30):
        letters = string.ascii_letters + string.digits + string.punctuation
        list_of_letters = [str(random.choice(letters)) for _ in range(length)]
        return ''.join(list_of_letters)


    # For creating new password
    def insert_password(self, length):
        global columns

        password_text = password.create_password(length)
        password_database = pandas.read_csv(r'path\to\file', index_col=0).T
        data_dict = password_database.to_dict()

        data_dict[self.website.upper()] = dict()

        data_dict[self.website.upper()]['WEBSITE'] = self.website.title()
        data_dict[self.website.upper()]['PASSWORD'] = password_text

        password_data = pandas.DataFrame(data=data_dict, index=columns).T
        password_data.to_csv(r'path\to\file')


    # If the password is already existing and you don't have it in the database
    def write_password(self, password_text):
        global columns

        password_database = pandas.read_csv(r'path\to\file', index_col=0).T
        data_dict = password_database.to_dict()

        data_dict[self.website.upper()] = dict()

        data_dict[self.website.upper()]['WEBSITE'] = self.website.title()
        data_dict[self.website.upper()]['PASSWORD'] = password_text

        password_data = pandas.DataFrame(data=data_dict, index=columns).T
        password_data.to_csv(r'path\to\file')


    # For renewing password
    def write_new_password(self, length):
        global columns

        password_text = password.create_password(length)
        password_database = pandas.read_csv(r'path\to\file', index_col=0).T
        data_dict = password_database.to_dict()

        data_dict[self.website.upper()] = dict()

        data_dict[self.website.upper()]['WEBSITE'] = self.website.title()
        data_dict[self.website.upper()]['PASSWORD'] = password_text

        password_data = pandas.DataFrame(data=data_dict, index=columns).T
        password_data.to_csv(r'path\to\file')


    def delete_password(self):
        global columns

        password_database = pandas.read_csv(r'path\to\file', index_col=0).T
        data_dict = password_database.to_dict()

        del data_dict[self.website.upper()]

        password_data = pandas.DataFrame(data=data_dict, index=columns).T
        password_data.to_csv(r'path\to\file')


    def open_file():
        os.startfile(r'path\to\file')



class passwords:


    # For inserting new password you need the following kind of list:
    # password = [['Instagram', 'qwerty12345'], ['Twitter', 'abcdef123456']]
    def write_passwords(*passwords):
        global columns

        password_database = pandas.read_csv(r'path\to\file', index_col=0).T
        data_dict = password_database.to_dict()

        for password in passwords:
            data_dict[password[0].upper()] = dict()
            data_dict[password[0].upper()]['WEBSITE'] = password[0].title()
            data_dict[password[0].upper()]['PASSWORD'] = password[1]

        password_data = pandas.DataFrame(data=data_dict, index=columns).T
        password_data.to_csv(r'path\to\file')

