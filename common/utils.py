import string
import random

def name_generator(size=4, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

def password_generator(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

def read_data_from_file(file_name):
    data=""
    with open(file_name) as file:
        for line in file:
            data+=line
    return data