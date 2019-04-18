#!/usr/bin/env python
# coding: utf-8
import re
import pandas as pd
import jieba
import cpca
import numpy as np
def tiqu(string):
    li=[]
    a=re.sub("[A-Za-z0-9\!\%\[\]\,\。\{\}\"\"\:]", "", string)
    li.append(a)
    s=cpca.transform(li,cut=False)
    s=s.drop(['区','地址'],axis=1)
    sheng=s.loc[0,'省']
    shi=s.loc[0,'市']
    #------------标准地区表处理-----------
    shi_data=pd.read_excel('市地区编码.xlsx',sheet_name='Sheet1')

    if shi!='':
        for index, row in shi_data.iterrows():
            if row['city']==shi:
                area_code=row['area_code']
                print(area_code)
    elif shi==''and sheng!='':
        sheng_data=pd.read_excel('市地区编码.xlsx',sheet_name='Sheet2')
        for index, row in sheng_data.iterrows():
            if row['province']==sheng:
                area_code=row['area_code']
                print(area_code)
    else:
        print("非地区字符")
tiqu('江苏南京')










