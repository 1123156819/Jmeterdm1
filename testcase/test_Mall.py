import json

import pytest

from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil
from utils.RequestsUtil import request_get, requests_post
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml
from common.Base import init_db
"""
登录成功	http://211.103.136.242:8064/authorizations/
		POST	json
		{"username":"python","password":"12345678"}

"""
# 登录
# 1导入包
import requests

# 2 定义登录方法
def test_login():
    # 3 定义测试数据
    conf_y = ConfigYaml()
    url_path = conf_y.get_conf_url()
    url = url_path+"/authorizations/"

    # url = "http://211.103.136.242:8064/authorizations/"
    data = {"username": "python", "password": "12345678"}
    # 4 发送Post请求
    # r = requests_post(url, json=data)
    # r = requests.post(url, json=data)
    request = Request()
    r = request.post(url,json=data)
    # 5 输出结果
    # print(r.json())
    print(r)
    # 验证
    # 返回状态码
    code = r["code"]
    # assert code == 200
    AssertUtil().assert_code(code,200)
    #返回结果内容
    # body = json.dumps(r["body"])
    body = r["body"]
    # assert '"user_id": 1, "username": "python"' in body
    AssertUtil().assert_in_body(body,'"username": "python", "user_id": 1')


    #1 初始化数据库对象
    conn = init_db("db_1")
    #2 查询结果
    res_db = conn.fetchone("select id,username from tb_users where username = 'python'")
    print("数据库查询结果：",res_db)
    #3 验证
    user_id = body["user_id"]
    assert user_id == res_db["id"]

    #2 查询数据信息
    #3 验证

"""
个人信息	个人信息	http://211.103.136.242:8064//user/		登录 get

 headers: {
           'Authorization': 'JWT ' + this.token
 },
"""


def test_info():
    # 1 参数
    url = "http://211.103.136.242:8064/user/"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE2MjAyNDQ5MTAsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.1m0RdLbDDyq0-QVqswektQWSm3SJv9wFFJRAb3GP50o"
    headers = {
        'Authorization': 'JWT ' + token
    }
    # 2 get请求
    # r = requests.get(url, headers=headers)
    # r = request_get(url,headers = headers)

    request = Request()
    r = request.get(url, headers=headers)
    # 3 输出结果
    # print(r.json())
    print(r)


"""
商品列表数据正确	http://211.103.136.242:8064/categories/115/skus/		
get	json	" 
{
 ""page"":""1"",
 ""page_size"": ""10"",
 ""ordering"": ""create_time""
 }"

"""


def goods_list():
    pass
    # 1 参数
    url = "http://211.103.136.242:8064/categories/115/skus/"
    data = {
        "page": "1",
        "page_size": "10",
        "ordering": "create_time"
    }
    # 2 请求
    r = requests.get(url, json=data)
    # 3 结果
    print(r.json())


"""
添加购物车成功	http://211.103.136.242:8064/cart/	
登录 post json	
{"sku_id": "3","count": "1", "selected": "true"}	sku_id': 3, 'count': 1

"""


def cart():
    url = "http://211.103.136.242:8064/cart/"
    data = {"sku_id": "3", "count": "1", "selected": "true"}
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE2MjAyNDQ5MTAsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.1m0RdLbDDyq0-QVqswektQWSm3SJv9wFFJRAb3GP50o"
    headers = {
        'Authorization': 'JWT ' + token
    }

    # r = requests.post(url, json=data, headers=headers)
    r = requests_post(url, json=data, headers=headers)
    # print(r.json())
    print(r)


"""
保存订单	http://211.103.136.242:8064/orders/	
登录 post	json	
{ "address":"1","pay_method":"1" }	

"""


def order():
    url = "http://211.103.136.242:8064/orders/"
    data = {"address": "1", "pay_method": "1"}
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE2MjAyNDQ5MTAsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.1m0RdLbDDyq0-QVqswektQWSm3SJv9wFFJRAb3GP50o"
    headers = {
        'Authorization': 'JWT ' + token
    }
    r = requests.post(url, json=data, headers=headers)
    print(r.json())


if __name__ == '__main__':
    # login()
    # info()
    # goods_list()
    # cart()
    # order()


    #1 根据默认运行原则 调整py文件名，函数命名
    #2 pytest.main()运行 或者命令行直接pytest运行
    pytest.main(["-s"])








