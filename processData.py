import freshdeskService
from collections import defaultdict

name_mapping = {
	480XXXX7506:"agent1",
	480XXXX2697:"agent2",
	480XXXX4635:"agent3",
	480XXXX0364:"agent4"
}

fin = {}
fd = defaultdict(list)

def dataMapper(fd):
	for k in fd:
		for ke, va in name_mapping.items():
			if(k == ke):
				key = name_mapping.get(ke)
				value = fd.get(k)
				fin[key] = value
	return(fin)







