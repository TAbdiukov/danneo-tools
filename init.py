#!/usr/bin/python3
import configparser


	
def APP_NAME():
	return "danneo-tools"

def APP_SHORT():
	return "dan-tools"
	
def CFG():
	return APP_SHORT() + ".ini"
	
def finprint():
	print(__file__ + " finished successfully")

def DELIM():
	return "|"

def main():
	WEBSITE = "DEFAULT"
	
	config = configparser.ConfigParser()
	config.read(CFG())
	
	config[WEBSITE] = {
		'url': 'http://example.com', 
		'user_cookie': '123userCRAZZZY',
		'user_id_min': 1336,
		'user_id_max': 25000,
		'type': 666,
		'username_check_variable': 'usernamechk',
		'username_check_url': "/mod/user/check.php",
		'username_check_FreeOrTakenOrInvalid': "Username free|Username taken|Username invalid",
		'login_status_url': "/scriptzz/am_i_logged_on.php",
		'login_len_false': "[0, 666]",
		'login_len_true': "[1337, 22222]",
	}

	with open(CFG(), 'w') as configfile:
		config.write(configfile)	

	finprint()
	
# BEGIN
if __name__ == '__main__':
	main()