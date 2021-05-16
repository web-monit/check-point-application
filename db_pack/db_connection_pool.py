__author__ = "Manouchehr Rasouli"
__date__ = "2/Aug/2017"

from pymongo import MongoClient
from config_pack import configuration_manager
from pymongo.errors import ConnectionFailure
from exception_log_service_connection import exception_logger
import datetime


class Pooling:
    def __init__(self):
        self.manager = configuration_manager.ConfigPack()
        self.db_max_pool = self.manager.get_db_max_pool()
        self.db_wait_pool = self.manager.get_db_wait_queue_multiple()
        self.db_wait_pool_time_out = self.manager.get_db_wait_queue_timeout_ms()
        self.db_host_url = self.manager.get_db_host()
        self.db_host_port = self.manager.get_db_host_port()

    def get_db_host_url(self):
        return self.db_host_url

    def get_db_host_port(self):
        return self.db_host_port

    def get_connection(self):
        client = MongoClient(self.db_host_url, self.db_host_port, maxPoolSize = self.db_max_pool, waitQueueMultiple = self.db_wait_pool, waitQueueTimeoutMS = self.db_wait_pool_time_out)
        try:
            # The ismaster command is cheap and does not require auth.
            client.admin.command('ismaster')
        except ConnectionFailure as e:
            error = {"service_name" : "dbpack/db_connection_pool.pooling", "date" : datetime.datetime.now().strftime("%y/%m/%d %H:%M"), "exception" : str(e)}
            logger = exception_logger.ExceptionLogger()
            logger.put_exception(error)
        return client
