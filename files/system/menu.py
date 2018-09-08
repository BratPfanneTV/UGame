class menu():
	def __init__(self):
		from system.globals import system;
		self.system = system;
	def go(self):
		system = self.system;
		tk = system.modules.tkinter;
		
		system.gui.reset();
		
		tk.Label(system.gui.b, font=system.f.fsize("32"), fg="red", text="UGame", anchor="center", width=6, bg="grey").place(y=75, x=system.f.get_screensize(0,48));