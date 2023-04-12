'''
数据处理层
'''
import json
import os.path
from conf import setting

#查询用户
def select(username):
    user_data_path = os.path.join(setting.USER_DATA_PATH, f'{username}.json')
    if os.path.exists(user_data_path):
        with open(user_data_path, 'rt', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic

#保存用户数据
def save(user_dic):
    username = user_dic.get('username')
    user_data_path = os.path.join(setting.USER_DATA_PATH, f'{username}.json')
    with open(user_data_path, 'wt', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii=False)

#查询商品字典


def select_shop_list():
    shop_file_path = os.path.join(setting.SHOP_DATA_PATH,'shop.json')
    with open(shop_file_path,mode='r',encoding='utf-8') as f:
        shop_dic = json.load(f)
        return shop_dic