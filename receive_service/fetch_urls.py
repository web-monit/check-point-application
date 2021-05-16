__author__ = "Manouchehr Rasouli"
__date__ = "3/Aug/2017"

from config_pack import configuration_manager
from exception_log_service_connection import exception_logger
import datetime
import requests
from db_pack import db_connection_pool, use_db


# This method fetch all urls that there's in main service


def fetch_urls_from_service():
    config = configuration_manager.ConfigPack()
    service_url = config.get_service_url()
    service_get_urls = config.get_service_urls()
    pool = db_connection_pool.Pooling()
    connection = pool.get_connection()
    db = use_db.use_url_db(connection)
    try :
        url_json = requests.get(service_url + service_get_urls)
        db.insert_url(url_json.json())
    except Exception as e:
        error = {"service_name" : "receiver/fetch_urls", "date" : datetime.datetime.now().strftime("%y/%m/%d %H:%M"), "exception" : e}
        loger = exception_logger.ExceptionLogger()
        loger.put_exception(error)
    return None
