import urllib2
import ssl
import json
import sys
import time
import datetime

reload(sys)
sys.setdefaultencoding("utf8")

url="https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2016-09-14&from_station=BJP&to_station=XAY"
req=urllib2.Request(url)
gcontent=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
while True:
	try:
		rep=urllib2.urlopen(req, context=gcontent).read()
		# print rep
		items=json.loads(rep)
		trans=items['data']['datas']
		for tran in trans:
			if tran['station_train_code']=='Z43' and tran['canWebBuy']=="Y":
				print 'YES'
				break
		print datetime.datetime.now()
		time.sleep(10)
	except Exception, e:
		print e