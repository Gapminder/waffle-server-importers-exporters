import time


def set_timestamp():
    time_now = time.gmtime()
    return str(time_now.tm_year) + '-' + str(time_now.tm_mon) + '-' + str(time_now.tm_mday) + 'T' + \
          str(time_now.tm_hour) + ':' + str(time_now.tm_min) + ':' + str(time_now.tm_sec) + "Z"
