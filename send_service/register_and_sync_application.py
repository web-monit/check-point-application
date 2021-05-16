__author__ = "Manouchehr Rasouli"
__date__ = "3/Aug/2017, 10/Aug/2017"

import datetime
import requests
import json
import threading
import time
from config_pack import configuration_manager
from exception_log_service_connection import exception_logger
from db_pack import db_connection_pool, use_db


# This section do registration for app in main service


def do_registration():
    # Fetch data from config package
    config = configuration_manager.ConfigPack()
    app_url = config.get_app_url()
    app_location = config.get_app_location()
    service_url = config.get_service_url()
    service_register_app_url = config.get_service_register_app_url()
    # Send request to main service to register ourselves on the it
    print("start to sync with service")
    while True:
        try :
            data = [('app', '{"appurl":"'+ app_url +'", "applocation":"'+ app_location +'"}')]
            requests.put( service_url + service_register_app_url, data=data)
            break
        except Exception as e:
            error = {"service_name" : "send_service/do_registration", "date" : datetime.datetime.now().strftime("%y/%m/%d %H:%M"), "exception" : str(e)}
            loger = exception_logger.ExceptionLogger()
            loger.put_exception(error)
        time.sleep(10)
    return


class DoSync:

    def __init__(self):
        self.conf = None
        self.pool = None
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        # Store last date that app do sync with main service and we send result for after this time
        last_date_file_location = "send_service/last_sync.txt"
        f = open(last_date_file_location, "r")
        last_date = f.read()
        temporary_date = last_date
        while True:
            self.conf = configuration_manager.ConfigPack()
            try:
                service_url = self.conf.get_service_url()
                service_sync_url = self.conf.get_service_sync_url()
                self.pool = db_connection_pool.Pooling()
                connection = self.pool.get_connection()
                result_db = use_db.use_result_db(connection)
                result_list = result_db.get_result_as_list_after(last_date)
                if len(result_list) > 0:
                    status_dic = {}
                    for x in range(0, len(result_list)):
                        if result_list[x]["date"] >= last_date:
                            last_date = result_list[x]["date"]
                        status_dic[x] = result_list[x]
                    result_json = json.dumps(status_dic)
                    data = [('result', '{"res":'+ result_json +'}')]
                    requests.put(service_url + service_sync_url, data=data)
                    f = open(last_date_file_location, "w")
                    f.write(last_date)
                    print("sync done !")
            except Exception as e:
                error = {"service_name" : "send_service/send_result", "date" : time.strftime("%d/%m/%Y %I:%M"), "exception" : str(e)}
                logger = exception_logger.ExceptionLogger()
                logger.put_exception(error)
                # If there's any problem in syncing then we have the last date and we can start over there
                f = open(last_date_file_location, "w")
                f.write(temporary_date)
            time.sleep(self.conf.get_sync_time())
