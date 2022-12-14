import pandas as pd


def wea_data():
    try:
        df = pd.read_csv(
            r'/home/ubuntu/coding/weather-script/data.txt', names=['date', 'city', 'update_time', 'tem', 'wea'], encoding='UTF-8')
        res = []
        for i in range(7):
            tem = df['tem'][i*3][2:].split('~')
            res.append([df['date'][i*3], int(tem[0]), int(tem[1])])
        dict = {"wea": res}
        return dict
    except:
        return []