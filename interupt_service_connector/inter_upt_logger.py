__author__ = "Manouchehr Rasouli"
__date__ = "5/Aug/2017"

from . import interuptqueue


class InterUptLogger:

    instance = None

    class __InterUptLogger:
        def __init__(self):
            self.inter_upt_queue = interuptqueue.InterUptQueue()

        def __put_inter_upt__(self, interupt):
            self.inter_upt_queue.__put_interupt__(interupt)
            return

        def __get_inter_upt__(self):
            return self.inter_upt_queue

        def __get_size__(self):
            return self.inter_upt_queue.__get_size__()

        def __pop_inter_upt__(self):
            return self.inter_upt_queue.__pop_interupt__()

    def __init__(self):
        if not InterUptLogger.instance:
            InterUptLogger.instance = InterUptLogger.__InterUptLogger()

    def put_interupt (self, inter_upt):
        InterUptLogger.instance.__put_inter_upt__(inter_upt)
        return

    def get_loged_interupt(self):
        return InterUptLogger.instance.__get_inter_upt__()

    def pop_interupt(self):
        return InterUptLogger.instance.__pop_inter_upt__()

    def check_size(self):
        return InterUptLogger.instance.__get_size__()
