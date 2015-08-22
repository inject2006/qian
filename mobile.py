#-*- coding:utf-8 -*-

import MySQLdb
import time
import os
last_time_file = "last_get_log_time.txt"
if __name__ == "__main__":
    conn=MySQLdb.connect(host='183.131.78.214',user="root",passwd="Bigsec_888;",db="bigsec_platform",charset="utf8")
    cur=conn.cursor()
    cur.execute("select count(distinct mobile) from analyser;")
    length, = cur.fetchone()
    print "all length: ",length
    print "start read from mysql."
    last_time = os.popen('tail -1 %s'%last_time_file).read()
    print last_time
    cur.execute("select distinct mobile from analyser where time>%s;",(last_time,))
    mobiles = cur.fetchall()
    print "distinct mobile length %d." % len(mobiles)
    with open('log_mobiles.txt','w') as f:
        for i,record in enumerate(mobiles):
            mobile, = record
            # print "write %d  %s " % (i,mobile)
            try:
                f.write(mobile+'\n')
            except TypeError:
                print "catch %s" % mobile

    with file(last_time_file,'a') as f:
	now = time.time()
	f.write(str(now)+'\n')
	


