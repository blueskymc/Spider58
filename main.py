#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a spider module '

__author__ = 'Ma Cong'

import seek58
import excute_csv

def main():
    s1 = seek58.seek58()
    #s1.seek()

    csv = excute_csv.csv()
    csv.readSql()
    #csv.showPlot(csv.df)
    #csv.showPlot(csv.df, title='58同城保定二手房结构统计-总样本数14000个', column="shitingwei", min=15)
    para = [30, 300, 3000, 30000]
    #csv.filter(areaMin=para[0], areaMax=para[1], avgMin=para[2], avgMax=para[3])
    #print(csv.avgMean())
    #csv.range_show()
    #csv.computePriceByXiaoqu(csv.filter(avgMin=para[2], avgMax=para[3]))
    csv.computePriceByShiqu(csv.filter(avgMin=para[2], avgMax=para[3]))

if __name__ == '__main__':
    main()