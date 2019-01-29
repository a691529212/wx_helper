#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/1/26 下午4:28
# @Author   : Vampire
# @Site     :  
# @File     : setup.py.py
# @Software : PyCharm

from setuptools import setup

setup(
    name='xc_helper',
    version='1.0',
    long_description=__doc__,
    packages=['app', 'app._db', 'app.exception'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.10',
        'Flask-Mail>=0.9',
        'Flask-SQLAlchemy>=2.1'
    ]
)