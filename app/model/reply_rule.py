#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/1/23 下午7:13
# @Author   : Vampire
# @Site     :  
# @File     : reply_rule.py
# @Software : PyCharm

def reply(key):
    try:
        reply_list = {
            "我要像梦一样自由": "要开启新世界请发送数字:\n1 : iphone手机登录 \n2 : android手机登录 \n3: mac登录 \n4: windows登录 \n5 : 更多节点",
            "1": "iphone登录步骤,首先打卡App Store 退出国区登录的apple id,登录其他地址apple id,搜索app Potatso Lite 下载 \n 下载完成后打开 Potatso Lite"
                 "点击 代理 > , 点击二维码 -> ,点击 开始按钮,即可开始像梦一样自由\n 更多帮助 --> 请发送数字:\n 11 : 获取app id\n 12 获取二维码\n 13 还没想好",
            "11": "username : \nr53tiqnz9x@icloud.com \n password:\n Wm123056",
            "12": {"type": "img", "path": "shadowsocks_qrcode_123.gif"},
            "13": "敬请期待...",
            "2": "开发中...",
            "3": "mac 指南 :获取shadowsockx.dmg ,安装 ,安装完成后桌面右上角找到小飞机图标 ,再屏幕上打开二维码 点击小飞机 选择扫描屏幕上二维码, 再次点击小飞机 选择开启获取shadowsocks"
                 "\n更多帮助 --> 请发送数字\n 31:获取dmg文件 \n 32:获取二维码",
            "31": {"type": 'file', "path": 'shadowsocksx.dmg'},
            "32": {"type": "img", "path": "shadowsocks_qrcode_123.gif"},
            "4": "开发中...",
            "5": "处于成本考虑当前只开放一个节点,限定10人使用,因是众筹模式 所以只收服务器成本价 一个月20刀 折合135.738软妹,平均一人13.5738软,同时将也已将服务器带宽完全放开,如需更多节点欢迎大佬众筹再开",
            "help": "发送 -> 我要像梦一样自由 <- \n 开启新世界",
            "Help": "发送 -> 我要像梦一样自由 <- \n 开启新世界",
        }
        res = reply_list[key]
    except KeyError as e:
        res = "no_msg"
    return res
