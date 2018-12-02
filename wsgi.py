# Assuming pythonanywhere.com as your hosting server,
# rename and place this script in your hosted /var/www

import os
import json
import requests
import subprocess
from cgi import parse_qs

raw_name = 'raw.bin'
encrypted_name = 'enc.zip'

# FROM  : {'url': ['https://github.com']}
# TO    : https://github.com
def getUrlFromGET(s):
    s = str(s)
    s = s.replace("'",'"')
    j = json.loads(s)
    url = j['url']
    url = str(url[0])
    return url

def application(environ, start_response):
    # Get URL to download from GET request
    url = getUrlFromGET(parse_qs(environ['QUERY_STRING']))

    # Download file
    r = requests.get(url, allow_redirects=True)
    f = open(raw_name, 'wb')
    f.write(r.content)
    f.close()

    # Encrypt file
    subprocess.Popen(['zip', '-P', '1234', encrypted_name, raw_name])

    # Read file
    f = open(encrypted_name,'rb')
    size = os.path.getsize(encrypted_name)

    # Set up response header information
    if environ.get('PATH_INFO') == '/':
        status = '200 OK'
    else:
        status = '404 NOT FOUND'
    response_headers = [
        ('Content-Disposition', 'filename=' + encrypted_name),
        ('Content-Type', 'application/octet-stream'),
        ('Content-Length', str(size))
        ]
    start_response(status, response_headers)

    # Return file content
    yield f.read()


