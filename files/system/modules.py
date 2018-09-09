import tkinter as tk;
import os;
from functools import partial;
import json;

class modules():
	def __init__(self):
		self.tkinter = tk;
		self.os = os;
		self.partial = partial;
		self.json = json;
		# time
		# sys