__author__ = "Manouchehr Rasouli"
__date__ = "3/Aug/2017, 8/Aug/2017, 11/Aug/2017"

from multiprocessing.dummy import Pool as ThreadPool
import threading
import time
import datetime
from config_pack import configuration_manager
from exception_log_service_connection import exception_logger
from interupt_service_connector import inter_upt_logger
from db_pack import db_connection_pool, use_db
from app_main_service.up_and_speed_test import up_and_speed_test


class StartMainService:
    def __init__(self):
        self.conf = None
        self.pool = None
        self.url_list = None
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            try:
                self.conf = configuration_manager.ConfigPack()
                self.pool = db_connection_pool.Pooling()
                connection = self.pool.get_connection()
                url_db = use_db.use_url_db(connection)
                self.url_list = url_db.get_urls_as_list()
                result_list = self.__calculate_parallel__()
                result_db = use_db.use_result_db(connection)
                if len(result_list) is not 0:
                    result_db.inser_results_as_list(result_list)
                time.sleep(self.conf.get_update_time())
            except Exception as e:
                error = {"service_name": "app_main_service/main_service", "date": time.strftime("%d/%m/%Y %I:%M"),
                         "exception": str(e)}
                logger = exception_logger.ExceptionLogger()
                logger.put_exception(error)

    # function to be mapped over
    def __calculate_parallel__(self):
        pool = ThreadPool(self.conf.get_thread_pool())
        result_list = pool.map(self.__gather_services__, self.url_list)
        pool.close()
        pool.join()
        return result_list

    def __gather_services__(self, url):
        url_check_time = datetime.datetime.now().strftime("%y/%m/%d %H:%M")
        status_and_speed = up_and_speed_test.server_test("http", url)
        if status_and_speed['status'] is 'up':
            result = {'Result': {'app_url': self.conf.get_app_url(), 'location': self.conf.get_app_location(),
                                 'date': url_check_time, 'url': url, 'result': status_and_speed}}
            return result
        elif status_and_speed['status'] is 'down':
            result = {'Result': {'app_url': self.conf.get_app_url(), 'location': self.conf.get_app_location(), 'date': url_check_time, 'url': url,'result': status_and_speed}}
            # Send the inter upt to inter upt service and then do some things on this downed urls in that service
            interupt_logger = inter_upt_logger.InterUptLogger()
            interupt_logger.put_interupt(result["Result"])
            return result
