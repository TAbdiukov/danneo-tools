#!/usr/bin/python3
# time watch and sleep purposes
import time

# lazy args
import sys

# for requests stuff
from fake_useragent import UserAgent
import requests

# for config manipulation
import configparser
import ast # https://stackoverflow.com/a/56084659/12258312
	
# for visuals
from etaprogress.progress import ProgressBar
	
def APP_NAME():
	return "danneo-tools"

def APP_SHORT():
	return "dan-tools"
	
def DELIM():
	return "|"
	
def CFG():
	return APP_SHORT() + ".ini"

def finprint():
	print(__file__ + " finished successfully")

# https://stackoverflow.com/a/26853961/12258312
def merge_two_dicts(x, y):
	z = x.copy()   # start with x's keys and values
	z.update(y)    # modifies z with y's keys and values & returns None
	return z

def fti_digest(pfti, input):
	return pfti.index(input)
	
def getUnixTime():
	return toHexCustom(int(time.time()))
	
def toHexCustom(dec): 
	return str(hex(dec).split('x')[-1])	


def main():
	
	config = configparser.ConfigParser()
	config.read(CFG())
	
	print("[P] Initialising User-Agent, please wait (1/3)")
	ua = UserAgent()
	print("[P] Initialising User-Agent, please wait (2/3)")
	#ua.update()
	print("[P] Initialising User-Agent, please wait (3/3)")
	print("")
	
	if len(sys.argv) != 3: #-1
		print("USAGE: python3 "+__file__+" <webconfig> <secfile>")
		print("<webconfig> - I.e. name of website to attack in .INI")
		print("<secfile> - Aka dictionary to try out. Line-delimited")
		print("For example: python3 "+__file__+".py pastebing.ns.agency users.txt")
	else:
		# rudimental inputs
		web  = str(sys.argv[1])
		fdict = str(sys.argv[2])
		
		assert(config != {})
		assert(config[web] != {})
		
		# config inputs
		url = config[web]["url"]
		check_url = config[web]["username_check_url"]
		freeortakenorinvalid = config[web]["username_check_freeortakenorinvalid"]
		headers = config[web]["headers"]
		username_check_variable = config[web]["username_check_variable"]
		
		assert(len(url))
		assert(len(check_url))
		assert(len(freeortakenorinvalid))
		assert(len(username_check_variable))
		
		# process inputs  complexely 
		## url
		work_url = url + check_url
		print(work_url)
		
		pre_header = ast.literal_eval(headers)		
		headers = merge_two_dicts({'User-Agent': ua.random}, pre_header)
		
		processed_fti = freeortakenorinvalid.split(DELIM())
		data_base = "{'"+username_check_variable+"': '"
		
		# files
		## MISC
		utime = getUnixTime()
		
		
		fname_bad  = APP_SHORT() + "_" + utime + "_free" + ".text"
		fname_good = APP_SHORT() + "_" + utime + "_tken" + ".text"
		fname_log  = APP_SHORT() + "_" + utime + "_log" + ".text"
		
		fbad  = open(fname_bad,  "w+", encoding="utf-8")
		fgood = open(fname_good, "w+", encoding="utf-8")
		flog = open(fname_log, "w+", encoding="utf-8")
		
	
		with open(fdict, encoding="utf-8") as f:
			content = f.read().splitlines()
			
		## Misc
		username_count = len(content)
		work = username_count
		assert(username_count > 0)
		
		bar = ProgressBar(work, max_width=40)		
		
		## Final out
		whatToLog = __file__ + " is starting!\n" \
		"[*] config["+web+"] = "+str(config[web])+"\n" \
		"[*] headers = "+str(headers)+"\n" \
		"The script will start in ~5s" 
		flog.write(whatToLog+"\n")
		print(whatToLog)
		time.sleep(5)

		
		# work
		i = 0
		for uname in content:
			i=i+1
			data = ast.literal_eval(data_base + uname + "'}")
			resp = requests.post(work_url, headers=headers, data=data)
			buf = fti_digest(processed_fti, resp.text)
			if(buf == 0): # login FREE
				fbad.write(uname + "\n")
				whatToLog = "[F] "+ uname
				flog.write(whatToLog+"\n")
				print(whatToLog)
			elif (buf == 1): # login TAKEN
				fgood.write(uname + "\n")
				whatToLog = "[T] "+ uname
				flog.write(whatToLog+"\n")
				print(whatToLog)
			elif (buf == 2): # login INVALID
				fgood.write(uname + "\n")
				whatToLog = "[I] "+ uname
				flog.write(whatToLog+"\n")
				print(whatToLog)
				
			bar.numerator = i
			print(str(bar).strip())


	finprint()
	
# BEGIN
if __name__ == '__main__':
	main()