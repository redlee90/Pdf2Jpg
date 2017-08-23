#!/usr/bin/python3

import sys
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from PIL import Image
from io import StringIO
from time import sleep

file_path = sys.argv[1]
print ("pdf file path:", file_path)

multipart_data = MultipartEncoder(fields={'pdf': (file_path, open(file_path, 'rb'), 'application/pdf'),'resolution':'300'})

response1 = requests.post('https://pdf2jpg-pdf2jpg.p.mashape.com/convert_pdf_to_jpg.php', data=multipart_data, headers={'X-Mashape-Key': 'ScnSDyOw2HmshhpEJvHZ2U6upZKYp135iybjsnQMfr1AdDaCkt','Content-Type': multipart_data.content_type})
if response1.status_code==requests.codes.ok:
	image_id = response1.json()['id']
	image_key = response1.json()['key']
	print ("id:",image_id,"key:",image_key)
	
	sleep(2)
	response2 = requests.get('https://pdf2jpg-pdf2jpg.p.mashape.com/convert_pdf_to_jpg.php', params={'id':image_id, 'key':image_key}, headers={'X-Mashape-Key': 'ScnSDyOw2HmshhpEJvHZ2U6upZKYp135iybjsnQMfr1AdDaCkt', 'Accept': 'application/json'})
	if response2.status_code==requests.codes.ok:
		print('response2: ',response2.json())
		if response2.json()['status']=='done':
			image1 = Image.open(requests.get(response2.json()['pictures'][0], stream=True).raw)
			print('image size:', image1.size)
			image1.show()
			
	else:
		print ('response2 failed:', response2.status_code)	
else:
	print ('response1 failed:', response1.status_code)
		
		
		