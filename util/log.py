import logging
import time

logging.basicConfig(filename='log/ws_ie_info.log', level=logging.DEBUG)


def set_info(msg):
    logging.info(str(time.gmtime()) + '  INFO:' + msg)
