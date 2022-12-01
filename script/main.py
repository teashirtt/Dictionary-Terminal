import requests
import json

ret = requests.get(
    'https://v0.yiketianqi.com/api?unescape=1&version=v61&appid=43429654&appsecret=qSjImVc6'
)

res = json.loads(ret.text)

data = f'{res["date"]},{res["city"]},更新时间{res["update_time"]},气温{res["tem2"]}~{res["tem1"]},天气{res["wea"]}'

print(data)
