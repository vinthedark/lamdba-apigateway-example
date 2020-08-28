from common.logger import get_logger
import pymysql
from user_service.config import Endpoint, Username, Password, DatabaseName

class DbInterface(object):
    
    def __init__(self):
        self.endpoint = Endpoint
        self.username = Username
        self.password = Password
        self.db_name = DatabaseName
        self.logger = get_logger(__name__)
        self.cusrorType = pymysql.cursors.DictCursor
        
    def get_connection(self):
        connection = ''
        try:
            connection = pymysql.connect(host=self.endpoint,user=self.username,password=self.password,
                                         db=DatabaseName,charset="utf8mb4",cursorclass=self.cusrorType)
        except Exception as e:
            self.logger.error('Unable to connect to the DB')
            self.logger.error("Exeception occured:{}".format(e))
        return connection       
    
    
    def close_connection(self, connection):
        if connection:
            print(connection)
            connection.close()
        
    
        
    
    
    
   
    