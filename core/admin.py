import sys
from core import src
from interface import admin_interface
# 0、退出功能
def quit():
    print('感谢使用')


# 添加账户功能
def add_user():
    src.register()

# 修改用户额度功能
def edit_balance():
    while True:
        username = input('请输入需要修改的用户').strip()
        balance = input('请输入需要修改的额度').strip()
        if not balance.isdigit():
            print('请输入正确的金额')
            continue
        balance = float(balance)
        flag,msg = admin_interface.edit_balance_interface(username,balance)
        if flag:
            print(msg)
            break
        else:
            print(msg)

#冻结账户功能
def lock_user():
    while True:
        username = input('请输入需要冻结用户').strip()
        if username == 'q':
            break
        flag,msg = admin_interface.lock_user_interface(username)
        if flag:
            print(msg)
            break
        else:
            print(msg)

func_dic = {
    '0':[quit,'退出'],
    '1':[add_user,'添加账户功能'],
    '2':[edit_balance,'修改用户额度功能'],
    '3':[lock_user,'冻结账户功能']
}

def admin_run():
    while True:
        print('管理员功能'.center(20, '='))
        for k in func_dic:
            print(k, func_dic.get(k)[1])
        print('end'.center(20, '='))

        choice = input('请输出功能编号： ').strip()
        if choice == '0':
            print('感谢使用')
            break

        if choice in func_dic:
            func_dic.get(choice)[0]()
        else:
            print('请输入正确编号')

if __name__ == '__main__':
    admin_run()