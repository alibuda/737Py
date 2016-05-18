# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:21:05 2016

@author: Administrator
"""

#%%
import cx_Oracle as cO
import pandas as pd
from pandas import Series,DataFrame
from matplotlib import pyplot as plt
import numpy as np
#%%
con_str = u'adp_pm/adp_pm@192.168.3.129:1521/gtf'
con = cx_Oracle.connect(con_str)
c = con.cursor()
r = c.execute(u'''select s.report_content_datetime,s.engine_id,s.tgt,s.tat,s.epr,s.alt from pm_a330_eng_r04_src s where s.aircraft_id = (select id from asset_aircraft_tail t where t.aircraft_no = 'B-5932') and s.engine_place = 2 order by s.report_content_datetime''')
dat = DataFrame(r.fetchall(),columns = ['report_content_datetime','engine_id','tgt','tat','epr','alt'])
#%%
roll = dat[[2,3]].rolling(180)
#plt.plot(dat.ix[:,2],'ro')