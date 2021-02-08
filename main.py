import time

from LayerUtama.open import *
from LayerUtama.menubars import *
from tombol.tombolUtama import tombolKeluar
from tkinter import *


width = 900
height = 700

wopen = (width*70)/100
hopen = (height*90)/100
edit = 0

if __name__ == '__main__': 

	jendelaUtama = tkinter.Tk()
	jendelaUtama.geometry(f"{width}x{height}")

	frameUtama = Frame(jendelaUtama, bg='#777777')
	frameUtama.pack(fill=BOTH, expand=1)

	grap = open(frameUtama)
	grap.pack(side=LEFT, fill=BOTH, expand=1)

	do = dock(frameUtama)

	frm = footer(do)

	app = menunya(jendelaUtama)


	jendelaUtama.mainloop()
