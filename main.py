'''
Time: 2026/08/21 00:52:56
Author: Yuzhouxing
GitHub: https://github.com/yuzhouxing-git
Project: Bilibili Video Comments Get
Version: V1.0
File: main.py
Software: python3.8.6
'''
from config import *
import requests
import time
import re
import csv
import random

def getOid(bvid):
	url = f"https://www.bilibili.com/video/{bvid}"
	headers ={
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
	}

	try:
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			match = re.search(r'"aid":(\d+)', response.text)
			if match:
				return int(match.group(1))
			else:
				return None
		else:
			return None
	except Exception as e:
		return None

def catchComment(bvid, oid, cookies, page=0):
	url = f"https://api.bilibili.com/x/v2/reply/main?oid={oid}&type=1&next={page}&mode=3&wts={time.time()}"
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
		'Referer': f'https://www.bilibili.com/video/{bvid}',
		'Origin': 'https://www.bilibili.com',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
		'Accept-Encoding': 'gzip, deflate, br',
		'Cookie': cookies
	}

	try:
		response = requests.get(url, headers=headers, timeout=10)
		if response.status_code == 200:
			data = response.json()
			if data['code'] == 0:
				return data['data']['replies']
			else:
				return []
		else:
			return []
	except Exception as e:
		return []

def catchMoreComments(bvid, cookies, maxPage=100):
	oid = getOid(bvid)
	comments = []
	page = 0
	while page < maxPage:
		temp = catchComment(bvid, oid, cookies, page)
		if not temp:
			break
		comments.append(temp)
		page += 1
		time.sleep(random.uniform(3,6))
	return comments

def save(bvid, cookies, maxPage=100):
	fieldnames = ["名字", "评论", "点赞数", "时间"]
	with open("comment.csv", "w", encoding="utf-8-sig", newline="") as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()

		for i in catchMoreComments(bvid, cookies, maxPage):
			for j in i:
				row = {
					"名字": j['member']['uname'],
					"评论": j['content']['message'],
					"点赞数": j['like'],
					"时间": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(j['ctime']))
				}
				writer.writerow(row)

if __name__ == "__main__":
	save(bvid, cookies, maxPage)