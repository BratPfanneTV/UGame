class menu():
	def __init__(self):
		from system.globals import system;
		self.system = system;
	def go(self):
		system = self.system;
		tk = system.modules.tkinter;
		
		system.gui.reset();
		
		tk.Label(system.gui.b, font=system.f.fsize("32"), fg="red", text="UGame", anchor="center", width=6, bg="white").place(y=75, x=system.f.get_screensize(0,46));
		tk.Button(system.gui.b, text="Start", font=system.f.fsize("20"),bg="green", fg="white", bd=8,command=self.tryboot).place(anchor=tk.CENTER, y=system.f.get_screensize(0,12), x=system.f.get_screensize(0,50), width=system.f.get_screensize(0,25), height=system.f.get_screensize(1,10));
		tk.Button(system.gui.b, text="Login", font=system.f.fsize("20"),bg="red", fg="white", bd=8,command=self.login).place(anchor=tk.CENTER, y=system.f.get_screensize(0,18), x=system.f.get_screensize(0,50), width=system.f.get_screensize(0,25), height=system.f.get_screensize(1,10));
		
		bg="red";
		fg="red";
		text="red";
		
		L = tk.Label(system.gui.b, text=text, bg=bg, fg=fg, font=system.f.fsize("16"));
		self.connectfunc = self.system.modules.partial(self.connect, L);
		self.connectfunc.__name__ = "connect";
		L.after(0, self.connectfunc);
	def connect(self, L):
		system = self.system;
		tk = system.modules.tkinter;
	
		text = system.http.secure("verify", {}, system.profile);
		text2 = system.http.secure("hello", {}, system.profile);
		if not text:
			bg = "red";
			fg = "white";
			text2 = "Server not found";
		elif text=="Online!":
			bg = "green";
			fg = "white";
		else:
			bg = "Gold2";
			fg = "red";
		L.config(bg=bg,fg=fg,text=text2);
		L.place(y=system.f.get_screensize(1,94), x=system.f.get_screensize(0,0), anchor=tk.SW);
		if L.winfo_exists():
			L.after(10000, self.connectfunc);
	def tryboot(self):
		if not hasattr(self.system, "profile") or not self.system.profile.success:
			self.login("You are missing a valid account. Please enter Details.");
		else:
			self.system.game.go();
	def login(self, missing=False):
		system = self.system;
		tk = system.modules.tkinter;
		partial = system.modules.partial;
		
		system.gui.reset();
		
		tk.Label(system.gui.b, font=system.f.fsize("32"), fg="red", text="UGame", anchor="center", width=6, bg="white").place(y=75, x=system.f.get_screensize(0,46));
		if not missing:
			tk.Label(system.gui.b, font=system.f.fsize("16"), fg="black", text="Enter Details:", anchor="center", bg="white").place(y=150, x=system.f.get_screensize(0,46));
		else:
			tk.Label(system.gui.b, font=system.f.fsize("16"), fg="red", text=missing, anchor="center", bg="white").place(y=150, x=system.f.get_screensize(0,38));
		e1 = tk.Entry(system.gui.b);
		e1.place(anchor=tk.CENTER, y=system.f.get_screensize(0,12), x=system.f.get_screensize(0,50), width=system.f.get_screensize(0,25), height=system.f.get_screensize(1,2));
		e2 = tk.Entry(system.gui.b, show="*");
		e2.place(anchor=tk.CENTER, y=system.f.get_screensize(0,13), x=system.f.get_screensize(0,50), width=system.f.get_screensize(0,25), height=system.f.get_screensize(1,2));
		def la():
			self.loginattempt(e1.get(), e2.get());
		tk.Button(system.gui.b, text="Login", font=system.f.fsize("20"),bg="red", fg="white", bd=8,command=la).place(anchor=tk.CENTER, y=system.f.get_screensize(0,18), x=system.f.get_screensize(0,50), width=system.f.get_screensize(0,25), height=system.f.get_screensize(1,10));
	def loginattempt(self, e1, e2):
		self.system.profile.login(e1, e2);
		if self.system.profile.success:
			self.go();
		else: 
			self.login("Login Failed.");