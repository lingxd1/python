from db import db_handler
#修改额度接口
def edit_balance_interface(username,balance):
    user_dic = db_handler.select(username)
    if user_dic:
        user_dic['balance']=balance
        db_handler.save(user_dic)
        return True,f'用户{username},额度修改成功'
    return False,f'用户{username}不存在'


#冻结用户接口
def lock_user_interface(username):
    user_dic = db_handler.select(username)
    if user_dic:
        if user_dic['locked']:
            return False,f'用户{username}已经是锁定状态，无需操作'
        user_dic['locked']=True
        db_handler.save(user_dic)
        return True,f'用户{username}冻结成功'
    return False,'用户不存在'

