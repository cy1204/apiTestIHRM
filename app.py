"""
配置文件
"""
import logging, os
from logging import handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "http://182.92.81.159"
HEADERS = {"Content-Type": "application/json"}
EMP_ID = 0


def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 设置处理器
    # 设置控制台处理器
    sh = logging.StreamHandler()
    # 设置文件处理器
    login_path = BASE_DIR + "/log/ihrm.log"
    fh = logging.handlers.TimedRotatingFileHandler(login_path, when="M", interval=1, backupCount=5)
    # 创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    fomatter = logging.Formatter(fmt=fmt)
    # 将格式化器添加给处理器
    sh.setFormatter(fomatter)
    fh.setFormatter(fomatter)
    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)
