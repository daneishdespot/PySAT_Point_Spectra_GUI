import sys
from PyQt5 import QtWidgets
from PythonUI import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
mainW = mainwindow.Ui_MainWindow()
mainW.setupUi(MainWindow)

widgetW = regression_train.Ui_Form()
widgetW.setupUi(mainW.centralwidget)
widgetW.yvarmax_spin.valueChanged.connect(lambda: print(widgetW.yvarmax_spin.value()))

MainWindow.show()
sys.exit(app.exec_())