__author__ = "Manouchehr Rasouli"
__date__ = "5/Aug/2017, 8/Aug/2017"

import requests
import json
import threading
import time
import datetime
from config_pack import configuration_manager
from interupt_service_connector import inter_upt_logger
from exception_log_service_connection import exception_logger


class InterUptService:
    def __init__(self):
        self.conf = None
        self.logger = inter_upt_logger.InterUptLogger()
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            self.conf = configuration_manager.ConfigPack()
            try:
                if int(self.logger.check_size()) > 0:
                    service_url = self.conf.get_service_url()
                    service_inter_upt_url = self.conf.get_service_interupt_url()
                    inter_upt = self.logger.pop_interupt()
                    result_json = json.dumps(inter_upt)
                    data = [('interupt', '{"interupt":'+ result_json +'}')]
                    requests.put(service_url + service_inter_upt_url, data=data)
            except Exception as e:
                error = {"service_name" : "inter_upt_service/inter_upt_service", "date" : datetime.datetime.now().strftime("%y/%m/%d %H:%M"), "exception" : str(e)}
                logger = exception_logger.ExceptionLogger()
                logger.put_exception(error)
            time.sleep(self.conf.get_interupt_service_sleep_time())
