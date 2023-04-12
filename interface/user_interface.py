'''
逻辑接口层
'''
# 注册接口
from db import db_handler
from lib import common
# 根据不同的接口类型传入不同的日志对象
user_logger = common.get_logger(log_type='user')

def register_interface(username, password, balance=15000):
    user_dic = db_handler.select(username)
    if user_dic:
        msg = '用户名已存在'
        user_logger.warn(msg)
        return False, msg
    password = common.get_pwd_md5(password)

    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        # 用于记录用户流水的q列表
        'flow': [],
        # 用于记录用户购物车
        'shop_car': {},
        # locked：用于记录用户是否被冻结
        # False: 未冻结   True: 已被冻结
        'locked': False
    }

    db_handler.save(user_dic)
    res = f'{username} 注册成功'
    user_logger.info(res)
    return True, res


# 登录接口
def login_interface(username, password):

    password = common.get_pwd_md5(password)
    user_dic = db_handler.select(username)
    if user_dic:
        if user_dic['locked']:
            msg = '当前用户已被锁定'
            user_logger.error(msg)


            return False,msg
        if password == user_dic.get('password'):
            msg = f'{username}登录成功'
            user_logger.info(msg)
            return True, msg
        else:
            msg = '密码错误'
            user_logger.error(msg)
            return False, msg
    msg = '用户名不存在'
    user_logger.error(msg)
    return False, msg


# 查询用户余额接口
def select_bal_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('balance')
