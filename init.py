#!/usr/bin/python3
import configparser


	
def APP_NAME():
	return "danneo-tools"

def APP_SHORT():
	return "dan-tools"
	
	
def finprint():
	print(__file__ + " finished successfully")

def main():
	WEBSITE = "DEFAULT"
	#c = config[]
	
	config = configparser.ConfigParser()
	config[WEBSITE] = {
		'url': 'http://example.com', 
		'user_cookie': '123userCRAZZZY',
		'user_id_max': 25000
	}

	with open(APP_SHORT() + ".ini", 'w') as configfile:
		config.write(configfile)	

	print("init.py done successfully")
	
# BEGIN
if __name__ == '__main__':
	main()