import time
import tkinter
from tkinter import *
from OpenGL import GL
from pyopengltk import OpenGLFrame
from OpenGL import GLU
from LayerUtama.window2 import *


class open(OpenGLFrame):
    def initgl(self):
        """Initalize gl states when the frame is created"""
        GL.glViewport(0, 0, self.width, self.height)
        GL.glClearColor(0.0, 0.0, 0.0, 0.0)   
        GL.glLoadIdentity()
        GLU.gluPerspective(45, (self.width/self.height), 0.1, 70.0)
        GL.glTranslatef(0.0,0.0, -10)
        GLU.gluLookAt(0.0, -2.0, 3.0,  10.0, 10.0, 0.0,  0.0, 0.0, 1.0)
 
        self.start = time.time()
        self.nframes = 0
    

    def redraw(self):
        """Render a single frame"""
        x1 = 0.0
        x2 = 0.0

        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

        GL.glBegin(GL.GL_LINES)
        for i in range(100):
            GL.glVertex3f(x1, 500.0, 0.0)
            GL.glVertex3f(x1, -500.0, 0.0)
            GL.glVertex3f(-x1, 500.0, 0.0)
            GL.glVertex3f(-x1, -500.0, 0.0)
            x1 = x1 + 2.0

        for i in range(100):
            GL.glVertex3f(500, x2, 0.0)
            GL.glVertex3f(-500, x2, 0.0)
            GL.glVertex3f(500, -x2, 0.0)
            GL.glVertex3f(-500, -x2, 0.0)
            x2 = x2 + 2.0


        GL.glEnd()
        tm = time.time() - self.start
        self.nframes += 1
        print("fps",self.nframes / tm, end="\r" )
    '''def initgl(self):
        """Initalize gl states when the frame is created"""
        GL.glViewport(0, 0, 500, 500)
        GL.glClearColor(0.0, 1.0, 0.0, 0.0)    
        self.start = time.time()
        self.nframes = 0
    

    def redraw(self):
        """Render a single frame"""
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        tm = time.time() - self.start
        self.nframes += 1
        print("fps",self.nframes / tm, end="\r" )'''

verticies = (    (1, -1, -1),    (1, 1, -1),    (-1, 1, -1),    (-1, -1, -1),
                 (1, -1, 1),    (1, 1, 1),    (-1, -1, 1),    (-1, 1, 1)    )

edges = (    (0,1),    (0,3),    (0,4),    (2,1),    (2,3),    (2,7),
    (6,3),    (6,4),    (6,7),    (5,1),    (5,4),    (5,7)    )

def Cube():
    GL.glBegin(GL.GL_LINES)
    for edge in edges:
        for vertex in edge:
            GL.glVertex3fv(verticies[vertex])
    GL.glEnd()

class CubeSpinner( OpenGLFrame ):
    def initgl(self):
        GL.glLoadIdentity()
        GLU.gluPerspective(90, (self.width/self.height), 0.1, 50.0)
        GL.glTranslatef(0.0,0.0, -5)
    def redraw(self):
        GL.glRotatef(1, 3, 1, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        Cube()

def maine():
    m =tkinter.Tk()
    frm = CubeSpinner(m, width=200, height=200)
    frm.animate = 10
    frm.pack(side=LEFT, fill=BOTH, expand = 1)
    return m.mainloop()

class Window1(Toplevel):
    def __init__(self, parent, title):
        Toplevel.__init__(self, parent)
        self.title(title)
         
        self.aturKomponen()
        self.transient(parent)
        self.grab_set()
        self.wait_window()
         
    def aturKomponen(self):
        mainFrame = CubeSpinner(self, width=300, height=300)
        mainFrame.animate=10
        mainFrame.pack(fill=BOTH, expand=1)
         

class Window2(Toplevel):
    def __init__(self, parent, title):
        Toplevel.__init__(self, parent)
        self.title(title)
         
        self.aturKomponen()
         
    def aturKomponen(self):
        mainFrame = ShaderFrame(self, width=512, height=512)
        mainFrame.pack(fill=BOTH, expand=1)
        mainFrame.after(100, app.printContext)
        mainFrame.animate = 1000 // 60
        mainFrame.animate = 1