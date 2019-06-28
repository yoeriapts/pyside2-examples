# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Thu Jun 27 16:53:35 2019
#      by: pyside2-uic  running on PySide2 5.9.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setObjectName("vboxlayout")
        self.view = QtWidgets.QTreeView(self.centralwidget)
        self.view.setAlternatingRowColors(True)
        self.view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.view.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.view.setAnimated(False)
        self.view.setAllColumnsShowFocus(True)
        self.view.setObjectName("view")
        self.vboxlayout.addWidget(self.view)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 26))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        self.actionsMenu = QtWidgets.QMenu(self.menubar)
        self.actionsMenu.setObjectName("actionsMenu")
        self.dataMenu = QtWidgets.QMenu(self.menubar)
        self.dataMenu.setTearOffEnabled(False)
        self.dataMenu.setObjectName("dataMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exitAction = QtWidgets.QAction(MainWindow)
        self.exitAction.setObjectName("exitAction")
        self.insertRowAction = QtWidgets.QAction(MainWindow)
        self.insertRowAction.setObjectName("insertRowAction")
        self.removeRowAction = QtWidgets.QAction(MainWindow)
        self.removeRowAction.setObjectName("removeRowAction")
        self.insertColumnAction = QtWidgets.QAction(MainWindow)
        self.insertColumnAction.setObjectName("insertColumnAction")
        self.removeColumnAction = QtWidgets.QAction(MainWindow)
        self.removeColumnAction.setObjectName("removeColumnAction")
        self.insertChildAction = QtWidgets.QAction(MainWindow)
        self.insertChildAction.setObjectName("insertChildAction")
        self.showPyObjAction = QtWidgets.QAction(MainWindow)
        self.showPyObjAction.setObjectName("showPyObjAction")
        self.fileMenu.addAction(self.exitAction)
        self.actionsMenu.addAction(self.insertRowAction)
        self.actionsMenu.addAction(self.insertColumnAction)
        self.actionsMenu.addSeparator()
        self.actionsMenu.addAction(self.removeRowAction)
        self.actionsMenu.addAction(self.removeColumnAction)
        self.actionsMenu.addSeparator()
        self.actionsMenu.addAction(self.insertChildAction)
        self.dataMenu.addAction(self.showPyObjAction)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.actionsMenu.menuAction())
        self.menubar.addAction(self.dataMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Editable Tree Model w Data", None, -1))
        self.fileMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.actionsMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Actions", None, -1))
        self.dataMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Data", None, -1))
        self.exitAction.setText(QtWidgets.QApplication.translate("MainWindow", "E&xit", None, -1))
        self.exitAction.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.insertRowAction.setText(QtWidgets.QApplication.translate("MainWindow", "Insert Row", None, -1))
        self.insertRowAction.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+I, R", None, -1))
        self.removeRowAction.setText(QtWidgets.QApplication.translate("MainWindow", "Remove Row", None, -1))
        self.removeRowAction.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+R, R", None, -1))
        self.insertColumnAction.setText(QtWidgets.QApplication.translate("MainWindow", "Insert Column", None, -1))
        self.insertColumnAction.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+I, C", None, -1))
        self.removeColumnAction.setText(QtWidgets.QApplication.translate("MainWindow", "Remove Column", None, -1))
        self.removeColumnAction.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+R, C", None, -1))
        self.insertChildAction.setText(QtWidgets.QApplication.translate("MainWindow", "Insert Child", None, -1))
        self.insertChildAction.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+N", None, -1))
        self.showPyObjAction.setText(QtWidgets.QApplication.translate("MainWindow", "Show Python Object", None, -1))
        self.showPyObjAction.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))

import editabletreemodel_rc
