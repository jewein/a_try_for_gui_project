import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from PyQt5.QtCore import QTimer
from OpenGL.GL import *
import numpy as np

class OpenGLWidget(QOpenGLWidget):
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        self.angle = 0.0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateRotation)
        self.timer.start(16)  # 60 FPS

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glPushMatrix()
        glRotatef(self.angle, 0, 0, 1)
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(0.0, 1.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(-1.0, -1.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(1.0, -1.0)
        glEnd()
        glPopMatrix()

    def updateRotation(self):
        self.angle += 1.0
        if self.angle >= 360:
            self.angle -= 360
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    glWidget = OpenGLWidget()
    window.setCentralWidget(glWidget)
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec())




