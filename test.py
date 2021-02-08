import time
from tkinter import *
from OpenGL import GL
from pyopengltk import OpenGLFrame
from OpenGL import GLU

class OpenGL(OpenGLFrame):
    def initgl(self):
        """Initalize gl states when the frame is created"""
        GL.glViewport(0, 0, self.width, self.height)
        GL.glClearColor(0.0, 0.0, 0.0, 0.0)   
        GL.glLoadIdentity()
        GLU.gluPerspective(45, (self.width/self.height), 0.1, 50.0)
        GL.glTranslatef(0.0,0.0, -10)
        GLU.gluLookAt(0.0, -0.02, 0.03,  0.1, 0.1, 0.0,  0.0, 0.0, 0.1)
 
        self.start = time.time()
        self.nframes = 0
    

    def redraw(self):
        """Render a single frame"""
        x1 = 0.0
        x2 = 0.0

        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

        GL.glBegin(GL.GL_LINES)
        for i in range(100):
            GL.glVertex3f(x1, 50.0, 0.0)
            GL.glVertex3f(x1, -50.0, 0.0)
            GL.glVertex3f(-x1, 50.0, 0.0)
            GL.glVertex3f(-x1, -50.0, 0.0)
            x1 = x1 + 1.0

        for i in range(100):
            GL.glVertex3f(50, x2, 0.0)
            GL.glVertex3f(-50, x2, 0.0)
            GL.glVertex3f(50, -x2, 0.0)
            GL.glVertex3f(-50, -x2, 0.0)
            x2 = x2 + 1.0

        GL.glEnd()
        GL.glRotatef(1, 3, 1, 1)
        tm = time.time() - self.start
        self.nframes += 1
        print("fps",self.nframes / tm, end="\r" )



if __name__ == '__main__':

    ss = Tk()
    app = OpenGL(ss, width=500, height=500)
    app.pack(fill=BOTH, expand=1)
    app.animate=15

    ss.mainloop()
