# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 11:19:04 2017

@author: uqrzhan7
"""

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# -*- coding:utf-8 -*-


data = {
'login':   'clarkbear',
'password'    :'superman',
    }

s = requests.session()
s.post(url='https://pvoutput.org/index.jsp',data=data)


date_num = []
date_begin = 20170714;
for a in range (1,18):
    date_num.append(str(date_begin + a))



power_data_row=[]


for k in range (0,10):
    power_data_col=[]
    url = "https://pvoutput.org/intraday.jsp?id=33717&sid=32067&dt="+date_num[k]+"&gs=0&m=0"
    response=s.get(url)
#==============================================================================
# response = requests.get(url)
# URLs : url = "https://pvoutput.org/intraday.jsp?id=33717&sid=32067&dt="+date_num[k]+"&gs=0&m=0"

#==============================================================================
    content = response.content

    parser = BeautifulSoup(content,'html.parser')

    head = parser.head

    data_content = parser.find_all(id = "tb")
#==============================================================================
# 
# data_content_text = data_content.text
#==============================================================================

    tbls = parser.find('table')


    trs = tbls.find_all('tr')

    for i in range(2,len(trs)):
        trs_temp = trs[i]
        tds = trs_temp.find_all("td")
        tds[4] = str(tds[4])
#==============================================================================
#     print(tds[4][46])
#==============================================================================
        power_data = re.findall(">(.*?)W",tds[4])
        power_data = list(filter(str.isdigit, power_data[0]))
        power_data = ''.join(power_data)
        power_data = int(power_data)
        power_data_col.append(power_data)
        
        print(power_data)
    power_data_row[:][k]=(power_data_col)

#==============================================================================
# print(content)
#==============================================================================

