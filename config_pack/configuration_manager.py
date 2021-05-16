__author__ = "Manouchehr Rasouli"
__date__ = "1/Aug/2017, 10/Aug/2017"

from bs4 import BeautifulSoup
from exception_log_service_connection import exception_logger
import datetime


class ConfigPack:
    def __init__(self):
        #init file for this class
        try:
            self.file_url = "config_pack/config.xml"
            with open(self.file_url) as f:
                content = f.read()
            self.beautifull_soup = BeautifulSoup(content, "lxml")
        except Exception as e:
            error = {"service_name" : "config pack", "date" : datetime.datetime.now().strftime("%y/%m/%d %H:%M"), "exception" : str(e)}
            logger = exception_logger.ExceptionLogger()
            logger.put_exception(error)

    def get_conf_pack_id(self):
        return int(self.beautifull_soup.find("conf_pack_id").contents[0])

    def get_config_pack_url(self):
        return self.file_url

    def get_app_url(self):
        try:
            return self.beautifull_soup.find("appurl").contents[0]
        except Exception as e:
            loger = exception_logger.ExceptionLogger()
            loger.put_exception(e)

    def get_service_url(self):
        return self.beautifull_soup.find("serviceurl").contents[0]

    def get_sync_time(self):
        return int(self.beautifull_soup.find("synctime").contents[0])

    def get_update_time(self):
        return int(self.beautifull_soup.find("updatetime").contents[0])

    def get_thread_pool(self):
        return int(self.beautifull_soup.find("threadpool").contents[0])

    def get_db_max_pool(self):
        return int(self.beautifull_soup.find("db_max_pool").contents[0])

    def get_db_wait_queue_multiple(self):
        return int(self.beautifull_soup.find("db_wait_queue_multiple").contents[0])

    def get_db_wait_queue_timeout_ms(self):
        return int(self.beautifull_soup.find("db_wait_queue_timeout_ms").contents[0])

    def get_db_host(self):
        return self.beautifull_soup.find("dbhost").contents[0]

    def get_db_host_port(self):
        return int(self.beautifull_soup.find("dbport").contents[0])

    def get_app_host(self):
        return self.beautifull_soup.find("apphost").contents[0]

    def get_app_port(self):
        return int(self.beautifull_soup.find("appport").contents[0])

    def get_service_host(self):
        return self.beautifull_soup.find("servicehost").contents[0]

    def get_service_port(self):
        return int(self.beautifull_soup.find("serviceport").contents[0])

    def get_service_sync_url(self):
        return self.beautifull_soup.find("syncurl").contents[0]

    def get_service_register_app_url(self):
        return self.beautifull_soup.find("registeappurl").contents[0]

    def get_service_interupt_url(self):
        return self.beautifull_soup.find("interupturl").contents[0]

    def get_interupt_service_sleep_time(self):
        return int(self.beautifull_soup.find("checktime").contents[0])

    def get_app_url_register_url(self):
        return self.beautifull_soup.find("appurlregister").contents[0]

    def get_app_url_remove_url(self):
        return self.beautifull_soup.find("appurlremove").contents[0]

    def get_app_version(self):
        return self.beautifull_soup.find("version").contents[0]

    def get_app_location(self):
        return self.beautifull_soup.find("location").contents[0]

    def get_service_urls(self):
        return self.beautifull_soup.find("servicegeturls").contents[0]

    def get_exception_service_check_time(self):
        return int(self.beautifull_soup.find("exceptionchecktime").contents[0])
