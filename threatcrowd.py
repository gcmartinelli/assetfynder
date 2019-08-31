from fetcher import Fetcher
import json


class Fetch(Fetcher):
	def __init__(self):
		self.service_url = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}'
	
	def subdomains(self, domain):
		try:
			c = self.fetch(domain)
			json_ = json.loads(c)
			if json_:
				return json_['subdomains']	
			else:
				return None
		except Exception as e:
			print(f'[*] Error parsing json for {self.service_url}: {e}')
			return None
