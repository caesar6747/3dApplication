import time
import tkinter
from tkinter.ttk import Button
from OpenGL import GL
from pyopengltk import OpenGLFrame


def tombolKeluar(self):
	but=Button(self, text="keluar", command=self.quit)
	but.grid(column=1, row=0)
	return but

def tombol():
	variabelTombol = Button(self, text="exit")
