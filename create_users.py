# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 3:58 PM
# @Author  : Jihu Sun
# @FileName: create_users.py
# @Software: PyCharm


def create_user(central_conn, users):
    # central添加user API
    apiPath = "/platform/rbac/v1/users"
    apiMethod = "POST"

    # 将user写到central
    for user in users:
        username = user[0]
        firstname = user[1]
        lastname = user[2]
        name = {
            'firstname': firstname,
            'lastname': lastname
        }
        phone = '+86-{}'.format(str(user[3]).split('.')[0])

        nms_role = 'readonly'
        account_setting_role = 'readonly'

        apiData = {
            "username": username,
            "password": "123",  # 任意字符，无用
            "description": "central api creat user",
            "name": name,
            "phone": phone,
            "address": {
                "street": "street",
                "city": "city",
                "state": "state",
                "country": "country",
                "zipcode": "zipcode"
            },
            "applications": [
                {
                    "name": "nms",
                    "info": [
                        {
                            "role": nms_role,
                            "scope": {
                                "groups": [
                                    "allgroups"
                                ]
                            }
                        }
                    ]
                },
                {
                    "name": "account_setting",
                    "info": [
                        {
                            "role": account_setting_role
                        }
                    ]
                }
            ]
        }
        base_resp = central_conn.command(apiMethod=apiMethod,
                                         apiPath=apiPath,
                                         apiData=apiData)
        if base_resp['code'] == 200:
            print("Account: {} post successfully!".format(username))
        else:
            print("Account: {} post failed! Code:{}, Reason:{}".format(username, base_resp['code'], base_resp['msg']))
