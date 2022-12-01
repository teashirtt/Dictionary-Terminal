def separator():
    print('------------------------------------------------------------')


def cat():
    print('　　　　　　 ＿＿\n　　　　　／＞　　フ\n　　　　　| 　_　 _|\n　 　　　／ ミ＿ωノ\n　　 　 /　　　 　 |\n\n　 　 │　　|　|　|\n　／￣|　　 |　|　|\n　| (￣ヽ＿_ヽ_)__)\n　＼二つ\n')


def instructions():
    separator()
    version()
    print('\n输入 <english word> 以查看英文释义和例句\n使用 -<command> 执行相关命令\n目前支持的命令有: -exit(-q) 退出  -weather(-wea) 查看天气  -weachart 查看天气变化图  -date 查看日期\n-ip 查看ip-clear(-cl) 清屏  -version(-v) 查看版本  -help(-h) 查看帮助  -todo 关联todolist项目')
    separator()


def version():
    print('@teashirt-terminal 0.8.7')


def todoinfo():
    print('欢迎使用todo模块!本模块所关联的项目地址为 http://152.136.154.181:4547/todo')
