__author_ = "Manouchehr Rasouli"
__date__ = "2/Aug/2017, 5/Aug/2017"


from collections import deque


class ExceptionQueue:
    def __init__(self):
        self.queue = deque()

    def __put_exception__(self, exception):
        self.queue.append(exception)
        return

    def __pop_exception__(self):
        return self.queue.popleft()

    def __get_size__(self):
        return len(self.queue)
