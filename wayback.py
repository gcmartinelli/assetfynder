from fetcher import Fetcher
import json

class Fetch(Fetcher):
	def __init__(self):
		self.service_url = 'http://web.archive.org/cdx/search/cdx?url=*.{}/*&output=json&collapse=urlkey'
	
	def subdomains(self, domain, verbose):
		c = self.fetch(domain, verbose)
		try:
			subs = []
			json_ = json.loads(c)
			for block in json_[2:]: # the first couple of blocks don't bring new info
				subs.append(block[2])
			if len(subs) > 0:
				return subs
			else:
				return None
		except Exception as e:
			print(f'[*] Error parsing json for {self.service_url}: {e}')
			return None
