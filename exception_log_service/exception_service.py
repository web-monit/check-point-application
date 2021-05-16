__author__ = "Manouchehr Rasouli"
__date__ = "1/Aug/2017, 3/Aug/2017"

import threading
from exception_log_service_connection import exception_logger
import time
from db_pack import db_connection_pool, use_db
from config_pack import configuration_manager


class ExceptionService:
    def __init__(self):
        self.loger = exception_logger.ExceptionLogger()
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

# the exception log service themselves handle exceptions every 20 second
    def run(self):
        while True:
            conf = configuration_manager.ConfigPack()
            try:
                if int(self.loger.check_size()) > 0:
                    # Get connection from db and insert exception in exception collection
                    pool = db_connection_pool.Pooling()
                    exception = self.loger.pop_exception()
                    connection = pool.get_connection()
                    exception_db = use_db.use_exception_db(connection)
                    exception_db.insert_error(exception)
                    print("A exception log to database !")
            except Exception as e:
                print(str(e))
            except KeyboardInterrupt as e:
                print(str(e))
            time.sleep(conf.get_exception_service_check_time())
