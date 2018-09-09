import os
import json

class httpsystem():
	def __init__(self, system):
		self.system = system;
		#self.profile = profile;
		pass;
	def send(self, url, method="POST", data={}):
		if method=="POST":
			cmd = "curl \""+url+"\" -s -X "+method+" -d "+str(json.dumps(json.dumps(data)));
			print(cmd);
			response = os.popen(cmd).read();
		else:
			response = os.popen("curl \""+url+"\" -s -X "+method).read();
		print(response);
		return response;
	def get(self, url):
		url = "http://"+self.system.ip+"/"+url;
		return self.send(url, "GET");
	def post(self, url, data={}):
		url2 = url;
		url = "http://"+self.system.ip+"/"+url;
		r = self.send(url, "POST", data);
		if url2=="login":
			print("Attempting login on "+url+" with the following parameters: "+str(data));
			print("Result: "+r);
		return r;
	def secure(self, sub, data, profile=False):
		if not profile:
			profile = self.system.profile;
		url = "http://"+self.system.ip+"/secure_"+sub;
		data["hash"] = profile.hash;
		data["name"] = profile.username;
		return self.send(url, "POST", data);