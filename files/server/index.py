import random
import os
import hashlib
import json;

def login(data):
	if "username" in data and "password" in data:
		try:
			accounts = json.loads(open("accounts.json", "r").read());
		except FileNotFoundError:
			print(os.getcwd());
		if not data["username"] in accounts:
			accounts[data["username"]]=hashlib.md5(str(data["password"]).encode('utf-8')).hexdigest();
			open("accounts.json", "w+").write(json.dumps(accounts));
		if accounts[data["username"]]==hashlib.md5(str(data["password"]).encode('utf-8')).hexdigest():
			os.chdir("axs");
			string = data["username"]+data["password"]+str(random.randint(1,1000000));
			string = hashlib.md5(str(string).encode('utf-8')).hexdigest();
			open(string+".txt", "w+").write(data["username"]);
			os.chdir("..");
			return '{"success":true,"hash":"'+string+'"}';
		else:
			return '{"success":false}';	
	else:
		return '{"success":false}';
def favicon(data):
	return "Nope";
def secure_verify(data):
	return "Online!";
def secure_hello(data):
	return "Online as "+data["name"]+"!";
def secure_initiate(data):
	import config
	config = config.main();
	return '{"name":"'+config.startworld+'", "x":"'+config.startX+'", "z":"'+config.startY+'"}';