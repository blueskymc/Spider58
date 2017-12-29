#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a main page module '

__author__ = 'Ma Cong'

import requests
import re
import time
import random
from bs4 import BeautifulSoup
import json
import data_struct as ds
import MySqlHelper
import detailPage
import basePage as bp

class page(bp.basePage):
    def save_info_from_mainpage(self, shiqu):
        list = self.request_details()
        for data in list:
            data.shiqu = shiqu
            self.dataToSqlInfo(self.sql, data)

    def hasHttpLink(self, tag):
        return tag.has_attr('logr') and tag.has_attr('_pos')

    def request_details(self):
        print(self.url)
        f = requests.get(self.url, headers=self.header)
        soupAll = BeautifulSoup(f.text, 'lxml')
        listLi = soupAll.select('li')
        listLi = filter(self.hasHttpLink, listLi)
        listData = []
        for li in listLi:
            soup = BeautifulSoup(str(li), 'lxml')
            title = self.getText(soup.select('.title'))
            mianshui = ''
            date = self.getText(soup.select('.time'))
            view_num = ''
            price = self.getText(soup.select('.price > .sum'))
            avg = self.getText(soup.select('.unit'))
            lTmp = soup.select('.baseinfo > span')
            if(len(lTmp) > 0):
                shitingwei = lTmp[0].getText()
            else:
                shitingwei = ''
            if (len(lTmp) > 1):
                area = lTmp[1].getText()
            else:
                area = ''
            if (len(lTmp) > 2):
                toward = lTmp[2].getText()
            else:
                toward = ''
            if (len(lTmp) > 3):
                cenggao = lTmp[3].getText()
            else:
                cenggao = ''

            zhuangxiu = ''
            age = ''
            list = soup.select('.baseinfo > span > a')
            if len(list) > 0:
                xiaoqu = list[0].getText()
            else:
                xiaoqu = ''
            if len(list) > 1:
                weizhi = list[1].getText()
            else:
                weizhi = ''
            if len(list) > 2:
                weizhi += list[2].getText()
            jingjiren = self.getText(soup.select('.jjrinfo'))

            title = self.deleteEmpty(title)
            area = self.deleteEmpty(area)
            avg = self.deleteEmpty(avg)
            price = self.deleteEmpty(price)
            shitingwei = self.deleteEmpty(shitingwei)
            xiaoqu = self.deleteEmpty(xiaoqu)
            weizhi = self.deleteEmpty(weizhi)
            jingjiren = self.deleteEmpty(jingjiren)

            data = ds.info(title, mianshui, date, view_num, price, avg, shitingwei, cenggao,
                           area, zhuangxiu, toward, age, xiaoqu, weizhi, jingjiren, '')
            listData.append(data)

        return listData

    def get_link(self):
        f = requests.get(self.url)
        soup = BeautifulSoup(f.text, 'lxml')
        links = soup.select('.house-list-wrap > li > .pic > a')
        link_list = []
        for link in links:
            link_content = link.get('href')
            if 'ershoufang' in link_content:
                link_list.append(link_content)
        return link_list

    def save_info_from_detailpages(self, shiqu):
        link_list = self.get_link()
        for link in link_list:
            dp = detailPage.page(link)
            dp.read_and_write()
            time.sleep(10 + random.randint(1, 10))
