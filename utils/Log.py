import os
import logging
from logging.handlers import TimedRotatingFileHandler


class AppLog:
    @staticmethod
    def init_log(path):
        if not os.path.exists(path):
            os.makedirs(path)
        formatter =  "时间：%(asctime)s ;日志的文件名: %(filename)s ;行数: %(lineno)d %(funcName)s ;日志等级: %(levelname)s ;日志信息:%(message)s "
        logging.basicConfig(
            level=logging.DEBUG,
            format=formatter,
            datefmt='%a, %d %b %Y %H:%M:%S',
        )
        handler = TimedRotatingFileHandler(path + '/flask.log', when="d",
                                           backupCount=7)
        handler.setFormatter(logging.Formatter(formatter))
        handler.setLevel(logging.DEBUG)
        logging.getLogger('').addHandler(handler)
        logging.getLogger('sqlalchemy.engine').addHandler(handler)
