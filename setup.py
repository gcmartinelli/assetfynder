from setuptools import setup, find_packages

setup(
    name = 'assetfynder',
    version = '0.1',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'Click',
        'requests',
        ],
        py_modules = [
                'main',
                'threatcrowd',
                'hackertarget',
                'certspotter',
                'fetcher',
                'wayback',
                ],
    entry_points = {
            'console_scripts': [
                'assetfynder = main:cli'
                        ]
                },
    )
