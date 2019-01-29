#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/1/26 上午9:27
# @Author   : Vampire
# @Site     :  
# @File     : wx_infos.py
# @Software : PyCharm

import threading
import itchat
import xmltodict, json
from itchat.content import *
from app._db.database import Mongo
from app.util.dfa import dfa
from app.model.reply_rule import reply


@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def msg_receive(msg):
    print(json.dumps(msg))
    if msg['FromUserName'].startswith("@@"):
        print('receive msg :\n', "from group %s - %s : %s" % (msg['User']['NickName'], msg['ActualNickName'], msg.text))
        if (dfa(msg.text)):
            itchat.add_friend(msg.actualUserName, verifyContent='嘿嘿')
            s = "中国共产党同全国各民族工人、农民、知识分子团结在一起，同各民主党派、无党派人士、各民族的爱国力量团结在一起，进一步发展和壮大由全体社会主义劳动者、社会主义事业的建设者、拥护社会主义的爱国者、拥护祖国统一和致力于中华民族伟大复兴的爱国者组成的最广泛的爱国统一战线。"
            return "%s  ! %s" % (msg.actualNickName, s)
        if '加我好友' in msg.text:
            itchat.add_friend(msg.actualNickName, verifyContent='hello')
            itchat.send_msg('asdf', toUserName=msg.actualNickName)
        if msg.isAt:
            # someone @me
            msg.user.send(u'@%s\u2005 : 我收到了 --> %s 不要急...' % (
                msg.actualNickName, msg.text))
        return
    res = reply(msg.text)
    print('receive msg :\n', "from friends %s : %s" % (msg['User']['NickName'], msg.text))
    if isinstance(res, dict):
        ty = res['type']
        if ty == 'img':
            itchat.send_image(res['path'], msg['FromUserName'])
        elif ty == 'file':
            itchat.send_file(res['path'], msg['FromUserName'])
    elif isinstance(res, str):
        if res == 'no_msg':
            pass
        else:
            return res


@itchat.msg_register(MAP, isFriendChat=True, isGroupChat=True, isMpChat=True)
def map_receive(msg):
    print('map========>\n', msg)


@itchat.msg_register(CARD, isFriendChat=True, isGroupChat=True, isMpChat=True)
def card_receive(msg):
    print('card========>\n', msg)


# xxx邀请xx进群
@itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)
def note_receive(msg):
    uname = str(msg.content).split('"')[1]
    if str(msg.content).__contains__('加入'):
        itchat.send_msg("欢迎 %s  \n 你可以发送 -> 我要像梦一样自由 <- \n 开启新世界" % uname, toUserName=msg['FromUserName'])
    elif str(msg.content).__contains__('移出'):
        itchat.send_msg("%s , 违反律令,被就地正法!" % uname)


@itchat.msg_register(SHARING, isFriendChat=True, isGroupChat=True, isMpChat=True)
def sharing_receive(msg):
    print('%s========>\n' % msg['Type'], msg)


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True, isGroupChat=True, isMpChat=True)
def pic_receive(msg):
    print('%s========>\n' % msg['Type'], msg)
    print(msg.fileName)
    msg.download(msg.fileName)


@itchat.msg_register(FRIENDS, isFriendChat=True, isGroupChat=True, isMpChat=True)
def friends_receive(msg):
    print('%s========>\n' % msg['Type'], msg)
    print(msg.text['autoUpdate']['Content'])
    message = msg.content
    xml_dict = xmltodict.parse(message)
    json_str = json.dumps(xml_dict)
    json_dict = json.loads(json_str)
    print("res : ====== >", json_str)
    print("dict : ====== >", json_dict)
    if msg.text['autoUpdate']['Content'] == '梯子':
        msg.user.verify()
        msg.user.send('Nice to meet you! \n 你可以发送 -> 给我梯子 <- \n 获取帮助')


@itchat.msg_register(SYSTEM, isFriendChat=True, isGroupChat=True, isMpChat=True)
def sys_receive(msg):
    pass



class wx_util(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name="wx")
        self.setDaemon(False)

    def run(self):
        itchat.auto_login(picDir='qr_img.png',hotReload=True)
        itchat.run()
