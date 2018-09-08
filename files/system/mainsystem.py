from tkinter import *
import tkinter as tk2
from system import trivial;
from system import menu;
from system import modules;

class create():
	def __init__(self, ip):
		self.ip = ip;
		self.ipfull = "http://"+ip+"/uGate.php";
		self.f = trivial.trivial();
		self.gui = gui(self);
		self.modules = modules.modules();
		self.tkinter = tk2;
		self.modules.os.system("cls");
		print("");
		print("");
		print("");
		print("#-#-#-#");
		print("");
		print("Initiating System");
		print("Server IP:             "+ip);
		print("Server Address: "+self.ipfull);
		
	def go(self):
		self.menu = menu.menu();
		self.gui.frame.after(0, self.menu.go);
		self.gui.frame.mainloop();
class gui():
	def __init__(self, system):
		self.system = system;
		self.tk = Tk();
		self.tk.title("UGame");
		self.tk.call('wm', 'iconphoto', self.tk._w, PhotoImage(file='graphic\icon.png'));
		self.tk.state('zoomed');
		self.tk.geometry(str(system.f.get_screensize(0))+"x"+str(system.f.get_screensize(1)));
		self.screen = screen(system);
		self.reset();
	def reset(self):
		if hasattr(self, "frame"):
			self.frame.forget();
		self.frame = Frame(self.tk);
		self.frame.pack();
		self.b = Canvas(self.frame, bg="grey", width=self.screen.x, height=self.screen.y, highlightthickness=0);
		self.b.pack();
		
class screen():
	def __init__(self, system):
		self.system = system;
		self.x = system.f.get_screensize(0);
		self.y = system.f.get_screensize(1);