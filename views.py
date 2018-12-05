from django.shortcuts import render
    
from django.http import HttpResponse

from .models import Greeting

import os
import json
import subprocess
import random
import requests
import string

def getFilename(s):
  new_file_name = '' 
  if all(x in s for x in ['/', '.']):
    return s.split('/')[-1]
  else:
    return 'raw.bin'

# Create your views here.
def index(request):
  # Get URL to download from
  url = request.GET.get('url')

  # Generate
  uid = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
  enc_name = uid + '.zip'

  # Download raw file
  raw_name = getFilename(url)
  r = requests.get(url, allow_redirects=True)
  f = open(raw_name, 'wb')
  f.write(r.content)
  f.close()

  # Encrypt raw file
  subprocess.Popen(['zip', '-P', '1234', enc_name, raw_name]).wait()

  # Delete raw file
  subprocess.Popen(['rm', raw_name]).wait()

  # Read encrypted file
  f = open(enc_name,'rb')
  size = os.path.getsize(enc_name)
  data = f.read()
  f.close()
  # Delete encrypted file after reading contents into memory
  subprocess.Popen(['rm', enc_name]).wait()

  # Return encrypted file
  response = HttpResponse(content=data, 
    content_type='application/octet-stream')
  response['Content-Disposition'] = 'filename="{}"'.format(enc_name)
  response['Content-Length'] = str(size)
  return response

