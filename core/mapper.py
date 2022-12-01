import utilspy.reqpy as req
import utilspy.funcpy as func
import utilspy.textpy as tp


def mapper(order):
    if order == 'exit' or order == 'q':
        func.exit()
    elif order == 'weather' or order == 'wea':
        req.weather()
    elif order == 'weachart':
        req.weachart()
    elif order == 'date':
        print(func.date())
    elif order == 'ip':
        print(req.getIp())
    elif order == 'clear' or order == 'cl':
        func.clear()
    elif order == 'version' or order == 'v':
        tp.version()
    elif order == 'help' or order == 'h':
        tp.instructions()
    elif order == 'todo':
        tp.todoinfo()
        username = input('username: ')
        password = input('password: ')
        req.databaseLogin(username, password)
    else:
        print('try -help to see how to use')
