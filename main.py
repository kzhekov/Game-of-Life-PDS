from __future__ import with_statement
import numpy as np
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from qtdesigner2 import Ui_MplMainWindow
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import threading

ALIVE = 1
DEAD = 0

class DesignerMainWindow(QtWidgets.QMainWindow, Ui_MplMainWindow):
    def __init__(self, parent=None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.size = 100
        self.grid = np.random.choice([ALIVE, DEAD], self.size * self.size, p=[0.1, 0.9]).reshape(self.size, self.size)
        self.mat = self.mpl.canvas.ax.matshow(self.grid, interpolation='none', cmap='Greens')
        
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)
        
        self.resume_button_clicked()
        self.pauseButton.clicked.connect(self.pause_button_clicked)
        #self.resumeButton.clicked.connect(self.resume_button_clicked)
        self.stepModeButton.clicked.connect(self.activate_step_by_step)
        self.nextStepButton.clicked.connect(self.update)
        self.horizontalSlider.valueChanged.connect(self.slider_moved)
        
        
    def pause_button_clicked(self):
        self.timer.stop()
        self.pauseButton.setText("Resume Simulation")
        self.pauseButton.clicked.connect(self.resume_button_clicked)
        
    def resume_button_clicked(self):
        self.timer.start(self.horizontalSlider.value())
        self.pauseButton.setText("Pause Simulation")
        self.pauseButton.clicked.connect(self.pause_button_clicked)
        
    def slider_moved(self):
        self.timer.start(self.horizontalSlider.value())
        
    def activate_step_by_step(self):
        self.pause_button_clicked()
        self.nextStepButton.setEnabled(True)
        self.stepModeButton.setText("Disable Step-by-Step")
        self.stepModeButton.clicked.connect(self.disable_step_by_step)
    
    def disable_step_by_step(self):
        self.resume_button_clicked()
        self.nextStepButton.setEnabled(False)
        self.stepModeButton.clicked.connect(self.activate_step_by_step)
        self.stepModeButton.setText("Enable Step-by-Step")
        
    def select_file(self):
        file = QtGui.QFileDialog.getOpenFileName()
        if file:
            self.mpllineEdit.setText(file)

    def parse_file(self, filename):
        pass
    
    def thread_update(self):
        threading.Thread(target=self.update).start()

    def update(self):
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
        self.mat.set_data(newGrid)
        self.grid = newGrid
        #self.mpl.canvas.ax.clear()
        #self.mat = self.mpl.canvas.ax.matshow(self.grid, interpolation='sinc', cmap='tab20c')
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
