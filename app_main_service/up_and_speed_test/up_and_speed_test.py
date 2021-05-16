__author__ = "Manouchehr Rasouli"
__date__ = "3/Aug/2017, 11/Aug/2017"

from urllib.request import urlopen
from socket import socket
import time


def tcp_test(server_info):
    cpos = server_info.find(':')
    try:
        sock = socket()
        sock.connect((server_info[:cpos], int(server_info[cpos+1:])))
        sock.close
        return True
    except Exception as e:
        return False


def http_test(server_info):
    try:
        # TODO : we can use this data after to find sub urls up or down results
        startTime = time.time()
        data = urlopen(server_info).read()
        endTime = time.time()
        speed = endTime - startTime
        return {'status' : 'up', 'speed' : str(speed)}
    except Exception as e:
        return {'status' : 'down', 'speed' : str(-1)}


def server_test(test_type, server_info):
    if test_type.lower() == 'tcp':
        return tcp_test(server_info)
    elif test_type.lower() == 'http':
        return http_test(server_info)

