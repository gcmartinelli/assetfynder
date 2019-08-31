#!/usr/bin/python3
import click
import requests
from multiprocessing import Pool, cpu_count
import threatcrowd, certspotter, hackertarget, wayback


# A list of fetcher objects
services = [['threatcrowd', threatcrowd.Fetch()],
			['certspotter', certspotter.Fetch()],
			['wayback', wayback.Fetch()],
			['hackertarget', hackertarget.Fetch()],]


def get_subs(domain, fetcher, fout=False, verbose=False):
	''' Receives a domain name and a fetcher object,
		returns a list of subdomains, or None.
	'''	
	try:
		subs = fetcher.subdomains(domain, verbose)
		# I preffer printing here so the user gets feedback ASAP
		if not fout and subs:
			for sub in subs:
				print(sub)
		elif not subs:
			return []
		return subs
	except Exception as e:
		if verbose:
			print(e)
		return None


@click.command()
@click.option('--verbose', is_flag=True,
				 help='Output more information during execution')
@click.argument('domain')
@click.argument('out', type=click.File('a'), default='-',
				required=False)
def cli(verbose, domain, out):
	''' Returns possible subdomains for a 
		given URL. Can append results to an output filename
		if one is given; else prints to stdout. '''	
	if out.name != '<stdout>':
		fout = True
	else:
		fout = False
	if verbose:
		print(f'> Collecting subdomains for {domain}')
		print('------------------------------------')
	with Pool(cpu_count()) as p:
		l = p.starmap_async(get_subs, [(domain, x[1], fout, verbose) for x in services]).get()
		subdomains = list(set([domain for sublist in l for domain in sublist]))
	if fout:
		for sub in subdomains:
			click.echo(sub, file=out)
