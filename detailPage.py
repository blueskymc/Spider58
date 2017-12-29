#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a detail page module '

__author__ = 'Ma Cong'

import requests
import re
from bs4 import BeautifulSoup
import data_struct as ds
import basePage as bp

class page(bp.basePage):
    def read_and_write(self):
        data = self.request_details()
        self.dataToSqlInfo(self.sql, data)

    def request_details(self):
        print(self.url)
        f = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(f.text, 'lxml')
        title = self.getText(soup.select('.house-title > h1'))
        mianshui = self.getText(soup.select('.house-title > .house-update-info > .ms'))
        date = self.getText(soup.select('.house-title > .house-update-info > .up'))
        view_num = self.getText(soup.select('.house-title > .house-update-info > .up > #totalcount'))
        price = self.getText(soup.select('.house-basic-item1 > .price'))
        avg = self.getText(soup.select('.house-basic-item1 > .unit'))
        shitingwei = self.getText(soup.select('.house-basic-item2 > .room > .main'))
        cenggao = self.getText(soup.select('.house-basic-item2 > .room > .sub'))
        area = self.getText(soup.select('.house-basic-item2 > .area > .main'))
        zhuangxiu = self.getText(soup.select('.house-basic-item2 > .area > .sub'))
        toward = self.getText(soup.select('.house-basic-item2 > .toward > .main'))
        age = self.getText(soup.select('.house-basic-item2 > .toward > .sub'))
        list = soup.select('.house-basic-item3 > li')
        if len(list) > 0:
            xiaoqu = list[0].getText()
        else:
            xiaoqu = ''
        if len(list) > 1:
            weizhi = list[1].getText()
        else:
            weizhi = ''
        # list = soup.find_all("a", class_=["c_000", "agent-name-txt"])
        # list = soup.find('body', {'class': 'agent-name f14 c_555'})
        lis = soup.find(attrs={'class', 'agent-name'})
        # if len(list) > 0:
        if lis is None:
            jingjiren = ''
            # jingjiren = list[0].getText()
        else:
            jingjiren = ''

        price = self.deleteEmpty(price)
        xiaoqu = self.deleteEmpty(xiaoqu)
        weizhi = self.deleteEmpty(weizhi)
        jingjiren = self.deleteEmpty(jingjiren)

        data = ds.info(title, mianshui, date, view_num, price, avg, shitingwei, cenggao,
                       area, zhuangxiu, toward, age, xiaoqu, weizhi, jingjiren, self.url)
        return data

