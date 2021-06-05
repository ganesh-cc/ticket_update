import datetime

today = datetime.datetime.now()
date_today = str(today.strftime("'%Y-%m-%d'"))

domain = {"rxtech" : "https://FDdomain.",
	"test" : "https://test."
	}

group_id = {"rxtech" : "(group_id:48xxxxxx211 OR group_id:48xxxxxx713)",
	"test": "test_group_id:00000000"}

base_url = "freshdesk.com/api/v2/search/tickets?query="



tag = {
	"woc":"status:6 AND ",	
	"pending":"status:3 AND ",
	"resolved":"updated_at:" + date_today + " AND status:4 AND ",
	"closed":"updated_at:" + date_today + " AND status:5 AND " ,
	#"test_closed":"updated_at:" + date_today + " AND status:5 " ,
	"OD & Ageing":"due_by:<" + date_today+ " AND (status:3 OR status:12) AND "
}

multiple_url = {}

def url_generator_multiple(groupname):
	groupname_str = ("%s" %groupname)
	print(groupname_str)
	multiple_url.clear()
	for k,v in tag.items():
		url_m = (domain.get(groupname_str))+ base_url + "\"" + v + (group_id.get(groupname_str)) + "\""
		#print(url_m)
		#test_url_m = (domain.get(groupname_str))+ base_url + "\"" + v + "\""
		multiple_url.update({k : url_m})
	return(multiple_url)

def url_generator_open(groupname):
	groupname_str = ("%s" %groupname)
	print(groupname_str)
	url = (domain.get(groupname_str)) + base_url + "agent_id:null AND status:2 AND " + (group_id.get(groupname_str))
	return("'%s'" %url)



