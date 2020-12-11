# import os
# import logging
# from logging.handlers import TimedRotatingFileHandler


# class AppLog:
#     @staticmethod
#     def init_log(path):
#         if not os.path.exists(path):
#             os.makedirs(path)
#         formatter =  "时间：%(asctime)s ;日志的文件名: %(filename)s ;行数: %(lineno)d %(funcName)s ;日志等级: %(levelname)s ;日志信息:%(message)s "
#         logging.basicConfig(
#             level=logging.DEBUG,
#             format=formatter,
#             datefmt='%a, %d %b %Y %H:%M:%S',
#         )
#         handler = TimedRotatingFileHandler(path + '/flask.log', when="d",
#                                            backupCount=7)
#         handler.setFormatter(logging.Formatter(formatter))
#         handler.setLevel(logging.DEBUG)
#         logging.getLogger('').addHandler(handler)
#         logging.getLogger('sqlalchemy.engine').addHandler(handler)
# # -*- coding: utf-8 -*-
 
import logging
from flask.logging import default_handler
import os
from logging.handlers import RotatingFileHandler
from logging import StreamHandler

from flask import has_request_context, request

class RequestFormatter(logging.Formatter):
    
    def format(self, record):
 
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)




BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_PATH = os.path.join(BASE_DIR, '../logs')
LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
LOG_PATH_ALL = os.path.join(LOG_PATH, 'all.log')
# 日志文件最大 100MB
LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
# 轮转数量是 10 个
LOG_FILE_BACKUP_COUNT = 10

class Logger(object):
    
    def init_app(app):
                # 移除默认的handler
        app.logger.removeHandler(default_handler)
        # formatter = RequestFormatter(
        #     '[%(asctime)s] [%(thread)d:%(threadName)s] [%(filename)s:%(module)s:%(funcName)s]  [%(levelname)s: %(message)s]'
        # )
        formatter = RequestFormatter('[%(asctime)s] %(remote_addr)s requested %(url)s\n''%(levelname)s in %(module)s: %(message)s')
        # 将日志输出到文件
        # 1 MB = 1024 * 1024 bytes
        # 此处设置日志文件大小为500MB，超过500MB自动开始写入新的日志文件，历史文件归档
        file_handler = RotatingFileHandler(
            filename=LOG_PATH_ALL,
            mode='a',
            maxBytes=LOG_FILE_MAX_BYTES,
            backupCount=LOG_FILE_BACKUP_COUNT,
            encoding='utf-8'
        )
 
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.INFO)
 
        # stream_handler = StreamHandler()
        # stream_handler.setFormatter(formatter)
        # stream_handler.setLevel(logging.ERROR)
 

        # formatter1 = RequestFormatter('[%(asctime)s] %(remote_addr)s requested %(url)s\n''%(levelname)s in %(module)s: %(message)s')
        # file_handler.setFormatter(formatter1)
        # stream_handler.setFormatter(formatter1)


        for logger in (
                # 这里自己还可以添加更多的日志模块，具体请参阅Flask官方文档
                app.logger,
                logging.getLogger('sqlalchemy'),
                logging.getLogger('werkzeug')
 
        ):
            logger.addHandler(file_handler)
            # logger.addHandler(stream_handler)

    def create_logger():
        # """配置flask日志"""
        # 创建flask.app日志器
        flask_logger = logging.getLogger('flask.app')
        # 设置全局级别
        flask_logger.setLevel('DEBUG')

        # 创建控制台处理器
        console_handler = logging.StreamHandler()

        # 给处理器设置输出格式
        console_formatter = logging.Formatter(fmt='%(name)s %(levelname)s %(pathname)s %(lineno)d %(message)s')
        console_handler.setFormatter(console_formatter)

        # 日志器添加处理器
        flask_logger.addHandler(console_handler)

        # 创建文件处理器
        file_handler = RotatingFileHandler(filename='flask.log', maxBytes=100 * 1024 * 1024, backupCount=10)  # 转存文件处理器  当达到限定的文件大小时, 可以将日志转存到其他文件中

        # 给处理器设置输出格式
        file_formatter = RequestFormatter(fmt='[%(asctime)s] %(remote_addr)s requested %(url)s %(name)s %(levelname)s %(pathname)s %(lineno)d %(message)s')
        file_handler.setFormatter(file_formatter)
        # 单独设置文件处理器的日志级别
        file_handler.setLevel('WARN')

        # 日志器添加处理器
        flask_logger.addHandler(file_handler)