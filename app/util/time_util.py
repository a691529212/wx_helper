#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/1/11 下午9:00
# @Author   : Vampire
# @Site     :  
# @File     : time_util.py
# @Software : PyCharm


import time

format_str_ymdHMS = "%Y-%m-%d %H:%M:%S"
format_str_ymdHM = "%Y-%m-%d %H:%M"
format_str_ymd = "%Y-%m-%d"
format_2_week = "%A"
format_2_hour = "%H"


def getDateStr2ymdhms(timeRes=time.time()):
    return __time_transform(format_str_ymdHMS, timeRes)


def getDateStr2ymdh(timeRes=time.time()):
    return __time_transform(format_str_ymdHM, timeRes)


def getDateStr2ymd(timeRes=time.time()):
    return __time_transform(format_str_ymd, timeRes)


def getWeekDay(timeRes=time.time()):
    return __time_transform(format_2_week, timeRes)


def check_morning_night(timeRes=time.time()):
    if int(__time_transform(format_2_hour, timeRes)) > 5 and int(__time_transform(format_2_hour, timeRes)) < 9:
        return '早晨'
    elif int(__time_transform(format_2_hour, timeRes)) > 9 and int(__time_transform(format_2_hour, timeRes)) < 11:
        return '上午'
    elif int(__time_transform(format_2_hour, timeRes)) > 11 and int(__time_transform(format_2_hour, timeRes)) < 13:
        return '中午'
    elif int(__time_transform(format_2_hour, timeRes)) > 13 and int(__time_transform(format_2_hour, timeRes)) < 18:
        return '下午'
    elif int(__time_transform(format_2_hour, timeRes)) > 18:
        return '晚上'
    else:
        return '凌晨'


def __time_transform(type=format_str_ymdHMS, timeRes=time.time()):
    try:
        if isinstance(timeRes, str):  # 传入的是str
            return time.strftime(type, time.strptime(timeRes, format_str_ymdHMS))
        elif isinstance(timeRes, float):  # 传入的是float
            return time.strftime(type, time.localtime(timeRes))
        elif isinstance(timeRes, int):  # 传入的是int
            return time.strftime(type, time.localtime(float(timeRes)))
        else:
            return timeRes
    except ValueError:
        return timeRes
