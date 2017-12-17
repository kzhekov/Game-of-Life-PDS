from __future__ import with_statement
import numpy as np
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MplMainWindow
import threading
#from lifethread import LifeThread
import multiprocessing
#import matplotlib.animation as animation
import time

ALIVE = 1
DEAD = 0

class MyListModel(QtCore.QAbstractListModel): 
    def __init__(self, datain, parent=None, *args): 
        """ datain: a list where each item is a row
        """
        QtCore.QAbstractListModel.__init__(self, parent, *args) 
        self.listdata = datain
 
    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self.listdata) 
 
    def data(self, index, role): 
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.listdata[index.row()])
        else: 
            return QtCore.QVariant()

class DesignerMainWindow(QtWidgets.QMainWindow, Ui_MplMainWindow):
    def __init__(self, parent=None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.thread_count = multiprocessing.cpu_count()
        #self.animation = animation.FuncAnimation(self.mpl.canvas.fig, self.update_plot, interval=25, blit=True)
        
        self.init_values()
        #self.resume_button_clicked()
        self.list_configs()
        
        self.pauseButton.clicked.connect(self.resume_button_clicked)
        #self.restartButton.clicked.connect(self.init_values)
        self.stepModeButton.clicked.connect(self.activate_step_by_step)
        self.nextStepButton.clicked.connect(self.update)
        self.horizontalSlider.valueChanged.connect(self.slider_moved)
        self.fileMod.setText("Random")
        self.genMod.setText(str(self.counter))
        self.speedMod.setText(str(self.horizontalSlider.value()))
        
    def init_values(self):
        self.counter = 1
        self.size = 155
        self.grid = np.random.choice([ALIVE, DEAD], self.size * self.size, p=[0.1, 0.9]).reshape(self.size, self.size)
        self.mat = self.mpl.canvas.ax.imshow(self.grid, interpolation='none', cmap='Greys')
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.stop()
        
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
        self.speedMod.setText(str(self.horizontalSlider.value()))

        
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
        
    def list_configs(self):
        initial_list = os.listdir("../config/")
        list_model = MyListModel(initial_list, self)
        self.listView.setModel(list_model)
        
    def select_file(self):
        file = QtGui.QFileDialog.getOpenFileName()
        if file:
            self.mpllineEdit.setText(file)

    def parse_file(self, filename):
        pass
    
    def thread_update(self):
        if threading.active_count < self.thread_count:
            threading.Thread(target=self.update).start()

    def update(self, data=None):
        start = time.time()
        oldGrid = self.grid.copy()
        newGrid = self.grid.copy()
        for i in range(self.size):
            for j in range(self.size):
                try:
                    total = (oldGrid[i, (j - 1)] + oldGrid[i, (j + 1)] +
                             oldGrid[(i - 1), j] + oldGrid[(i + 1), j] +
                             oldGrid[(i - 1), (j - 1)] + oldGrid[(i - 1), (j + 1)] +
                             oldGrid[(i + 1), (j - 1)] + oldGrid[(i + 1), (j + 1)])
                    if self.grid[i, j] == ALIVE:
                        if (total < 2) or (total > 3):
                            newGrid[i, j] = DEAD
                    elif total == 3:
                            newGrid[i, j] = ALIVE
                except IndexError:
                    pass
        
        self.counter += 1
        self.genMod.setText(str(self.counter))
        self.mat.set_data(newGrid)
        self.grid = newGrid
        # self.mat = self.mpl.canvas.ax.matshow(self.grid, interpolation='sinc', cmap='tab20c')
        self.mpl.canvas.draw_idle()
        end = time.time()
        print(end - start)
        return [self.mat]


# create the GUI application
app = QtWidgets.QApplication(sys.argv)
# instantiate the main window
dmw = DesignerMainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
