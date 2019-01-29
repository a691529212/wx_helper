#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/1/11 上午9:49
# @Author   : Vampire
# @Site     :  
# @File     : dfa.py
# @Software : PyCharm

import sys


class Node(object):
    def __init__(self):
        self.children = None


# The encode of word is UTF-8
def add_word(root, word):
    node = root
    for i in range(len(word)):
        if node.children == None:
            node.children = {}
            node.children[word[i]] = Node()
        elif word[i] not in node.children:
            node.children[word[i]] = Node()

        node = node.children[word[i]]


def init(path):
    root = Node()
    fp = open(path, 'r')
    for line in fp:
        line = line[0:-1]
        add_word(root, line)
    fp.close()
    return root


def is_contain(msg, root):
    for i in range(len(msg)):
        p = root
        j = i
        while (j < len(msg) and p.children != None and msg[j] in p.children):
            p = p.children[msg[j]]
            j = j + 1

        if p.children == None:
            # print '---word---',message[i:j]
            return True

    return False


def dfa(msg):
    root = init('/Users/vampire/PycharmProjects/wx_helper/app/util/dangerous.txt')
    return is_contain(msg, root)
