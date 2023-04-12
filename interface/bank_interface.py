# 提现接口（收取5%手续费）
from db import db_handler
from lib import common
# 根据不同的接口类型传入不同的日志对象
bank_logger = common.get_logger(log_type='bank')
#提现接口
def withdraw_interface(username, money):
    user_dic = db_handler.select(username)
    balance = float(user_dic['balance'])
    money2 = float(money) * 1.05
    if balance > money2:
        balance -= money2
        user_dic['balance'] = balance
        flow = '用户%s 提现%s 手续费%s' % (username, money, money2 - float(money))
        bank_logger.info(flow)
        user_dic['flow'].append(flow)
        db_handler.save(user_dic)
        return True, flow
    return False, '余额不足，请重新输入'
# 还款接口
def repay_interface(username,money):
    user_dic = db_handler.select(username)
    user_dic['balance'] += money
    flow =  f'用户{username}还款{money}成功'
    bank_logger.info(flow)
    user_dic['flow'].append(flow)
    db_handler.save(user_dic)
    return True,flow
# 转账接口
def transfer_interface(login_user,to_user,transfer_money):
    login_user_dic = db_handler.select(login_user)
    to_user_dic = db_handler.select(to_user)
    if not to_user_dic:
        return False,'转账用户不存在'
    if login_user_dic['balance'] >= transfer_money:
        login_user_dic['balance'] -= transfer_money
        to_user_dic['balance'] += transfer_money
        to_user_flow = f'收到{login_user} 转账{transfer_money}'
        login_user_flow = f'给{to_user}转账{transfer_money}成功'
        login_user_dic['flow'].append(login_user_flow)
        to_user_dic['flow'].append(to_user_flow)

        db_handler.save(login_user_dic)
        db_handler.save(to_user_dic)
        return True,login_user_flow
    return False,'当前用户金额不足'
# 查询流水接口
def check_flow_interface(login_user):
    user_dic = db_handler.select(login_user)
    return user_dic['flow']

# 支付接口
def pay_interface(login_user, cost):
    user_dic = db_handler.select(login_user)
    if user_dic['balance'] >= cost:
        user_dic['balance'] -= cost

        flow = f'用户购买商品支付{cost}'
        user_dic['flow'].append(flow)
        db_handler.save(user_dic)
        return True,flow
    return False,'用户金额不足，无法支付'

