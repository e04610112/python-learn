# -*- coding: UTF-8 -*-
# 提示输入用户名和密码

# 验证用户名和密码
#     如果错误，则输出用户名或密码错误
#     如果成功，则输出 欢迎，XXX!




import getpass


name = raw_input('请输入用户名：')

pwd = getpass.getpass('请输入密码：')

if name == "alex" and pwd == "cmd":
    print "欢迎，alex！"
else:
    print "用户名和密码错误"