from  interface import bank_interface
from  db import db_handler

#购物功能,准备结算
def shopping_interface(login_user,shop_car):
    cost = 0
    for i in shop_car.values():
        price , num = i
        cost += (price * num)

    flag,msg = bank_interface.pay_interface(login_user, cost)
    if flag:
        return True,msg
    else:
        return False,msg


#添加购物车功能
def add_shop_car_interface(login_user,shop_car):
    user_dic = db_handler.select(login_user)
    shop_car_file = user_dic['shop_car']
    for shop_name , price_num in shop_car.items():
        num = price_num[1]
        if shop_name in shop_car_file:
            user_dic['shop_car'][shop_name][1] += num
        else:
            user_dic['shop_car'][shop_name]=price_num
    db_handler.save(user_dic)
    return True,'添加购物车成功'
#查看购物车
def select_shop_car(login_user):
    user_dic = db_handler.select(login_user)
    return user_dic.get('shop_car')







