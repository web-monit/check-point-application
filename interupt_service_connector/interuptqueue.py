__author__ = "Manouchehr Rasouli"
__date__ = "5/Aug/2017"


from queue import Queue


class InterUptQueue:
    def __init__(self):
        self.queue = Queue()

    def __put_interupt__(self, exception):
        self.queue.put(exception)
        return

    def __pop_interupt__(self):
        return self.queue.get()

    def __get_size__(self):
        return self.queue.qsize()
