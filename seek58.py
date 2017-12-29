#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' seek 58 city module '

__author__ = 'Ma Cong'

import mainPage
import time
import random

class seek58(object):
    def __init__(self):
        linkGkq = 'http://bd.58.com/gaokaiqu/ershoufang/h1/pn{}'
        linkXsq = 'http://bd.58.com/xinshiqu/ershoufang/h1/pn{}'
        linkBsq = 'http://bd.58.com/beishi/ershoufang/h1/pn{}'
        linkNsq = 'http://bd.58.com/nanshiqu/ershoufang/h1/pn{}'
        self.listLink = [linkNsq, linkXsq, linkBsq, linkGkq]
        #self.listLink = [linkGkq]

    def seek(self):
        shiqu = 0
        for linkTmp in self.listLink:
            shiqu += 1
            print('换市区了：' + linkTmp)
            start = 41
            end = 70
            urls = [linkTmp.format(i) for i in range(start, end)]
            for url in urls:
                mp = mainPage.page(url)
                #mp.save_info_from_mainpage(shiqu)
                mp.save_info_from_detailpages(shiqu)
                time.sleep(5)
                #time.sleep(10 + random.randint(1, 10))