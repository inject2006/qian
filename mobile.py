#-*- coding:utf-8 -*-

import MySQLdb

if __name__ == "__main__":
    conn=MySQLdb.connect(host='183.131.78.214',user="root",passwd="Bigsec_888;",db="bigsec_platform",charset="utf8")
    cur=conn.cursor()
    cur.execute("select count(*) from analyser;")
    length, = cur.fetchone()
    print "start read from mysql."
    cur.execute("select distinct mobile from analyser;")
    mobiles = cur.fetchall()
    print "distinct mobile length %d." % len(mobiles)
    with open('mobiles.txt','a') as f:
        for i,record in enumerate(mobiles):
            mobile, = record
            # print "write %d  %s " % (i,mobile)
            try:
                f.write(mobile+'\n')
            except TypeError:
                print "catch %s" % mobile


