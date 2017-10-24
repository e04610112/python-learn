#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 切换到root 权限   命令pip install Pillow 安装Pillow
from PIL import Image
im = Image.open('/Users/linyuanjing/11.png')
print(im.format, im.size, im.mode)

im.thumbnail((200, 100))
im.save('/Users/linyuanjing/121.jpg', 'JPEG')