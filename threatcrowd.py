from fetcher import Fetcher


class Fetch(Fetcher):
	def __init__(self):
		self.service_url = 'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}'
	
	def subdomains(self, domain):
		json = self.fetch(domain)
		if json:
			return json['subdomains']	
		else:
			return None
