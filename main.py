from __future__ import with_statement
import numpy as np
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qtdesigner import Ui_MplMainWindow
import matplotlib.pyplot as plt
import matplotlib.animation as anm

ALIVE = 1
DEAD = 0


class DesignerMainWindow(QtWidgets.QMainWindow, Ui_MplMainWindow):
    def __init__(self, parent=None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.size = 100
        self.grid = np.random.choice([ALIVE, DEAD], self.size * self.size, p=[0.2, 0.8]).reshape(self.size, self.size)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100)
        #QtCore.QObject.connect(self.mplpushButton, QtCore.SIGNAL("clicked()"), self.start_simulation_button)
        #QtCore.QObject.connect(self.mplactionOpen, QtCore.SIGNAL('triggered()'), self.select_file)
        #QtCore.QObject.connect(self.mplactionQuit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT("quit()"))

    def select_file(self):
        file = QtGui.QFileDialog.getOpenFileName()
        if file:
            self.mpllineEdit.setText(file)

    def parse_file(self, filename):
        pass

    def update(self):
        mat = self.mpl.canvas.ax.matshow(self.grid)
        newGrid = self.grid.copy()
        for i in range(self.size):
            for j in range(self.size):
                total = (self.grid[i, (j - 1) % self.size] + self.grid[i, (j + 1) % self.size] +
                         self.grid[(i - 1) % self.size, j] + self.grid[(i + 1) % self.size, j] +
                         self.grid[(i - 1) % self.size, (j - 1) % self.size] + self.grid[(i - 1) % self.size, (j + 1) % self.size] +
                         self.grid[(i + 1) % self.size, (j - 1) % self.size] + self.grid[(i + 1) % self.size, (j + 1) % self.size])
                if self.grid[i, j] == ALIVE:
                    if (total < 2) or (total > 3):
                        newGrid[i, j] = DEAD
                else:
                    if total == 3:
                        newGrid[i, j] = ALIVE
        mat.set_data(newGrid)
        self.grid = newGrid
        self.mpl.canvas.ax.clear()
        mat = self.mpl.canvas.ax.matshow(self.grid)
        self.mpl.canvas.draw()


# create the GUI application
app = QtWidgets.QApplication(sys.argv)
# instantiate the main window
dmw = DesignerMainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
