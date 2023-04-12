'''
用户视图层
'''
import sys
from interface import user_interface
from interface import bank_interface
from interface import shop_interface
from lib import common
from  core import admin as admin1
from  db import  db_handler

# 记录用户状态，是否已登录
login_user = None


# 0、退出功能
def quit():
    print('感谢使用')
    sys.exit(0)


# 1、注册功能
def register():
    while True:
        username = input('请输入用户名: ').strip()
        pwd = input('请输入密码: ').strip()
        re_pwd = input('请确认密码: ').strip()

        if pwd == re_pwd:

            res, msg = user_interface.register_interface(username, pwd)
            if res:
                print(msg)
                break
            else:
                print(msg)

        else:
            print('两次密码输入不一致，请重新输入！')
    pass


# 2、登录功能
def login():
    while True:
        username = input('请输入用户名： ').strip()
        pwd = input('请输入密码： ').strip()

        res, msg = user_interface.login_interface(username, pwd)
        if res:
            print(msg)
            global login_user
            login_user = username
            break
        else:
            print(msg)


# 3、查看余额
@common.login_auth
def check_balance():
    res = user_interface.select_bal_interface(login_user)
    print('用户%s，余额%s' % (login_user, res))


# 4、提现功能
@common.login_auth
def withdraw():
    while True:
        input_money = input('请输入提现金额').strip()
        if not input_money.isdigit():
            print('请重新输入')
            continue
        res, msg = bank_interface.withdraw_interface(login_user, input_money)
        if res:
            print(msg)
            break
        else:
            print(msg)


# 5、还款功能
@common.login_auth
def repay():
    while True:
        input_money = input('请输入还款金额').strip()
        if not input_money.isdigit():
            print('请输入正确金额')
            continue
        input_money = float(input_money)
        if input_money > 0:
            flag,msg = bank_interface.repay_interface(login_user,input_money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('输入的金额不能小于0')





# 6、转账功能
@common.login_auth
def transfer():
    while True:
        to_user = input('请输入转账用户').strip()
        transfer_money = input('请输入转账金额').strip()
        if not transfer_money.isdigit():
            print('请输入正确金额')
            continue
        transfer_money = float(transfer_money)
        if transfer_money > 0:
            flag,msg = bank_interface.transfer_interface(login_user,to_user,transfer_money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('输入的金额不能小于0')



# 7、查看流水
@common.login_auth
def check_flow():
    flow_list = bank_interface.check_flow_interface(login_user)
    if flow_list:
        for i in flow_list:
            print(i)
    else:
        print('当前用户无流水')


# 8、购物功能
@common.login_auth
def shopping():
    shop_dic = db_handler.select_shop_list()
    shop_car = {} #{商品名称：[单价,数量]}

    while True:
        for k in shop_dic:
            print(f'商品编号【{k}】,商品名称【{shop_dic[k][0]}】,商品价格【{shop_dic[k][1]}】')
        choice = input('请选择商品编号（是否结账输入y or n）: ').strip()
        if choice == 'y':
            if not shop_car:
                print('购物车是空的，无需结账')
                continue
            flag,msg = shop_interface.shopping_interface(login_user,shop_car)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        elif choice == 'n':
            if not shop_car:
                print('购物车是空的，不能添加,请重新输入')
                continue
            flag, msg = shop_interface.add_shop_car_interface(login_user,shop_car)

            if flag:
                print(msg)
                break
        if not choice.isdigit():
            print('请输入正确的编号')
            continue

        if choice not in shop_dic:
            print('请输入范围内的标号')
            continue
        #获取 商品名称 和 单价
        shop_name , shop_price = shop_dic[choice]
        if shop_name in shop_car:
            shop_car[shop_name][1] += 1
        else:
            shop_car[shop_name]=[shop_price,1]
        print('当前购物车' ,shop_car)






# 9、查看购物车
@common.login_auth
def check_shop_car():
    shop_car = shop_interface.select_shop_car(login_user)
    print(shop_car)



# 10、管理员功能
@common.login_auth
def admin():
#    from  core import admin
    admin1.admin_run()


# 创建函数字典
func_dic = {
    '0': [exit, '退出'],
    '1': [register, '注册功能'],
    '2': [login, '登录功能'],
    '3': [check_balance, '查看余额'],
    '4': [withdraw, '提现功能'],
    '5': [repay, '还款功能'],
    '6': [transfer, '转账功能'],
    '7': [check_flow, '查看流水'],
    '8': [shopping, '购物功能'],
    '9': [check_shop_car, '查看购物车'],
    '10': [admin, '管理员功能']
}


def run():
    while True:

        print('ATM + 购物车'.center(20, '='))
        for k in func_dic:
            print(k, func_dic.get(k)[1])
        print('end'.center(20, '='))

        choice = input('请输出功能编号： ').strip()
        if choice in func_dic:
            func_dic.get(choice)[0]()
        else:
            print('请输入正确编号')


run()
