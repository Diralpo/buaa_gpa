## 几个合理的示例 ##


- 输入账号和密码(并将其设置为默认账户) 
> python main.py save username password

- 输入账号和密码及保存文件名，保存在`/save/user`目录下
> python main.py save username password savename.p

- 默认读入路径
> python main.py load


- 输入读入路径
> python main.py load username.p



- 帮助


> python main.py -h


> python main.py help



## 说明

1. 查询成绩结果保存在`/save/gpa`路径下
2. 课表保存路径文`/save`
3. 账号、密码、路径等都不要出现空白符
4. 目前GPA的算法有问题，与信息北航上的结果并不一致

