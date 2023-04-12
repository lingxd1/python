'''
存放公共方法
'''
import hashlib
from conf import setting
import logging.config


# 登录认证装饰器
def login_auth(func):
    def inner(*args, **kwargs):
        from core import src
        if src.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print('未登录，请重新登录')
            src.login()

    return inner


# 密码加盐
def get_pwd_md5(password):
    md5_obj = hashlib.md5()
    md5_obj.update(password.encode('utf-8'))
    salt = '哈哈哈哈哈哈嘻嘻嘻'
    md5_obj.update(salt.encode('utf-8'))
    return md5_obj.hexdigest()

# 日志
def get_logger(log_type):
    logging.config.dictConfig(setting.LOGGING_DIC)

    logger = logging.getLogger(log_type)
    return logger
