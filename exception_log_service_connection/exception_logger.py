__author__ = "Manouchehr Rasouli"
__date__ = "2/Aug/2017"

from . import exception_queue


class ExceptionLogger:

    instance = None

    class __ExceptionLogger:
        def __init__(self):
            self.exception_queue= exception_queue.ExceptionQueue()

        def __put_exception__(self, exception):
            self.exception_queue.__put_exception__(exception)
            return

        def __get_exceptions__(self):
            return self.exception_queue

        def __get_size__(self):
            return self.exception_queue.__get_size__()

        def __pop_exception__(self):
            return self.exception_queue.__pop_exception__()

    def __init__(self):
        if not ExceptionLogger.instance:
            ExceptionLogger.instance = ExceptionLogger.__ExceptionLogger()

    def put_exception (self, exception):
        ExceptionLogger.instance.__put_exception__(exception)
        return

    def get_loged_exceptions(self):
        return ExceptionLogger.instance.__get_exceptions__()

    def pop_exception(self):
        return ExceptionLogger.instance.__pop_exception__()

    def check_size(self):
        return ExceptionLogger.instance.__get_size__()
