class game():
	def __init__(self, system):
		self.system = system;
		self.player = player(self);
	def go(self):
		system = self.system;
		self.world = world(self);
		tk = system.modules.tkinter;
		
		system.gui.reset();
		
		system.gui.tk.bind("a", system.modules.partial(self.world.move,   -1, 0));
		system.gui.tk.bind("w", system.modules.partial(self.world.move,   0, -1));
		system.gui.tk.bind("d", system.modules.partial(self.world.move,  1, 0));
		system.gui.tk.bind("s", system.modules.partial(self.world.move,   0,1));
	#	system.gui.tk.bind("<F5>", system.modules.partial(self.world.build,   "refresh_entities"));

		self.bar = tk.Canvas(system.gui.b, height=system.f.get_screensize(1), bg="lightgrey", width=system.f.get_screensize(0,33)).place(x=system.f.get_screensize(0,67), y=0);
		self.bg = tk.Canvas(system.gui.b, height=system.f.get_screensize(1), bg="green", width=system.f.get_screensize(1)).place(x=0, y=0);
		system.gui.tk.focus_set();
		self.world.build("refresh_entities");
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
		self.entities = {};
		self.cooldown = 0;
	def build(self, mode):
		tk = self.system.modules.tkinter;
		if mode == "refresh_entities":
			print("Requesting Entities");
			ex=True;
			try:
				self.raw_data = self.system.modules.json.loads(self.system.http.secure("request_entities"));
			except:
				ex=False;
			if ex:
				if hasattr(self, "entities"):
					for name, entity in self.entities.items():
						if isinstance(entity, Entity) and not entity.name in self.raw_data:
							entity.d.destroy();
							entity.nl.destroy();
							del self.entities[name];
				for name, data in self.raw_data.items():
					if not name in self.entities:
						e = Entity(self.game, data["x"], data["y"], name);
						if name == self.system.profile.username:
							self.system.entity = e;
						self.entities[name] = e;
						e.d = tk.Label(self.game.bg, image=tk.PhotoImage(file=self.system.modules.os.path.join('graphic','world',data["image"]+".png")));
						e.nl = tk.Label(self.game.bg, text=name, font=self.system.f.fsize("5"), bg="green", fg="white");
						e.d.place(x=data["x"],y=data["y"]);
						e.nl.place(x=data["x"],y=data["y"]-20);
					else:
						e = self.entities[name];
					e.d.place_configure(x=data["x"],y=data["y"]);
					e.nl.place_configure(x=data["x"],y=data["y"]-20);
			func = self.system.modules.partial(self.build, "refresh_entities");
			func.__name__ = "build";
			
			self.system.gui.tk.after(80, func);
	def move(self, x, y, event):
		if (int(round(self.system.modules.time.time() * 1000)) - self.cooldown) > 250:
			self.cooldown = int(round(self.system.modules.time.time() * 1000));
			print("Attempting Movement");
			try:
				speed = int(self.system.http.secure("movement", {"x":x,"y":y}));
			except ValueError:
				speed = 0;
			self.game.player.x += x*speed;
			self.game.player.y += y*speed;
			if hasattr(self, "entities"):
				for name, entity in self.entities.items():
					if not entity.name == self.system.entity.name:
						entity.x -= x*speed;
						entity.y -= y*speed;
						entity.d.place_configure(x=entity.x,y=entity.y);
						entity.nl.place_configure(x=entity.x,y=entity.y-20);
		
class Entity():
	def __init__(self, game, x, y, name):
		self.game = game;
		self.system = game.system;
		self.x = x;
		self.y = y;
		self.name = name;