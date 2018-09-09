class game():
	def __init__(self, system):
		self.system = system;
		self.player = player(self);
		self.world = world(self);
	def go(self):
		system = self.system;
		tk = system.modules.tkinter;
		
		system.gui.reset();

		self.bar = tk.Canvas(system.gui.b, height=system.f.get_screensize(1), bg="lightgrey", width=system.f.get_screensize(0,33)).place(x=system.f.get_screensize(0,67), y=0);
class player():
	def __init__(self, game):
		self.game = game;
		self.system = game.system;
class world():
	def __init__(self, game):
		self.game = game;
		self.system = game.system;
		init = self.system.http.secure("initiate");