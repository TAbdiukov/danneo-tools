#!/usr/bin/python3

# UNFINISHED
"""UNFINISHED"""

# time watch and sleep purposes
import time

# lazy args
import sys

# for requests stuff
from fake_useragent import UserAgent
import requests

# for config manipulation
import configparser
import ast
	
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
		print("Tries logging in via cookies")
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
		authed_url = config[web]["login_status_url"]
		headers = config[web]["headers"]
		
		login_len_false = config[web]["login_len_false"]
		login_len_true = config[web]["login_len_true"]
		interval = config[web]["login_interval"]
		cookie_base = "{'" + config[web]["user_cookie"] + "': '"
		
		assert(len(url))
		assert(len(authed_url))
		assert(len(login_len_false))
		assert(len(login_len_true))
		
		# process inputs  complexely 
		## url
		work_url = url + authed_url
		print(work_url)
		
		is_logged_on_range_false = ast.literal_eval(login_len_false)
		is_logged_on_range_true = ast.literal_eval(login_len_true)
		assert(len(is_logged_on_range_false) == 2)
		assert(len(is_logged_on_range_true) == 2)
		
		pre_header = ast.literal_eval(headers)		
		headers = merge_two_dicts({'User-Agent': ua.random}, pre_header)
				
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
		
		id_min = config[web]["user_id_min"]
		id_max = config[web]["user_id_max"]
		id_total = (id_max - id_min) + 1
		assert(id_total > 0)
		
		work = id_total
		assert(username_count > 0)
		
		bar = ProgressBar(work, max_width=40)		
		
		## Final out
		whatToLog = __file__ + " is starting!\n" \
		"[*] config["+web+"] = "+str(config[web])+"\n" \
		"[*] username_count = "+str(username_count)+"\n" \
		"The script will start in ~5s" 
		flog.write(whatToLog+"\n")
		print(whatToLog)
		time.sleep(5)


		# work
		# >>> range(6)
		# [0, 1, 2,3,4,5]
		for i in range(id_work):
			k = i + id_min
			for uname in content
				"""fgood.write(uname + "\n")
				whatToLog = "[I] "+ uname
				flog.write(whatToLog+"\n")
				print(whatToLog)
				"""
				time.sleep(interval/1000)


	finprint()
	
	
def gen_cook_string(id, username):
	C34 = chr(34)

	# 0/3
	i0_prefix = "a:3:{i:0;s:"
	i0_string = str(id)
	i0_slen = len(i0_string)
	
	ret = i0_prefix + i0_slen + ":" + C34 + i0_string + C34 + ";"
	
	i1_prefix = "i:1;s:"
	i1_string = "password"
	i1_slen = len(i0_string)
	
	
	

def cook_string_to_cookie(s):

# BEGIN
if __name__ == '__main__':
	main()