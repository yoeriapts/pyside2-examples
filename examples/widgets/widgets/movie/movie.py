#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2004-2005 Trolltech AS. All rights reserved.
##
## This file is part of the example classes of the Qt Toolkit.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http/www.trolltech.com/products/qt/opensource.html
##
## If you are unsure which license is appropriate for your use, please
## review the following information:
## http/www.trolltech.com/products/qt/licensing.html or contact the
## sales department at sales@trolltech.com.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
#############################################################################

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Slot

# from PyQt5 import QtCore, QtWidgets, QtGui
# #from PyQt5.QtCore import Slot


class MoviePlayer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MoviePlayer, self).__init__(parent)

        self.movie = QtGui.QMovie(self)
        self.movie.setCacheMode(QtGui.QMovie.CacheAll)

        self.movieLabel = QtWidgets.QLabel("No movie loaded")
        self.movieLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.movieLabel.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.movieLabel.setBackgroundRole(QtGui.QPalette.Dark)
        self.movieLabel.setAutoFillBackground(True)

        self.currentMovieDirectory = 'movies'

        self.createControls()
        self.createButtons()

        self.movie.frameChanged.connect(self.updateFrameSlider)
        self.movie.stateChanged.connect(self.updateButtons)
        self.fitCheckBox.clicked.connect(self.fitToWindow)
        self.frameSlider.valueChanged.connect(self.goToFrame)
        self.speedSpinBox.valueChanged.connect(self.movie.setSpeed)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.movieLabel)
        mainLayout.addLayout(self.controlsLayout)
        mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout)

        self.updateFrameSlider()
        self.updateButtons()

        self.setWindowTitle("Movie Player")
        self.resize(400, 400)

    #@Slot()
    def open(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open a Movie",
                self.currentMovieDirectory)[0]

        if fileName:
            self.openFile(fileName)

    def openFile(self, fileName):
        print("fileName:" + fileName)
        print(self.movie.supportedFormats())
        self.currentMovieDirectory = QtCore.QFileInfo(fileName).path()

        self.movie.stop()
        self.movieLabel.setMovie(self.movie)
        self.movie.setFileName(fileName)
        self.movie.start()

        self.updateFrameSlider();
        self.updateButtons();

    #@Slot()
    def goToFrame(self, frame):
        self.movie.jumpToFrame(frame)

    #@Slot()
    def fitToWindow(self):
        self.movieLabel.setScaledContents(self.fitCheckBox.isChecked())

    #@Slot()
    def updateFrameSlider(self):
        hasFrames = (self.movie.currentFrameNumber() >= 0)

        if hasFrames:
            if self.movie.frameCount() > 0:
                self.frameSlider.setMaximum(self.movie.frameCount() - 1)
            elif self.movie.currentFrameNumber() > self.frameSlider.maximum():
                self.frameSlider.setMaximum(self.movie.currentFrameNumber())

            self.frameSlider.setValue(self.movie.currentFrameNumber())
        else:
            self.frameSlider.setMaximum(0)

        self.frameLabel.setEnabled(hasFrames)
        self.frameSlider.setEnabled(hasFrames)

    #@Slot()
    def updateButtons(self):
        state = self.movie.state()

        self.playButton.setEnabled(self.movie.isValid() and
                self.movie.frameCount() != 1 and
                state == QtGui.QMovie.NotRunning)
        self.pauseButton.setEnabled(state != QtGui.QMovie.NotRunning)
        self.pauseButton.setChecked(state == QtGui.QMovie.Paused)
        self.stopButton.setEnabled(state != QtGui.QMovie.NotRunning)

    def createControls(self):
        self.fitCheckBox = QtWidgets.QCheckBox("Fit to Window")

        self.frameLabel = QtWidgets.QLabel("Current frame:")

        self.frameSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.frameSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.frameSlider.setTickInterval(10)

        speedLabel = QtWidgets.QLabel("Speed:")

        self.speedSpinBox = QtWidgets.QSpinBox()
        self.speedSpinBox.setRange(1, 9999)
        self.speedSpinBox.setValue(100)
        self.speedSpinBox.setSuffix("%")

        self.controlsLayout = QtWidgets.QGridLayout()
        self.controlsLayout.addWidget(self.fitCheckBox, 0, 0, 1, 2)
        self.controlsLayout.addWidget(self.frameLabel, 1, 0)
        self.controlsLayout.addWidget(self.frameSlider, 1, 1, 1, 2)
        self.controlsLayout.addWidget(speedLabel, 2, 0)
        self.controlsLayout.addWidget(self.speedSpinBox, 2, 1)

    def createButtons(self):
        iconSize = QtCore.QSize(36, 36)

        openButton = QtWidgets.QToolButton()
        openButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DialogOpenButton))
        openButton.setIconSize(iconSize)
        openButton.setToolTip("Open File")
        openButton.clicked.connect(self.open)

        self.playButton = QtWidgets.QToolButton()
        self.playButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.playButton.setIconSize(iconSize)
        self.playButton.setToolTip("Play")
        self.playButton.clicked.connect(self.movie.start)

        self.pauseButton = QtWidgets.QToolButton()
        self.pauseButton.setCheckable(True)
        self.pauseButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
        self.pauseButton.setIconSize(iconSize)
        self.pauseButton.setToolTip("Pause")
        self.pauseButton.clicked.connect(self.movie.setPaused)

        self.stopButton = QtWidgets.QToolButton()
        self.stopButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop))
        self.stopButton.setIconSize(iconSize)
        self.stopButton.setToolTip("Stop")
        self.stopButton.clicked.connect(self.movie.stop)

        quitButton = QtWidgets.QToolButton()
        quitButton.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DialogCloseButton))
        quitButton.setIconSize(iconSize)
        quitButton.setToolTip("Quit")
        quitButton.clicked.connect(self.close)

        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(openButton)
        self.buttonsLayout.addWidget(self.playButton)
        self.buttonsLayout.addWidget(self.pauseButton)
        self.buttonsLayout.addWidget(self.stopButton)
        self.buttonsLayout.addWidget(quitButton)
        self.buttonsLayout.addStretch()


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    player = MoviePlayer()
    player.show()
    sys.exit(app.exec_())

