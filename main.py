#!/usr/bin/python3
import click
import requests
from multiprocessing import Pool, cpu_count
import threatcrowd, certspotter


# A list of fetcher objects
services = [['threatcrowd', threatcrowd.Fetch()],
			['certspotter', certspotter.Fetch()],]

def get_subs(domain, fetcher, fout=False):
	''' Receives a domain name and a fetcher object,
		returns a list of subdomains, or None.
	'''	
	try:
		subs = fetcher.subdomains(domain)
		# I preffer printing here so the user gets feedback ASAP
		if not fout:
			for sub in subs:
				print(sub)
		return subs
	except Exception as e:
		print(e)
		return None


@click.command()
@click.argument('domain')
@click.argument('out', type=click.File('a'), default='-',
				required=False)
def cli(domain, out):
	''' Returns possible subdomains for a 
		given URL. Can append results to an output filename
		if one is given; else prints to stdout. '''	
	if out.name != '<stdout>':
		fout = True
	else:
		fout = False

	print(f'> Collecting subdomains for {domain}')
	print('------------------------------------')
	with Pool(cpu_count()) as p:
		l = p.starmap_async(get_subs, [(domain, x[1], fout) for x in services]).get()
		subdomains = list(set([domain for sublist in l for domain in sublist]))
	if fout:
		for sub in subdomains:
			click.echo(sub, file=out)
