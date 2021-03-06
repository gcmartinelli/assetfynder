# assetfynder

Find domains and subdomains potentially related to a given domain.

Inspired by [assetfinder](http://github.com/tomnomnom/assetfinder)

## Installation

`pip install .`

## Usage
```
Usage: assetfynder [OPTIONS] DOMAIN [OUT]

  Returns possible subdomains for a  given URL. Can append results to an
  output filename if one is given; else prints to stdout.

Options:
  --verbose    Output more information during execution
  --nowayback  Do not incorporate wayback machine results
  --help       Show this message and exit.

```

`assetfynder example.com` prints to the terminal all discovered subdomains for example.com

`assetfynder example.com subdomains.txt` saves to subdomains.txt all discovered subdomains for example.com
