from LayerUtama.atur import *
from tkinter import *
from LayerUtama.open import *




class menunya(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Ditor")
		self.menus()
		ima = PhotoImage(file="img/monitor.png")
		self.parent.iconphoto(False, ima)

	def menus(self):
		
		menuBar = menu(self.parent)
		menuUtama = menu(menuBar)
		menuUtama.config(tearoff=0)

		menuDua = menu(menuBar)
		menuDua.config(tearoff=0)

		menuUtama.add_command(label="Window-1")
		menuUtama.add_command(label="keluar", command= self.quit)
		menuUtama.add_command(label="OpenGL", command=self.bukaJendela)

		menuDua.add_command(label="OpenGL", command=self.bukaJendela)
		menuDua.add_command(label="OpenGL_2", command=self.bukaJendela1)

		menuBar.add_cascade(label="Menu", menu=menuUtama)
		menuBar.add_cascade(label="Contoh", menu=menuDua)

		self.parent.config(menu=menuBar)

	def tombol(self):
		variabelTombol = Button(self, text="exit", command = self.quit)
		variabelTombol.grid(column=1, row=1)

	def cek (self):
		c = Checkbutton(self, text="hisahd")
		c.place(x=50, y=20)

	def bukaJendela(self, event=None):
		app = Window1(self, "OpenGL")

	def bukaJendela1(self):
		app = Window2(self, "OpenGL_2")
		app.mainloop()


def wOpen(mass):
	mass = Frame(mass, width=100, height=100, bg='green')
	mass.grid(column=0, row=0)

def wDock(mass):
	mass = Frame(mass, width=100, height=100, bg='blue')
	mass.grid(column=1, row=0)



def dock(inputs):

	inputs = Frame(inputs, width=170, bg='#555555')
	inputs.pack(side=RIGHT, fill=BOTH, expand=0)

	but = Button(inputs, text="keluar", command=inputs.quit, bg='blue', fg='#dddddd')
	but.grid(column=0, row=0, pady=0, padx=10)
	but.config(width=15, highlightbackground='#666666')

	but1 = Button(inputs, text="edit", bg='blue', fg='#dddddd')
	but1.grid(column=0, row=1, pady=10, padx=10)

def footer(sans):
	sans = Frame(sans, height=30, bg='#555555')
	sans.pack(side=TOP, fill=X, expand=0)
	sans.config(highlightbackground='white', relief='sunken')

	isd = Label(sans, text="alpha v0.01.03", bg='#666666', fg='white', padx=10, relief='flat')
	isd.pack(side=RIGHT)
