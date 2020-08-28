from user_service.utils.db_interface.db_interface import DbInterface
from common.logger import get_logger

class UserService(object):
    def __init__(self):
        self.db_interface = DbInterface()
        self.logger = get_logger(__name__)
        
    def insert_user(self, firstname, lastname, email, phonenumber):
        statement = "INSERT INTO Users(firstname,lastname,email,phonenumber) " \
            "VALUES(%s,%s,%s,%s)"
        arguments = (firstname, lastname, email, phonenumber)
        success = True
        try:
            connection = self.db_interface.get_connection()
            if not connection:
                raise ValueError('Could not establish connection to create User')
            cursor = connection.cursor()
            cursor.execute(statement, arguments)
            connection.commit()
            print('Framing Sentence')
        except Exception as e:
            self.logger.error('Failed to create user')
            self.logger.error("Exeception occured:{}".format(e))
            success = False
        finally:
            self.db_interface.close_connection(connection)
            return success