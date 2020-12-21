import logging
from flask.logging import default_handler
import os
from logging.handlers import RotatingFileHandler
from logging import StreamHandler
from flask import has_request_context, request
# from app.models import SysLog
import requests

 
class CustomHandler(logging.Handler):
    def __init__(self,host,uri,baseParam,method="POST"):
        logging.Handler.__init__(self)
        self.url = "%s/%s"%(host,uri)
        self.baseParam = baseParam
        method = str.upper(method)
        if method not in ["GET", "POST"]:
            # raise ValueError, "method must be GET or POST"
            method="GET"
        self.method = method

    def emit(self, record):
        '''
        重写emit方法，这里主要是为了把初始化时的baseParam添加进来
        :param record:
        :return:
        '''
        self.baseParam["logdata"]  = self.format(record)
        if self.method == "GET":
            if (string.find(self.url, '?') >= 0):
                sep = '&'
            else:
                sep = '?'
            url = self.url + "%c%s" % (sep, data)
            requests.get(url,timeout=1)
        else:
            headers = {
                "Content-type":"application/x-www-form-urlencoded",
                "Content-length":str(len(data))
            }
            requests.post(self.url,data=self.baseParam,headers=headers,timeout=1)




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
    
    def init_app(app,db):
                # 移除默认的handler
        app.logger.removeHandler(default_handler)
        formatter = RequestFormatter(
            '{%(asctime)s}{%(thread)d}{%(threadName)s}{%(filename)s}{%(module)s}{%(funcName)s}{%(levelname)s}{%(message)s}'
        )
        # formatter = RequestFormatter('[%(asctime)s] %(remote_addr)s requested %(url)s\n''%(levelname)s in %(module)s: %(message)s')
        
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
 
        stream_handler = StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.INFO)
 
        # httphandler = CustomHandler(r"http://127.0.0.1","collog",{"taskid":"aaaa","casenum":123})
        # httphandler.setFormatter(formatter) #这行代码就是将日志格式化成我们想要的样子
        # logger.addHandler(httphandler)

        for logger in (
                # 这里自己还可以添加更多的日志模块，具体请参阅Flask官方文档
                app.logger,
                logging.getLogger('sqlalchemy'),
                logging.getLogger('werkzeug')
 
        ):
            # logger.addHandler(file_handler)
            # 向控制台输出日志
            logger.addHandler(stream_handler)

     