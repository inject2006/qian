#-*- coding:utf-8 -*-
import re
import os
import pandas as pd
import numpy as np
import cairo
import pycha.pie

TAGS = {u'正常号码':'normal',u'关机':'poweroff',u'空号':'dead',u'垃圾号码':'junk',u'来电提醒':'reminder',u'其它':'other',u'请勿来电':'do_not_call',u'停机':'halt',u'呼入限制':'barring',u'无法接通':'not_available'}


def get_stat(entire,part):
    '''
    entire is consists of part.The function return ratio of every keys in part dict.
    '''
    ratio ={}
    for key,df in part.iteritems():
        if df is None:
            ratio[key] = 0
        else:
            ratio[key] = len(np.intersect1d(entire[0].values,df[0].values))
    return ratio  


def draw_pie(stat,title):
    dataSet = []
    for k,v in stat.items():
        dataSet.append((k,((0,v),(0,0),(0,0))))

    options={   
                    'legend':{'hide':False},   
                    'title':title,  
                    'titleColor':'#0000ff',  
                    'titleFont':'字体',  
                    'background':{'chartColor': '#ffffff'},   
                    'axis':{'labelColor':'#ff0000'},  
                }  
    width,height=1000,1000   
    surface=cairo.ImageSurface(cairo.FORMAT_ARGB32,width,height) 
    chart=pycha.pie.PieChart(surface,options)   
    chart.addDataset(dataSet)   
    chart.render()   
    surface.write_to_png('%s.png' % title)   

part = {}
for filename in os.listdir('瞬时空号检测'):
    for tag,name in TAGS.items():
        if re.search(tag,filename.decode('utf-8')):
            print tag
            try: 
                if name == "normal":
                    part[tag] = pd.read_csv(os.path.join('瞬时空号检测',filename),skiprows=19,header=None)
                else:
                    part[tag] = pd.read_csv(os.path.join('瞬时空号检测',filename),skiprows=12,header=None)
            except ValueError:
                part[tag] = None

sample_avail = pd.read_csv('available.txt',header=None)
sample_dis = pd.read_csv('disable.txt',header=None)

stat_avail = get_stat(sample_avail,part)
stat_dis = get_stat(sample_dis,part)
print stat_avail
print stat_dis
draw_pie(stat_avail,"600预测可用号")
draw_pie(stat_dis,"600预测空号")

            #lines = file(filename).readlines()
            #number = 0
            #for l in lines:
                #number += 1
                #if l.startswith("========"):
                    #number = 0
            #print "%s: %d行。" % (tag.encode('utf-8'),number)


                    
