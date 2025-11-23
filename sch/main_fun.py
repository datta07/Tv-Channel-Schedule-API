import requests
import json
from threading import Thread
import threading


class ThreadWithReturnValue(Thread):
	def __init__(self, group=None, target=None, name=None,args=(), kwargs={}, Verbose=None):
		Thread.__init__(self, group, target, name, args, kwargs)
		self._return = None
		self._stop_event = threading.Event()
	def run(self):
		#print(type(self._target))
		if self._target is not None:
			self._return = self._target(*self._args,**self._kwargs)
	def join(self, *args):
		Thread.join(self, *args)
		return self._return
	def terminate(self):
		self._stop_event.set()

path='sch'
headers={"appkey":"l7xx938b6684ee9e4bbe8831a9a682b8e19f","usergroup":"tvYR7NSNn7rymo3F","User-Agent":"Dalvik/2.1.0 (Linux; U; Android 10.0.0; Redmi 4A Build/OMC28.71-56)"}

def getCategories():
	with open(path+'/categories.json','r') as f:
		data=json.loads(f.read())
	data_json={"categories":list(data["categories"].keys()),"languages":list(data["languages"].keys())}
	return data_json# jsonify before sending it

def searchChannel(lang=False,cate=False):
	with open(path+'/categories.json','r') as f:
		data=json.loads(f.read())
		categories,languages=data["categories"],data["languages"]
	try:
		if (lang):
				lang=languages[lang]
	except Exception:
		return "invalid language search /getCategories"
	try:
		if (cate):
			cate=categories[cate]
	except Exception:
		return "invalid categories search /getCategories"
	with open(path+'/channel.json','r') as f:
		data=json.loads(f.read())
	data.pop("Updated-on")
	data_json=[]
	if (lang&cate):
		for i in data:
			if (data[i]['lang']==lang)&(data[i]['cate']==cate):
				data_json.append(i)
	elif (lang):
		for i in data:
			if (data[i]['lang']==lang):
				data_json.append(i)
	elif (cate):
		for i in data:
			if (data[i]['cate']==cate):
				data_json.append(i)
	return data_json

def TodaySchedule(channel=False,offset=0):
	with open(path+'/channel.json','r') as f:
		data=json.loads(f.read())
	try:
		channel=data[channel]['id']
	except Exception:
		return "invalid categories search /searchChannel"
	res=requests.get("https://jiotv.data.cdn.jio.com/apis/v1.3/getepg/get?offset="+str(offset)+"&channel_id="+str(channel)+"&langId=6",
				  headers= {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,te;q=0.6,hi;q=0.5",
    "cache-control": "max-age=0",
    "cookie": "_ga_68JYTCB6GJ=GS1.1.1740234955.1.1.1740235706.0.0.0; _ga=GA1.1.350865693.1740234823; _ga_KTDCM7ZGJS=GS1.1.1740234823.1.1.1740235726.0.0.0",
    "priority": "u=0, i",
    "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
				  })
	# print("https://jiotv.data.cdn.jio.com/apis/v1.3/getepg/get?offset="+str(offset)+"&channel_id="+str(channel)+"&langId=6")
	# print("output is",res.status_code,res.text)
	res=res.json()
	data_json={}
	for i in res['epg']:
		data_json[i["showtime"]]={"name":i["showname"],"type":i["showCategory"],"other-details":i["description"]}
	return data_json

def GetChannelMovie(i,offset=0):
	k={}
	res=requests.get("https://jiotv.data.cdn.jio.com/v1.3/getepg/get?offset="+str(offset)+"&channel_id="+str(i)+"&langId=6",
				headers= {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,te;q=0.6,hi;q=0.5",
    "cache-control": "max-age=0",
    "cookie": "_ga_68JYTCB6GJ=GS1.1.1740234955.1.1.1740235706.0.0.0; _ga=GA1.1.350865693.1740234823; _ga_KTDCM7ZGJS=GS1.1.1740234823.1.1.1740235726.0.0.0",
    "priority": "u=0, i",
    "sec-ch-ua": '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
				  } ).json()
	for i in res['epg']:
		if (i["showCategory"]=="Film"):
			k[i["showtime"]+'   :- '+res["channel_name"]]=i["showname"]+' ('+i["starCast"]+')'
			#data_json[i["showtime"]]={"name":i["showname"],"type":i["showCategory"],"other-details":i["description"]}
	return k

def GetTodaysMovies(lang=False,offset=0):
	with open(path+'/channel.json','r') as f:
		data=json.loads(f.read())
	if (not lang):
		return "invalid language entry /getCategories"
	data.pop("Updated-on")
	with open(path+'/categories.json','r') as f:
		lang=json.loads(f.read())["languages"][lang]
	channels=[]
	for i in data:
		if (data[i]["lang"]==lang):
			if (data[i]["cate"]==6)|(data[i]["cate"]==5):
				channels.append(data[i]['id'])
	k={}
	arr=[]
	for no,i in enumerate(channels):
		arr.append(ThreadWithReturnValue(target=GetChannelMovie,args=(i,offset)))
		arr[no].start()

	for i in arr:
		temp_k=i.join()
		for j in temp_k:
			k[j]=temp_k[j]

	key=list(k.keys())
	key.sort()
	matter=''
	for i in key:
		hin=i+' : '+k[i]+'<br>'
		matter+=hin
	return matter


print(TodaySchedule(channel="Zee Telugu"))