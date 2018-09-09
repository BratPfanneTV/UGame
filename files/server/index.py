import random
import os
import hashlib
import json;

def login(data):
	if "username" in data and "password" in data:
		try:
			afr=open("serverdata.accounts.json", "r" );
			accounts = json.loads(afr.read());
			afr.close();
		except FileNotFoundError:
			print(os.getcwd());
		if not data["username"] in accounts:
			accounts[data["username"]]=hashlib.md5(str(data["password"]).encode('utf-8')).hexdigest();
			afw=open("serverdata.accounts.json", "w+");
			afw.write(json.dumps(accounts));
			afw.close();
		if accounts[data["username"]]==hashlib.md5(str(data["password"]).encode('utf-8')).hexdigest():
			os.chdir("axs");
			string = data["username"]+data["password"]+str(random.randint(1,1000000));
			string = hashlib.md5(str(string).encode('utf-8')).hexdigest();
			hsw = open(string+".txt", "w+");
			hsw.write(data["username"]);
			hsw.close();
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
	psfr = open("serverdata.posdata.json", "r" );
	posdata = json.loads(psfr.read());
	psfr.close();
	if not data["name"] in posdata:
		posdata[data["name"]] = {"world":config.startworld,"x":int(config.startX)*16,"y":int(config.startY)*16,"z":int(config.startZ),"image":"player-test"};
		psfw = open("serverdata.posdata.json", "w+");
		psfw.write(json.dumps(posdata));
		psfw.close();
	return json.dumps(posdata[data["name"]]);
def secure_movement(data):
	import config
	config = config.security();
	psfr = open("serverdata.posdata.json", "r" );
	posdata = json.loads(psfr.read());
	psfr.close();
	userspeed = config.speed;
	if data["x"] in list(range(-1,2)):
		posdata[data["name"]]["x"]+=data["x"]*userspeed;
	if data["y"] in list(range(-1,2)):
		posdata[data["name"]]["y"]+=data["y"]*userspeed;
	posdata[data["name"]]["ax"]=round(posdata[data["name"]]["x"]/16);
	posdata[data["name"]]["ay"]=round(posdata[data["name"]]["y"]/16);
	posdata[data["name"]]["apx"]=round(posdata[data["name"]]["x"]);
	posdata[data["name"]]["apy"]=round(posdata[data["name"]]["y"]);
	psfw = open("serverdata.posdata.json", "w+");
	psfw.write(json.dumps(posdata));
	psfw.close();
	return '';
def secure_posdata_file(data):
	psfr = open("serverdata.posdata.json", "r");
	c = psfr.read();
	psfr.close();
	return c;
def secure_accounts_file(data):
	psfr = open("serverdata.accounts.json", "r");
	c = psfr.read();
	psfr.close();
	return c;
def secure_request_entities(data):
	psfr = open("serverdata.posdata.json", "r");
	players = json.loads(psfr.read());
	result = {};
	psfr.close();
	for name, values in players.items():
		if values["world"]==data["user"].world:
			if values["x"] in list(range(data["user"].x-480,data["user"].x+480)):
				if values["y"] in list(range(data["user"].y-480,data["user"].y+480)):
					x = values["x"]+480-data["user"].x;
					y = values["y"]+480-data["user"].y;
					result[name]={"x":x,"y":y};
	return json.dumps(result);