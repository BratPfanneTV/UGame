class game():
	def __init__(self, system):
		self.system = system;
		self.player = player(self);
	def go(self):
		system = self.system;
		self.world = world(self);
		tk = system.modules.tkinter;
		
		system.gui.reset();
		
		system.gui.tk.bind("w", system.modules.partial(self.world.move, -1,  0));
		system.gui.tk.bind("a", system.modules.partial(self.world.move,  0, -1));
		system.gui.tk.bind("s", system.modules.partial(self.world.move,  1,  0));
		system.gui.tk.bind("d", system.modules.partial(self.world.move,  0,  1));

		self.bar = tk.Canvas(system.gui.b, height=system.f.get_screensize(1), bg="lightgrey", width=system.f.get_screensize(0,33)).place(x=system.f.get_screensize(0,67), y=0);
		system.gui.tk.focus_set();
class player():
	def __init__(self, game):
		self.game = game;
		self.system = game.system;
		self.profile = game.system.profile;
class world():
	def __init__(self, game):
		self.game = game;
		self.system = game.system;
		init = self.system.modules.json.loads(self.system.http.secure("initiate"));
		self.game.player.world = init["world"];
		self.game.player.x = int(init["x"]);
		self.game.player.y = int(init["y"]);
		self.game.player.z = int(init["z"]);
	def getdata(self, mode):
		pass;
	def move(self, x, y, event):
		print("Attempting Movement");
		self.system.http.secure("movement", {"x":x,"y":y});
		self.game.player.x += x;
		self.game.player.y += y;