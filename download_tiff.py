#!/usr/bin/env python3

'''
This script downloads tiff files from
a geoserver web coverage service.
'''

import argparse
import shutil
import requests

def download_tiff_from_url(base_url, coverage_id, destination_file):
    if not base_url.endswith('?'):
        base_url += '?'
    url = base_url + \
            'service=WCS&' + \
            'version=2.0.0&' + \
            'request=GetCoverage&' + \
            'format=image/tiff&' + \
            'CoverageId={0}'.format(coverage_id)
    res = requests.get(url, verify=False, stream=True)

    if res.status_code == 200:
        with open(destination_file, 'wb') as f:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, f)
    else:
        raise Exception('Invalid status code', res.status_code)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Downloads a tiff from Web Coverage Service')
    argparser.add_argument('base_url', help='The base url / server for downloading the file')
    argparser.add_argument('coverage_id', help='Identifier for the file to download')
    argparser.add_argument('--destination_file', help='Output file name', default='output.tiff')
    args = argparser.parse_args()

    base_url = args.base_url
    coverage_id = args.coverage_id
    destination_file = args.destination_file


    download_tiff_from_url(base_url, coverage_id, destination_file)
