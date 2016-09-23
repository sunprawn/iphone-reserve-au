# The MIT License (MIT)
# Copyright (c) 2014 Karthikeya Udupa KM
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests
import time

# change this to alter the monitoring stores.
# only check Chadstone, Doncaster, Fountain Gate
pref_stores = ['R180', 'R342', 'R530']
	
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
def decode(k):

	if(k=="MN912X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Rose - 32GB"
	elif(k=="MN902X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Gold - 32GB"
	elif(k=="MN8Y2X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Silver - 32GB"
	elif(k=="MN8X2X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Black - 32GB"


	elif(k=="MN952X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Rose - 128GB"
	elif(k=="MN942X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Gold - 128GB"
	elif(k=="MN932X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Silver - 128GB"
	elif(k=="MN922X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Black - 128GB"
	elif(k=="MN962X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Jet - 128GB"

	elif(k=="MN9A2X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Rose - 256GB"
	elif(k=="MN992X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Gold - 256GB"
	elif(k=="MN982X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Silver - 256GB"
	elif(k=="MN972X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Black - 256GB"
	elif(k=="MN9C2X/A"):
		return bcolors.FAIL + "Apple iPhone 7 Jet - 256GB"

	elif(k=="MNQQ2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Rose - 32GB"
	elif(k=="MNQP2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Gold - 32GB"
	elif(k=="MNQN2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Silver - 32GB"
	elif(k=="MNQM2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Black - 32GB"


	elif(k=="MN4U2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Rose - 128GB"
	elif(k=="MN4Q2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Gold - 128GB"
	elif(k=="MN4P2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Silver - 128GB"
	elif(k=="MN4M2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Black - 128GB"
	elif(k=="MN4V2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Jet - 128GB"

	elif(k=="MN502X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Rose - 256GB"
	elif(k=="MN4Y2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Gold - 256GB"
	elif(k=="MN4X2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Silver - 256GB"
	elif(k=="MN4W2X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Black - 256GB"
	elif(k=="MN512X/A"):
		return bcolors.OKGREEN + "Apple iPhone 7 Plus Jet - 256GB"


	else:
		return bcolors.FAIL + k;

    
storeurl = "https://reserve.cdn-apple.com/AU/en_AU/reserve/iPhone/stores.json"
availurl = "https://reserve.cdn-apple.com/AU/en_AU/reserve/iPhone/availability.json"


try:
	store_json = requests.get(storeurl).json()
	avail_json = requests.get(availurl).json()

	if 'stores' in store_json:
		for key in store_json['stores']:
			if key['storeNumber'] not in pref_stores:
				continue
			items =  avail_json[key['storeNumber']]
			print bcolors.OKGREEN + str(key['storeName'])
			for k in items:
				if items[k]=="ALL":
					iphoneStr = decode(k)

					# only show plus
					if "Plus" in iphoneStr:
						print bcolors.OKGREEN + "	-	" + iphoneStr

		print bcolors.OKBLUE + "Updated: "+ time.strftime('%d, %b %Y %H:%M:%S')  + "\n"


	else:
		print bcolors.FAIL + time.strftime('%d, %b %Y %H:%M:%S') + " - Data Unavailable."
except ValueError:
	print bcolors.FAIL + time.strftime('%d, %b %Y %H:%M:%S')  + " - Server Unavailable."
