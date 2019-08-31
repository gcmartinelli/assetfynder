from fetcher import Fetcher


class Fetch(Fetcher):
	def __init__(self):
		self.service_url = 'https://certspotter.com/api/v0/certs?domain={}'
	
	def subdomains(self, domain):
		json = self.fetch(domain)
		if json:
			return json[0]['dns_names']	
		else:
			return None
