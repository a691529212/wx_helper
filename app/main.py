#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/1/10 下午3:32
# @Author   : Vampire
# @Site     :  
# @File     : main.py
# @Software : PyCharm

from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify
from app.model.wx_infos import wx_util
import itchat
app = Flask(__name__)
cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sendMsg', methods=['GET', 'POST'])
def home():
    username = request.form['toUser']
    content = request.form['msg']
    itchat.send_msg(content, toUserName=username)
    response = jsonify({
        'msg': 'send msg %s to %s' % (content, username)
    })
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    response.headers['Access-Control-Allow-Headers'] = allow_headers
    print(response)
    return response


@app.route('/getFriends', methods=['POST'])
def getFriends():
    friends = itchat.get_friends()
    for item in friends:
        item['HeadImgUrl'] = 'https://wx.qq.com' + item['HeadImgUrl']
    response = jsonify(friends)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    response.headers['Access-Control-Allow-Headers'] = allow_headers
    return response


@app.route('/login', methods=['POST'])
def login():
    try:
        wx_util.start()
    except RuntimeError as e:
        print(e)
    response = jsonify({'code': 0, "msg": 'success', 'path': '/tmp/qr_img.png'})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    response.headers['Access-Control-Allow-Headers'] = allow_headers
    return response

# 启动运行
if __name__ == '__main__':
    wx_util = wx_util()
    app.run('127.0.0.1', 7587)
