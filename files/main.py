from system import globals;
from system import mainsystem;
from system import pyevent;
import time;
import sys;

arg = sys.argv;
arg.pop(0);

system = mainsystem.create(arg[1]);
globals.setsystem(system);
system.hook = pyevent.Hook(system);

system.modules.time = time;
system.modules.sys = sys;

system.go();

print("")
print("#-#-#-#")
print("")
print(".");
time.sleep(1.5);
print("..");
time.sleep(1.5);
print("...");
time.sleep(1.5);
print("Shutting down...")
print("")
print("")