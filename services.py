__author__ = "Manouchehr Rasouli"
__date__ = "8/Aug/2017"

from app_main_service import main_service
from inter_upt_service import inter_upt_service
from receive_service import fetch_urls
from send_service import register_and_sync_application
from exception_log_service import exception_service


class StartServices:

    class __StartServices:
        def __init__(self):
            # Start exception log service because of other services use this service
            exception_service.ExceptionService()

            register_and_sync_application.do_registration()
            register_and_sync_application.DoSync()
            fetch_urls.fetch_urls_from_service()

            # Start other services
            main_service.StartMainService()
            inter_upt_service.InterUptService()

    instance = None

    def __init__(self):
        if not StartServices.instance:
            StartServices.instance = StartServices.__StartServices()