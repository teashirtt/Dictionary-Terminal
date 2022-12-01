import utilspy.reqpy as req
import mapper as mp

if __name__ == '__main__':
    host = req.init()
    while True:
        info = input(f'{host}> ').lstrip()
        if info == '':
            continue
        elif info[0] == '-':
            mp.mapper(info[1:])
        elif info[0].isalpha() == True:
            req.trans(info)
        else:
            print('wrong input! try -help to see how to use')
