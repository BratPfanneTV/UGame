from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse as urlparse
import json
import os
import time

if not os.path.exists('axs'):
	os.mkdir("axs");
if not os.path.exists('config.py'):
	r = os.popen("curl http://213.202.229.164/ugame-server/config.py -s");
	open("config.py", "w+").write(r.read());
r = os.popen("curl http://213.202.229.164/ugame-server/index.py -s");
open("index.py", "w+").write(r.read());
if not os.path.exists('serverdata.accounts.json'):
	open("serverdata.accounts.json", "w+").write("{}");
if not os.path.exists('serverdata.posdata.json'):
	open("serverdata.posdata.json", "w+").write("{}");

class S(BaseHTTPRequestHandler):
	class user():
		def __init__(self, name, hash):
			self.name = name;
			self.hash = hash;
		def terminate(self):
			pass;
	def _set_headers(self, res=200, type="text/html", loc=False):
		self.send_response(res)
		if loc:
			self.send_header('Location', loc)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		if self.client_address[0]=="127.0.0.1":
			self.do_POST();
		else:
			self._set_headers(200)
			self.wfile.write(b"<tt><h1>UGame-Server.</h1></tt><hr>Incorrect Method.")

	def do_HEAD(self):
		self._set_headers()
		
	def do_POST(self):
		if self.headers.get('Content-Length'):
			data = json.loads(self.rfile.read(int(self.headers.get('Content-Length'))));
		else:
			data = {};
		datas = json.dumps(data);
		if self.path == "/":
			self._set_headers(200, "text/html", "index");
			self.path = "/index";
		else:
			self._set_headers(200, "text/html");
		path = self.path[1:];
		print(path);
		import index as serverfile;
		auth=True;
		if path[:6]=="secure":
			auth=False;
			os.chdir("axs");
			if "hash" in data:
				if os.path.exists(data["hash"]+".txt") and time.time()-os.path.getmtime(data["hash"]+".txt")<43200:
					auth=True;
					print("Secure access from account "+data["name"]+" verified.");
					data["user"]=self.user(data["name"],data["hash"]);
				#	del data["name"];
			else:
				if self.client_address[0]=="127.0.0.1":
					auth=True;
					data["user"]=self.user("admin","fake");
					data["name"]="admin";
			os.chdir("..");
			if auth:
				psfr = open("serverdata.posdata.json", "r" );
				posdata = json.loads(psfr.read());
				psfr.close();
				if data["name"] in posdata:
					data["user"].x = posdata[data["name"]]["x"];
					data["user"].y = posdata[data["name"]]["y"];
					data["user"].z = posdata[data["name"]]["z"];
					data["user"].world = posdata[data["name"]]["world"];
		if auth:
		#	try:
			exec("global response; response = serverfile."+path+"(data);");
		#	except AttributeError:	
		#		exec('global response; response = "Method not found.";');
		else:
			exec('global response; response = "Authentification Failed.";');
		print("Sending response: "+response);
		self.wfile.write(bytes(response, 'utf8'));
		
			
def run(server_class=HTTPServer, handler_class=S, port=1103):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print('Starting httpd...');
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()