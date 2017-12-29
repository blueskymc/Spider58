#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a detail page module '

__author__ = 'Ma Cong'

import pandas as pd
import numpy as np
import MySqlHelper

class csv(object):
    def __init__(self):
        import pymysql
        pymysql.install_as_MySQLdb()
        self.sqlHelper = MySqlHelper.MySQL_Utils()

    def readSql(self):
        sqlAll = "SELECT id, title, price, avg, shitingwei, cenggao, \
                        area, xiaoqu, weizhi, jingjiren, shiqu FROM info_main"
        result = self.sqlHelper.exec_sql(sqlAll)
        for data in result:
            data['price'] = data['price'].replace('万', '')
            data['avg'] = data['avg'].replace('元/㎡', '')
            data['area'] = data['area'].replace('㎡', '')
        df = pd.DataFrame(list(result))
        cols = ['id', 'title', 'shiqu', 'area', 'price', 'avg', 'shitingwei', 'xiaoqu', 'cenggao',
                 'weizhi', 'jingjiren']
        df = df.ix[:, cols]
        df['总价'] = df.price.astype(float)
        df['均价'] = df.avg.astype(float)
        df['面积'] = df.area.astype(float)
        df['id'] = df.index
        #df.to_csv('data.csv', encoding='gbk')
        self.df = df

    def range_show(self):
        listRange = []
        listValue = []
        for i in range(0, 30):
            min = i * 1000
            max = (i + 1) * 1000 - 1
            dfTmp = self.filter(avgMin=min, avgMax=max)
            listRange.append(str(i) + '-' + str(i+1))
            listValue.append(len(dfTmp))
        data = {
                    '范围': listRange,
                    '二手房数量数量': listValue
                }
        newdf = pd.DataFrame(data)
        newdf.to_csv('tmp.csv', encoding='gbk')
        self.plot(newdf, title='各价格区间二手房数量-总样本数14000个')

    def computePriceByXiaoqu(self, df):
        mean = df.groupby('xiaoqu').mean()
        mean["小区"] = mean.index
        count = df.groupby('xiaoqu').size()
        df2 = pd.DataFrame(count, columns=['样本数量'])
        df2["小区"] = df2.index
        dfAll = pd.merge(mean, df2, left_on="小区", right_on="小区")
        dfAll = dfAll.loc[(dfAll['样本数量'] > 5)]
        dfAll.to_csv('各小区价格.csv', encoding='gbk')

    def computePriceByShiqu(self, df):
        mean = df.groupby('shiqu').mean()
        mean["市区"] = mean.index
        count = df.groupby('shiqu').size()
        df2 = pd.DataFrame(count, columns=['样本数量'])
        df2["市区"] = df2.index
        dfAll = pd.merge(mean, df2, left_on="市区", right_on="市区")
        dfAll = dfAll.loc[(dfAll['样本数量'] > 5)]
        dfAll.to_csv('各市区价格.csv', encoding='gbk')

    def filter(self, areaMin=30, areaMax=300, avgMin=3000, avgMax=30000):
        return self.df.loc[(self.df['面积'] < areaMax) & (self.df['面积'] > areaMin) &
                              (self.df['均价'] < avgMax) & (self.df['均价'] > avgMin)]

    def avgMean(self):
        mean = self.df.describe()
        return mean
        #print(mean.loc['mean', '均价'])

    def showPlot(self, dataf, title='58同城保定各小区二手房数量-总样本数14000个', column="xiaoqu", min=50, kind='bar'):
        dataf["tl"] = dataf[column].astype("category")
        counts = dataf[column].value_counts()
        counts.to_csv('58同城保定各小区二手房数量.csv', encoding='gbk')
        sOther = pd.Series([0], index=['其他'])
        counts = counts.append(sOther)
        dct = counts.to_dict()
        s = []
        for item in dct:
            if dct[item] < min:
                #dct['其他'] += dct[item]
                s.append(item)
        for k in s:
            dct.pop(k)

        counts = pd.Series(dct)
        counts = counts.sort_values(ascending=False)

        p = counts.plot(kind=kind).get_figure()  # 柱：bar；饼：pie
        p.suptitle(title)
        p.set_size_inches(13, 8)
        p.savefig(title + '.png', dpi=100)
        print('文件保存在：'+ title + '.png')

    def plot(self, df, title='标题-总样本数14000个', kind='bar'):
        p = df.plot(kind=kind).get_figure()  # 柱：bar；饼：pie
        p.suptitle(title)
        p.set_size_inches(13, 8)
        p.savefig(title + '.png', dpi=100)
        print('文件保存在：' + title + '.png')