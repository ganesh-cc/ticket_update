
import endpointGenerator
import freshdeskService
import processData
import slackService
from collections import defaultdict

fd = defaultdict(list)

def integrator_func(team):
	tag = endpointGenerator.url_generator_multiple(team)
	global fd
	for k,v in tag.items():
		fd.clear()
		print('\n' + '\n' +'\n' +k)
		if k == "closed":
			fd = freshdeskService.trigger_filter(v)
			if fd != 0:
				fd = processData.dataMapper(fd)
		else:
			fd = freshdeskService.trigger(v)
			if fd != 0:
				fd = processData.dataMapper(fd)
		#slackService.post_slack(team, k, str(fd))
		print(team, k, fd)

