import requests
import json

url = {
	"test":"https://en3ogaxunnww2.x.pipedream.net/",
	"rxtech":"https://hooks.slack.com/services/---------"
}

#data '{"text":"Hello, World!"}'

def post_slack(group, name, fd):
	slack_data = "*`" + name + "`*"+ "\n" + str(fd)
	try:
		r = requests.post(url.get(group), json ={"text":slack_data})
		r.raise_for_status()
	except requests.exceptions.RequestException as e:
		raise SystemExit(e)


	
	
	