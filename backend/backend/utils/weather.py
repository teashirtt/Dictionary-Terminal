import pandas as pd


def wea_data():
    try:
        df = pd.read_csv(
            r'/home/ubuntu/coding/weather-script/data.txt', names=['date', 'city', 'update_time', 'tem', 'wea'], encoding='UTF-8')
        res = []
        for i in range(1, df.shape[0], 3):
            tem = df['tem'][i][2:].split('~')
            res.append([df['date'][i], int(tem[0]), int(tem[1])])
        dict = {"wea": res[-7:]}
        return dict
    except:
        return []
