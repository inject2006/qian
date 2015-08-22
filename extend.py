#!/usr/bin/env python
import sys
import traceback
from bigsec_common import base_dao

mysql_url = "mysql://root:Bigsec_888%3b@um.bigsec.com:3306/bigsec_platform?charset=utf8"
if __name__ == "__main__":

    if len(sys.argv) == 2:
        bit = int(sys.argv[1])
    mobile_list = []
    with file('log_mobiles.txt','r') as top_f:
        with file('extend.txt','w') as f:
            for line in top_f:
                mobile = line.split(' ')[-1].strip('\n')
                if not mobile.isdigit():
                    print mobile
                    continue
                for i in xrange(10**int(bit)):
                    d = mobile[:-bit]+str(i).zfill(int(bit))
                    f.write(d+'\n')
                    mobile_list.append(d)

    modem_data_dao = base_dao.ModemDataDao(mysql_url)
    with file('extend.log','w') as fp:
        try:
            g_list = [mobile_list[i:i+5000] for i in range(0, len(mobile_list), 5000)]
            for sub_list in g_list:
                print len(sub_list)
                modem_data_dao.insert_mobile_bulk(sub_list)
        except Exception:
            traceback.print_exc(file=fp)



