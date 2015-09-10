#-*- coding:utf-8 -*-

import MySQLdb
import time
import os
if __name__ == "__main__":
    conn=MySQLdb.connect(host='183.131.78.214',user="root",passwd="Bigsec_888;",db="bigsec_platform",charset="utf8")
    cur=conn.cursor()
    cur.execute("select count(distinct mobile,ip) from analyser;")
    length, = cur.fetchone()
    print "all length: ",length
    print "start read from mysql."
    cur.execute("select distinct mobile,ip from analyser where mobile is not null and ip is not null;")
    mobiles = cur.fetchall()
    print "distinct mobile,ip not null length %d." % len(mobiles)
    with open('all_log.txt','w') as f:
        for i,record in enumerate(mobiles):
            mobile,ip = record
            # print "write %d  %s " % (i,mobile)
            try:
                f.write(mobile+' '+ip+'\n')
            except TypeError:
                print "catch %s,%s" % (mobile,ip)

	

