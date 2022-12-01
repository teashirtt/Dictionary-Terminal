# Dictionary-Terminal

### 使用
直接运行 `main.exe`

### 功能
- 输入 \<english word> 以查看英文释义和例句
- 使用 -\<command> 执行相关命令
- 目前支持的命令：

|                              功能                              |        命令         |
| :------------------------------------------------------------: | :-----------------: |
|                              退出                              |   `-exit` , `-q`    |
|                            查看天气                            | `-weather` , `-wea` |
|                     查看天气折线图(开发中)                     |     `-weachart`     |
|                            查看日期                            |       `-date`       |
|                             查看ip                             |        `-ip`        |
|                              清屏                              |  `-clear` , `-cl`   |
|                            查看版本                            |  `-version` , `-v`  |
|                            查看帮助                            |   `-help` , `-h`    |
| 关联[todolist](https://github.com/Zzzz0zzzZ/todolist-demo)项目 |       `-todo`       |


### TODO
- 多了去了

### 其他说明

- 数据库连接参数隐藏
```python
# /core/utilspy/databasepy.py
db = pymysql.connect(host="XXX",
                     port=XXX,
                     user="XXX",
                     password="XXX",
                     database="XXX",
                     charset='utf8')
```