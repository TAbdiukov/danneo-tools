#!/usr/bin/python3

try:
    import requests
except ModuleNotFoundError:
	print("Please install prerequisite,")
	print("```")
	print("pip install requests")
	print("```")
	exit()

import re
import argparse
from pathlib import Path


from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Description: The script mass-checks RAW domain names for Danneo
# Input: RAW domain names (without protocol) in an input file
# Output: Results in a separate file

# Define headers
headers = {
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://www.google.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9",
    "Priority": "u=0, i",
    "Connection": "keep-alive"
}


# Create the parser
parser = argparse.ArgumentParser(description='Process some domain names.')

# Add the arguments
parser.add_argument('URLsFile', metavar='URLsFile', type=str, help='The file with domain names')

# Parse the arguments
args = parser.parse_args()

# Open the file with domain names
with open(args.URLsFile, 'r') as f:
    urls_in = f.read().splitlines()
    
urls = []
for u in urls_in:
    if(u):
        urls.append("http://"+u)
        urls.append("https://"+u)
        urls.append("http://www."+u)
        urls.append("https://www."+u)

# Supress warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

results = []
with open(Path(args.URLsFile).stem+'-output.txt', 'a') as f:
    for url in urls:
        try:
            # Error-correction
            if("http" not in url):
                url = "https://"+url
            
            # Send a GET request
            response = requests.get(url, headers=headers, verify=False)
            # If the response is valid
            if response.status_code == 200:
                soup = str(response.headers) + response.text
                matches = re.search(r'(Danneo.{,20}?[\.|\d])[^\w\.]', soup)
                if matches:
                    result = f'URL: {url}, Matches: {matches.group(1)}'
                else:
                    result = f'URL: {url}, No matches found'
            else:
                result = f'URL: {url}, Invalid response'
        except requests.exceptions.SSLError as e:
            result = f'URL: {url}, SSLError'
        except requests.exceptions.ConnectionError as e:
            result = f'URL: {url}, ConnectionError'
        except Exception as e:
            result = f'URL: {url}, Error: {str(e)}'
        finally:
            f.write(result+"\n")
            f.flush()
            print(result)

f.close()
