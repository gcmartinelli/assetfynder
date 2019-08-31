from fetcher import Fetcher
import json


class Fetch(Fetcher):
	def __init__(self):
		self.service_url = 'https://certspotter.com/api/v0/certs?domain={}'
	
	def subdomains(self, domain):
		c = self.fetch(domain)
		try:
			json_ = json.loads(c)
			if json_:
				return json_[0]['dns_names']	
			else:
				return None
		except Exception as e:
			print(f'[*] Error parsing json for {self.service_url}: {e}')
			return None
