#-*- coding:utf-8 -*-
import re
import os

TAGS = {u'正常号码':'normal',u'关机':'poweroff',u'空号':'dead',u'垃圾号码':'junk',u'来电提醒':'reminder',u'其它':'other',u'请勿来电':'do_not_call',u'停机':'halt',u'呼入限制':'barring',u'无法接通':'not_available'}


for filename in os.listdir('.'):
    for tag,name in TAGS.items():
        if re.search(tag,filename.decode('utf-8')):
            print tag,name
            lines = file(filename).readlines()
            number = 0
            for l in lines:
                number += 1
                if l.startswith("========"):
                    number = 0
            print "%s: %d行。" % (tag.encode('utf-8'),number)


                    

