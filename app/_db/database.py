#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2018/12/30 下午1:51
# @Author   : Vampire
# @Site     :  
# @File     : database.py
# @Software : PyCharm

import pymongo, threading, time


class Mongo():

    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["wx_db"]

    def insert(self, table_name, data):
        data['create_time'] = int(time.time())
        data['update_time'] = int(time.time())
        try:
            col = self.mydb[table_name]
            col.insert(data)
            return 1
        except pymongo.errors.DuplicateKeyError as e:
            print(e)
            return 0

    def query(self, table, data):
        print('query from %s' % table, data)
        return self.mydb[table].find(data)

    def query_by_id(self, table_name, value):
        return self.mydb[table_name].find({
            '_id': value
        })[0]

    def update(self, table_name, condition, data):
        import bson
        try:
            self.mydb[table_name].update_many(condition, {'$set': data})
            print('update %s where ' % table_name, " to ", condition, data)
        except bson.errors.InvalidDocument as   e:
            print('no data to update')

    def delete_table(self, table):
        res = input('make sure to delete table %s ? (Y/N)...' % table)
        if res == "Y":
            x = self.mydb[table].delete_many({}).deleted_count
            print('u have deleted %s ... total data %d' % (table, x))
        elif res == "N":
            print('cancel delete table %s ...' % table)
        else:
            print('wrong input ...')

    '''
    排序查询
    @table_name:表名
    @column_name :要排序的字段
    @direction : 1 升序 ;-1降序
    '''

    def sort(self, table_name, column_name, direction=1):
        return self.mydb[table_name].find().sort(column_name, direction=direction)
