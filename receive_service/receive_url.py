_author__ = "Manouchehr Rasouli, Amireza Bala Boland"
__date__ = "5/Aug/2017"

from flask_restful import Resource
from flask import request
from db_pack import db_connection_pool, use_db
from exception_log_service_connection import exception_logger
import datetime


class ReceiveUrl(Resource):

    def put(self):
        try:
            url_json = request.form['url']
            print(url_json)
            pool = db_connection_pool.Pooling()
            connection = pool.get_connection()
            url_db = use_db.use_url_db(connection)
            url_db.insert_url(url_json)
            return {"result" : "success"}
        except Exception as e:
            error = {"service_name" : "receive_service/url_receive", "date" : datetime.datetime.now().strftime("%y/%m/%d %H:%M"), "exception" : e}
            loger = exception_logger.ExceptionLogger()
            loger.put_exception(error)
