import requests
import json
from collections import defaultdict


page_value = 1
d = defaultdict(list)
filter_tags = ["survey_sent", "merged"]

def freshdeskfunc(page_value, url):
	url = url
	data = {'page':page_value}
	r = requests.get(url, data, auth=('------', 'x'))
	print(r.url)
	total = r.json().get('total')
	print(total)
	tickets = r.json().get('results')
	return total, tickets


def trigger(url):
	d.clear()
	global page_value
	url = url
	result = freshdeskfunc(page_value, url)
	ticket_count = result[0]
	tics = result[1]
	while (ticket_count>0):
		result = freshdeskfunc(page_value, url)
		ticket_count = result[0]
		tics = result[1]
		for tic in tics:
			key = tic.get('responder_id')
			value = tic.get('id')
			d[key].append(value)
		page_value = page_value + 1
		if (tics == [] or page_value == 11):
			break
	page_value = 1
	print(d)
	return(d)


def trigger_filter(url):
	d.clear()
	global page_value
	url = url
	result = freshdeskfunc(page_value, url)
	ticket_count = result[0]
	tics = result[1]
	while (ticket_count>0):
		result = freshdeskfunc(page_value, url)
		ticket_count = result[0]
		tics = result[1]
		for tic in tics:
			if (tic.get('source')!=7):
				if not ((set(filter_tags) & set(tic.get('tags')))):
					key = tic.get('responder_id')
					value = tic.get('id')
					d[key].append(value)
			page_value = page_value + 1
			if (tics == [] or page_value == 11):
				break
		page_value = 1
		print(d)
		return(d)

