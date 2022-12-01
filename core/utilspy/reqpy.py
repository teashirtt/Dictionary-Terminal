import requests
import json
import utilspy.textpy as tp
from utilspy.funcpy import date
import utilspy.databasepy as db
import re
from hashlib import sha256


def init():
    tp.version()
    tp.cat()
    weather()
    print('使用 -help 查看如何使用')
    return getIp()


def trans(word):
    try:
        ret = requests.get(
            f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        data = json.loads(ret.text)
        if ret.status_code == 200:
            for part in data[0]['meanings']:
                for d in part['definitions'][:2]:
                    tp.separator()
                    print(f"{part['partOfSpeech']} : {d['definition']}")
                    try:
                        print(f"example : {d['example']}")
                    except:
                        continue
        else:
            print('sorry,没有找到这个词诶')
        tp.separator()
    except:
        print('网络连接异常 --获取翻译失败')


def weather():
    try:
        ret = requests.get(
            'https://v0.yiketianqi.com/api?unescape=1&version=v61&appid=43429654&appsecret=qSjImVc6'
        )
        res = json.loads(ret.text)
        time = date().split(' ')[1]
        print(
            f'{res["date"]},{time},{res["city"]},气温{res["tem2"]} ~ {res["tem1"]},天气{res["wea"]}')
    except:
        print('网络连接异常 --获取天气数据失败')


def weachart():
    try:
        ret = requests.get(
            'http://152.136.154.181:8020/api/wea'
        )
        wea = json.loads(ret.text)['wea']
        print(wea)
    except:
        print('网络连接异常 --获取天气接口数据失败')


def getIp():
    try:
        ret = requests.get(
            'http://myip.ipip.net'
        )
        ip = re.findall(r"[0-9]+(?:\.[0-9]+){0,3}", ret.text)[0]
        return ip
    except:
        print('网络连接异常 --获取ip地址失败')


def databaseLogin(username, password):
    hash = sha256()
    hash.update(password.encode('utf-8'))
    password = hash.hexdigest()
    data = {"username": f"{username}", "password": f"{password}"}
    try:
        ret = requests.post(
            'http://152.136.154.181:8060/login', json=data
        )
        user = json.loads(ret.text)
        db.connect(user['userid'], user['username'])
    except:
        print('账号关联失败,请保证你以注册并使用正确的账号和密码! --项目关联: http://152.136.154.181:4547/todo')
