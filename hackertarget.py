from fetcher import Fetcher


class Fetch(Fetcher):
    def __init__(self):
        self.service_url = 'https://api.hackertarget.com/hostsearch/?q={}'
    
    def subdomains(self, domain, verbose):
        c = self.fetch(domain, verbose)
        try:
            subs = []
            for line in c.split('\n'):
                sub = line.split(',')[0]
                # Not sure why but the API seems to reject some URLs
                if sub == 'error check your search parameter':
                    pass
            if len(subs) > 0:
                return subs
            else:
                return None
        except Exception as e:
            print(f'[*] Error parsing json for {self.service_url}: {e}')
            return None
