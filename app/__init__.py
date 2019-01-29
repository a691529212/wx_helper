#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/1/10 下午3:15
# @Author   : Vampire
# @Site     :  
# @File     : __init__.py.py
# @Software : PyCharm

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import json


# app = Flask(__name__)
# CORS(app)
# app.secret_key = 'd7874cd2fd1bc7683c00006c922768e2'
# api = Api(app)
# api.add_resource({r"/hello": {"origins": "*"}})
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# @app.route('/getMsg', methods=['GET', 'POST'])
# def home():
#     response = {
#         'msg': 'Hello, Python !'
#     }
#     return jsonify(response)
#
#
# # 启动运行
# if __name__ == '__main__':
#     app.run()  # 这样子会直接运行在本地服务器，也即是 localhost:5000
