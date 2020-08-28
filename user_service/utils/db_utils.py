from common.logger import get_logger
from common.utils import name_generator, password_generator
from common.aws_interface.rds_interface import RdsInterface
from clinic_db.utils.db_interface.db_interface import DbInterface
from common.aws_interface.ssm_interface import SsmInterface

class DbUtils(object):
    def __init__(self, clinic_name, identifier, password_length, engine, storage, instance_class):
        self.rds_resources = RdsInterface(identifier, engine, storage, instance_class)
        self.db_service = DbInterface()
        self.logger = get_logger(__name__)
        self.status = False
        self.db_name = clinic_name
        self.username = clinic_name + '_writer'
        self.password = password_generator(password_length)
        self.parameter_name = '/healthcare/'+clinic_name+'/db_configs/'
        self.rds_name = identifier + '-' + name_generator()
            
    def fetch_endpoints(self):
        self.logger.info('Get the list of Available Endpoints')
        return self.rds_resources.get_db_list()
    
    def db_per_cluster(self, endpoint):
        return self.db_service.count_dbs(endpoint)

    def create_rds(self):
        self.logger.info('Creating RDS Endpoint')
        return self.rds_resources.create_rds(self.rds_name)
                
    def create_db(self, endpoint):
        self.logger.info('Creating Database, User & Granting User Access to the Database')
        self.db_service.create_db(endpoint, self.db_name)
    
    def create_user(self, endpoint):    
        self.db_service.create_user(endpoint, self.username, self.password)
    
    def grant_permission(self, endpoint):
        self.db_service.grant_permission(endpoint, self.db_name, self.username, self.password)
    
    def store_credentials(self, endpoint):
        SsmInterface.put_credentials(self.parameter_name+'username', self.username)
        SsmInterface.put_credentials(self.parameter_name+'password', self.password)
        SsmInterface.put_credentials(self.parameter_name+'endpoint', endpoint['Address'])
        SsmInterface.put_credentials(self.parameter_name+'db_name', self.db_name)
            
            
        