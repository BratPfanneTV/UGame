from tkinter import *
import tkinter as tk2
from system import trivial;
from system import menu;
from system import modules;
from system import http;
from system import game;

class create():
	def __init__(self, ip):
		self.ip = ip;
		self.f = trivial.trivial();
		self.modules = modules.modules();
		self.profile = profile(self);
		self.http = http.httpsystem(self);
		self.gui = gui(self);
		self.tkinter = tk2;
		self.game = game.game(self);
		self.modules.os.system("cls");
		print("UGame");
		print("");
		print("");
		print("#-#-#-#");
		print("");
		print("Initiating System ...");
		print("Server IP:        "+ip);
		
	def go(self):
		self.menu = menu.menu();
		self.gui.frame.after(0, self.menu.go);
		print("Executed.");
		self.gui.frame.mainloop();
class gui():
	def __init__(self, system):
		self.system = system;
		self.tk = Tk();
		self.tk.title("UGame");
		self.tk.call('wm', 'iconphoto', self.tk._w, PhotoImage(file=system.modules.os.path.join('graphic', 'icon.png')));
		self.tk.state('zoomed');
		self.tk.geometry(str(system.f.get_screensize(0))+"x"+str(system.f.get_screensize(1)));
		self.screen = screen(system);
		self.reset();
	def reset(self):
		if hasattr(self, "frame"):
			self.frame.destroy();
		self.frame = Frame(self.tk);
		self.frame.pack();
		self.b = Canvas(self.frame, bg="grey", width=self.screen.x, height=self.screen.y, highlightthickness=0);
		self.b.pack();
		
class screen():
	def __init__(self, system):
		self.system = system;
		self.x = system.f.get_screensize(0);
		self.y = system.f.get_screensize(1);
class profile():
	def __init__(self, system):
		self.hash="";
		self.username="";
		self.password="";
		self.system = system;
		self.success= False;
	def login(self, username, password):
		self.username = username;
		self.password = password;
		self.hash = self.system.modules.json.loads(self.system.http.post("login", {"username":username,"password":password}))["hash"];
	#	print(self.system.http.secure("hello", {}, self));
		if not self.system.http.secure("verify", {}, self)=="Online!":
			self.system.profile = profile(self.system);
		else:
			self.success=True;