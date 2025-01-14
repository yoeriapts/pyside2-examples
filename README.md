Converting 'old' examples to PySide2/Qt5.12
===========================================
```
'Many' classes moved from QtGui to QtWidget

QtGui.QWidget -> QtWidget.Qwidget
QtGui.QPrinter() -> QtPrintSupport.QPrinter()

str(f.readAll())) -> f.readAll.data.decode()
                     f.readAll -> returns QByteArray
                              .data() -> returns 'bytes'
                                     .decode() -> returns 'str'
    
```
Examples
========

PySide2 example scripts for PySide2. If you would like to install PySide2, please go to [pyside2-setup](https://github.com/PySide/pyside2-setup) for instructions.

Resources:

* [PySide2-setup](https://github.com/PySide/pyside2-setup)
  The container-project with the setup.py script. It contains the following sub-projects:
  * [PySide2 Wiki](https://github.com/PySide/pyside2/wiki)
    Developer information
  * [PySide2](https://github.com/PySide/pyside2)
    The PySide2 project
  * [Shiboken2](https://github.com/PySide/shiboken2)
    The Shiboken2 project
  * [PySide2-tools](https://github.com/PySide/pyside2-examples)
    The PySide2-tools project
  * [PySide2-examples](https://github.com/PySide/pyside2-examples)
    The PySide2 example scripts
