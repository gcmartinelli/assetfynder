from fetcher import Fetcher
import json


class Fetch(Fetcher):
    def __init__(self):
        self.service_url = 'https://certspotter.com/api/v0/certs?domain={}'
    
    def subdomains(self, domain, verbose):
        c = self.fetch(domain, verbose)
        try:
            json_ = json.loads(c)
            if json_:
                # Certspotter returns many results of sites that use the
                # same certificate but don't seem to have a strong link
                # with the searched domain. So I filter these out
                subs = []
                for block in json_:
                    for sub in block['dns_names']:
                        if domain in sub and sub not in subs:
                            subs.append(sub)
                return subs
            else:
                return None
        except Exception as e:
            if verbose:
                print(f'[*] Error parsing json for {self.service_url}: {e}')
                print(f'[*] Fetch returned: {c}')
            return None
