#!/usr/bin/env python3

import os
import requests

path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"
external_ip = "http://"+your_ip_here+"/fruits/"

files = os.listdir(path)

for file in files:
  if file.endswith("txt"):
    with open(path + file, 'r', encoding="utf-8") as f:
      fruit_name = os.path.splitext(file)[0]
      lines = f.readlines()
      fruit_info = {
          "name": lines[0].strip('\n'),
          "weight": int(lines[1].strip('\n').split(" ")[0]),
          "description": lines[2].strip('\n'),
          "image_name": os.path.splitext(file)[0]+'.jpeg'
      }
      response = requests.post(external_ip, json=fruit_info)
      response.raise_for_status()
      print(response.request.url)
      print(response.status_code)