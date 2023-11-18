import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from OpenGL.GL import *

class OpenGLWidget(QOpenGLWidget):
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(0.0, 1.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(-1.0, -1.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(1.0, -1.0)
        glEnd()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    glWidget = OpenGLWidget()
    window.setCentralWidget(glWidget)
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())
