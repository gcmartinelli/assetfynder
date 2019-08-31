import requests

class Fetcher:
	''' Convenience class. Receives a domain name to fetch
		and the url of a service to use.
	'''
	timeout = 10

	def fetch(self, domain, verbose):
		try:
			fetch_url = self.service_url.format(domain)
			r = requests.get(fetch_url, timeout=self.timeout)
			if r.status_code == 200:
				return r.text
			else:
				return None
		except Exception as e:
			if verbose:
				print(e)
			return None
