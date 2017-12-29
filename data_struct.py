#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' contract module '

__author__ = 'Ma Cong'

import datetime

# 类
class info(object):
    def __init__(self, title, mianshui, date, view_num, price, avg, shitingwei, cenggao,
                 area, zhuangxiu, toward, age, xiaoqu, weizhi, jingjiren, link):
        '''
        初始化数据结构
        '''
        self.title = self.excuteSting(title)
        self.mianshui = self.excuteSting(mianshui)
        self.date = self.excuteSting(date)
        self.view_num = self.excuteSting(view_num)
        self.price = self.excuteSting(price)
        self.avg = self.excuteSting(avg)
        self.shitingwei = self.excuteSting(shitingwei)
        self.cenggao = self.excuteSting(cenggao)
        self.area = self.excuteSting(area)
        self.zhuangxiu = self.excuteSting(zhuangxiu)
        self.toward = self.excuteSting(toward)
        self.age = self.excuteSting(age)
        self.xiaoqu = self.excuteSting(xiaoqu)
        self.weizhi = self.excuteSting(weizhi)
        self.jingjiren = self.excuteSting(jingjiren)
        self.link = self.excuteSting(link)
        self.shiqu = 0

    def toSql(self):
        return "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s'" % \
               (self.title, self.mianshui, self.date, \
               self.view_num, self.price, self.avg, self.shitingwei, \
               self.cenggao, self.area, self.zhuangxiu, self.toward, self.age,\
               self.xiaoqu, self.weizhi, self.jingjiren, self.link, self.shiqu)

    def excuteSting(self, s):
        if s is str:
            return s.replace(',', '')
        else:
            return s


