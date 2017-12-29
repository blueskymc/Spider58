#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a main page module '

__author__ = 'Ma Cong'

import re
import MySqlHelper

class basePage(object):
    def __init__(self, url):
        self.url = url
        self.sql = MySqlHelper.MySQL_Utils()
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Connection': 'keep-alive'}

    def request_details(self):
        return None

    def dataToSqlInfo(self, sql, data):
        strSqlCount = "select * from info;"
        result = sql.exec_sql(strSqlCount)
        count = len(result)
        sqlStr = "INSERT INTO info VALUES (%d, %s);" % (count + 1, data.toSql())
        #strSqlName = "select * from info where title='%s';" % data.title
        #resultName = sql.exec_sql(strSqlName)
        #countName = len(resultName)
        # if countName < 1:
        #     #print(sqlStr)
        #     sql.exec_txsql(sqlStr)
        # else:
        #     print('已存在信息：' + data.title)
        sql.exec_txsql(sqlStr)  # 重名的也放入数据库

    def getText(self, list):
        if len(list) > 0:
            return list[0].getText()
        else:
            return ''

    def deleteEmpty(self, str):
        str = str.replace(' ', '')
        str = re.sub(r'\r', '', str)
        return re.sub(r'\n', '', str).replace(' ', '')