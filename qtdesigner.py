# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName("MplMainWindow")
        MplMainWindow.resize(791, 600)
        self.mplcentralwidget = QtWidgets.QWidget(MplMainWindow)
        self.mplcentralwidget.setObjectName("mplcentralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mplcentralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mplhorizontalLayout = QtWidgets.QHBoxLayout()
        self.mplhorizontalLayout.setObjectName("mplhorizontalLayout")
        self.mpllineEdit = QtWidgets.QLineEdit(self.mplcentralwidget)
        self.mpllineEdit.setText("")
        self.mpllineEdit.setObjectName("mpllineEdit")
        self.mplhorizontalLayout.addWidget(self.mpllineEdit)
        self.mplpushButton = QtWidgets.QPushButton(self.mplcentralwidget)
        self.mplpushButton.setObjectName("mplpushButton")
        self.mplhorizontalLayout.addWidget(self.mplpushButton)
        self.verticalLayout.addLayout(self.mplhorizontalLayout)
        self.mpl = MplWidget(self.mplcentralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setObjectName("mpl")
        self.verticalLayout.addWidget(self.mpl)
        MplMainWindow.setCentralWidget(self.mplcentralwidget)
        self.menubar = QtWidgets.QMenuBar(MplMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 21))
        self.menubar.setObjectName("menubar")
        self.mplmenuFile = QtWidgets.QMenu(self.menubar)
        self.mplmenuFile.setObjectName("mplmenuFile")
        MplMainWindow.setMenuBar(self.menubar)
        self.mplactionOpen = QtWidgets.QAction(MplMainWindow)
        self.mplactionOpen.setObjectName("mplactionOpen")
        self.actionExit = QtWidgets.QAction(MplMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(MplMainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.mplactionQuit = QtWidgets.QAction(MplMainWindow)
        self.mplactionQuit.setObjectName("mplactionQuit")
        self.mplmenuFile.addAction(self.mplactionOpen)
        self.mplmenuFile.addSeparator()
        self.mplmenuFile.addAction(self.mplactionQuit)
        self.menubar.addAction(self.mplmenuFile.menuAction())

        self.retranslateUi(MplMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)

    def retranslateUi(self, MplMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MplMainWindow.setWindowTitle(_translate("MplMainWindow", "MainWindow"))
        self.mplpushButton.setText(_translate("MplMainWindow", "Execute"))
        self.mplmenuFile.setTitle(_translate("MplMainWindow", "File"))
        self.mplactionOpen.setText(_translate("MplMainWindow", "Open"))
        self.actionExit.setText(_translate("MplMainWindow", "Pause"))
        self.actionExit_2.setText(_translate("MplMainWindow", "Exit"))
        self.mplactionQuit.setText(_translate("MplMainWindow", "Quit"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MplMainWindow = QtWidgets.QMainWindow()
    ui = Ui_MplMainWindow()
    ui.setupUi(MplMainWindow)
    MplMainWindow.show()
    sys.exit(app.exec_())

