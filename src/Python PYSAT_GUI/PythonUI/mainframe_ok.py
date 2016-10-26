# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nfinch\Desktop\GitHub\PySAT\src\PYSAT_Gui_UI_Forms\00_mainframe_ok.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(581, 843)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_9.setMargin(11)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.scrollArea = QtGui.QScrollArea(self.centralWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaContents = QtGui.QWidget()
        self.scrollAreaContents.setGeometry(QtCore.QRect(0, 0, 561, 742))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.scrollAreaContents.setFont(font)
        self.scrollAreaContents.setStyleSheet(_fromUtf8("QGroupBox {\n"
"  border: 2px solid gray;\n"
"  border-radius: 6px;\n"
"  margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"\n"
"  padding-top: -14px;\n"
"  padding-left: 8px;\n"
"}\n"
""))
        self.scrollAreaContents.setObjectName(_fromUtf8("scrollAreaContents"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaContents)
        self.verticalLayout_8.setMargin(11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.scrollArea.setWidget(self.scrollAreaContents)
        self.verticalLayout_9.addWidget(self.scrollArea)
        self.OK = QtGui.QGroupBox(self.centralWidget)
        self.OK.setObjectName(_fromUtf8("OK"))
        self.ok = QtGui.QHBoxLayout(self.OK)
        self.ok.setMargin(11)
        self.ok.setSpacing(6)
        self.ok.setObjectName(_fromUtf8("ok"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ok.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(self.OK)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.okButton.setFont(font)
        self.okButton.setMouseTracking(False)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.ok.addWidget(self.okButton)
        self.verticalLayout_9.addWidget(self.OK)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionLoad_Refence_Data = QtGui.QAction(MainWindow)
        self.actionLoad_Refence_Data.setObjectName(_fromUtf8("actionLoad_Refence_Data"))
        self.actionLoad_Unknown_Data = QtGui.QAction(MainWindow)
        self.actionLoad_Unknown_Data.setObjectName(_fromUtf8("actionLoad_Unknown_Data"))
        self.actionSave_Current_Workflow = QtGui.QAction(MainWindow)
        self.actionSave_Current_Workflow.setObjectName(_fromUtf8("actionSave_Current_Workflow"))
        self.actionSave_Current_Plots = QtGui.QAction(MainWindow)
        self.actionSave_Current_Plots.setObjectName(_fromUtf8("actionSave_Current_Plots"))
        self.actionSave_Current_Data = QtGui.QAction(MainWindow)
        self.actionSave_Current_Data.setObjectName(_fromUtf8("actionSave_Current_Data"))
        self.actionCreate_New_Workflow = QtGui.QAction(MainWindow)
        self.actionCreate_New_Workflow.setObjectName(_fromUtf8("actionCreate_New_Workflow"))
        self.actionNoise_Reduction = QtGui.QAction(MainWindow)
        self.actionNoise_Reduction.setObjectName(_fromUtf8("actionNoise_Reduction"))
        self.actionApply_Mask = QtGui.QAction(MainWindow)
        self.actionApply_Mask.setObjectName(_fromUtf8("actionApply_Mask"))
        self.actionInterpolate = QtGui.QAction(MainWindow)
        self.actionInterpolate.setObjectName(_fromUtf8("actionInterpolate"))
        self.actionInstrument_Response = QtGui.QAction(MainWindow)
        self.actionInstrument_Response.setObjectName(_fromUtf8("actionInstrument_Response"))
        self.actionALS = QtGui.QAction(MainWindow)
        self.actionALS.setObjectName(_fromUtf8("actionALS"))
        self.actionDietrich = QtGui.QAction(MainWindow)
        self.actionDietrich.setObjectName(_fromUtf8("actionDietrich"))
        self.actionPolyFit = QtGui.QAction(MainWindow)
        self.actionPolyFit.setObjectName(_fromUtf8("actionPolyFit"))
        self.actionAirPLS = QtGui.QAction(MainWindow)
        self.actionAirPLS.setObjectName(_fromUtf8("actionAirPLS"))
        self.actionFABC = QtGui.QAction(MainWindow)
        self.actionFABC.setObjectName(_fromUtf8("actionFABC"))
        self.actionKK = QtGui.QAction(MainWindow)
        self.actionKK.setObjectName(_fromUtf8("actionKK"))
        self.actionMario = QtGui.QAction(MainWindow)
        self.actionMario.setObjectName(_fromUtf8("actionMario"))
        self.actionMedian = QtGui.QAction(MainWindow)
        self.actionMedian.setObjectName(_fromUtf8("actionMedian"))
        self.actionRubberband = QtGui.QAction(MainWindow)
        self.actionRubberband.setObjectName(_fromUtf8("actionRubberband"))
        self.actionUndecimated_Wavelet = QtGui.QAction(MainWindow)
        self.actionUndecimated_Wavelet.setObjectName(_fromUtf8("actionUndecimated_Wavelet"))
        self.actionRatio = QtGui.QAction(MainWindow)
        self.actionRatio.setObjectName(_fromUtf8("actionRatio"))
        self.actionTommy_s_Methgod = QtGui.QAction(MainWindow)
        self.actionTommy_s_Methgod.setObjectName(_fromUtf8("actionTommy_s_Methgod"))
        self.actionPiecewise_Direct_Standardization = QtGui.QAction(MainWindow)
        self.actionPiecewise_Direct_Standardization.setObjectName(_fromUtf8("actionPiecewise_Direct_Standardization"))
        self.actionPCA = QtGui.QAction(MainWindow)
        self.actionPCA.setObjectName(_fromUtf8("actionPCA"))
        self.actionICA = QtGui.QAction(MainWindow)
        self.actionICA.setObjectName(_fromUtf8("actionICA"))
        self.actionK_Means = QtGui.QAction(MainWindow)
        self.actionK_Means.setObjectName(_fromUtf8("actionK_Means"))
        self.actionHierarchical = QtGui.QAction(MainWindow)
        self.actionHierarchical.setObjectName(_fromUtf8("actionHierarchical"))
        self.actionOthers = QtGui.QAction(MainWindow)
        self.actionOthers.setObjectName(_fromUtf8("actionOthers"))
        self.actionOthers_2 = QtGui.QAction(MainWindow)
        self.actionOthers_2.setObjectName(_fromUtf8("actionOthers_2"))
        self.actionOthers_3 = QtGui.QAction(MainWindow)
        self.actionOthers_3.setObjectName(_fromUtf8("actionOthers_3"))
        self.actionPLS = QtGui.QAction(MainWindow)
        self.actionPLS.setObjectName(_fromUtf8("actionPLS"))
        self.actionSM_PLS = QtGui.QAction(MainWindow)
        self.actionSM_PLS.setObjectName(_fromUtf8("actionSM_PLS"))
        self.actionICA_Regression = QtGui.QAction(MainWindow)
        self.actionICA_Regression.setObjectName(_fromUtf8("actionICA_Regression"))
        self.actionGaussian_Process = QtGui.QAction(MainWindow)
        self.actionGaussian_Process.setObjectName(_fromUtf8("actionGaussian_Process"))
        self.actionMLP = QtGui.QAction(MainWindow)
        self.actionMLP.setObjectName(_fromUtf8("actionMLP"))
        self.actionSVM = QtGui.QAction(MainWindow)
        self.actionSVM.setObjectName(_fromUtf8("actionSVM"))
        self.actionOthers_4 = QtGui.QAction(MainWindow)
        self.actionOthers_4.setObjectName(_fromUtf8("actionOthers_4"))
        self.actionOthers_5 = QtGui.QAction(MainWindow)
        self.actionOthers_5.setObjectName(_fromUtf8("actionOthers_5"))
        self.actionIndex = QtGui.QAction(MainWindow)
        self.actionIndex.setObjectName(_fromUtf8("actionIndex"))
        self.actionContent_2 = QtGui.QAction(MainWindow)
        self.actionContent_2.setObjectName(_fromUtf8("actionContent_2"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_QtCreator = QtGui.QAction(MainWindow)
        self.actionAbout_QtCreator.setObjectName(_fromUtf8("actionAbout_QtCreator"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionNormalization = QtGui.QAction(MainWindow)
        self.actionNormalization.setObjectName(_fromUtf8("actionNormalization"))
        self.actionICA_2 = QtGui.QAction(MainWindow)
        self.actionICA_2.setObjectName(_fromUtf8("actionICA_2"))
        self.actionPCA_2 = QtGui.QAction(MainWindow)
        self.actionPCA_2.setObjectName(_fromUtf8("actionPCA_2"))
        self.actionPLS_DA = QtGui.QAction(MainWindow)
        self.actionPLS_DA.setObjectName(_fromUtf8("actionPLS_DA"))
        self.actionSIMCA = QtGui.QAction(MainWindow)
        self.actionSIMCA.setObjectName(_fromUtf8("actionSIMCA"))
        self.actionK_means = QtGui.QAction(MainWindow)
        self.actionK_means.setObjectName(_fromUtf8("actionK_means"))
        self.actionHierarchical_2 = QtGui.QAction(MainWindow)
        self.actionHierarchical_2.setObjectName(_fromUtf8("actionHierarchical_2"))
        self.actionCross_Validation = QtGui.QAction(MainWindow)
        self.actionCross_Validation.setObjectName(_fromUtf8("actionCross_Validation"))
        self.actionTrain = QtGui.QAction(MainWindow)
        self.actionTrain.setObjectName(_fromUtf8("actionTrain"))
        self.actionPredict = QtGui.QAction(MainWindow)
        self.actionPredict.setObjectName(_fromUtf8("actionPredict"))
        self.actionLine_Plot = QtGui.QAction(MainWindow)
        self.actionLine_Plot.setObjectName(_fromUtf8("actionLine_Plot"))
        self.action1_to_1_Plot = QtGui.QAction(MainWindow)
        self.action1_to_1_Plot.setObjectName(_fromUtf8("action1_to_1_Plot"))
        self.actionScatter_Plot = QtGui.QAction(MainWindow)
        self.actionScatter_Plot.setObjectName(_fromUtf8("actionScatter_Plot"))
        self.actionSet_output_location = QtGui.QAction(MainWindow)
        self.actionSet_output_location.setObjectName(_fromUtf8("actionSet_output_location"))
        self.actionCreate_N_Folds = QtGui.QAction(MainWindow)
        self.actionCreate_N_Folds.setObjectName(_fromUtf8("actionCreate_N_Folds"))
        self.actionCreate_Test_Folds = QtGui.QAction(MainWindow)
        self.actionCreate_Test_Folds.setObjectName(_fromUtf8("actionCreate_Test_Folds"))
        self.actionSubmodel_Ranges = QtGui.QAction(MainWindow)
        self.actionSubmodel_Ranges.setObjectName(_fromUtf8("actionSubmodel_Ranges"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PYSAT", None))
        self.okButton.setText(_translate("MainWindow", "OK", None))
        self.actionLoad_Refence_Data.setText(_translate("MainWindow", "Load Refence Data", None))
        self.actionLoad_Unknown_Data.setText(_translate("MainWindow", "Load Unknown Data", None))
        self.actionSave_Current_Workflow.setText(_translate("MainWindow", "Save Current Workflow", None))
        self.actionSave_Current_Plots.setText(_translate("MainWindow", "Save Current Plots", None))
        self.actionSave_Current_Data.setText(_translate("MainWindow", "Save Current Data", None))
        self.actionCreate_New_Workflow.setText(_translate("MainWindow", "Create New Workflow", None))
        self.actionNoise_Reduction.setText(_translate("MainWindow", "Noise Reduction", None))
        self.actionApply_Mask.setText(_translate("MainWindow", "Apply Mask", None))
        self.actionInterpolate.setText(_translate("MainWindow", "Interpolate (unknown to known)", None))
        self.actionInstrument_Response.setText(_translate("MainWindow", "Instrument Response", None))
        self.actionALS.setText(_translate("MainWindow", "ALS", None))
        self.actionDietrich.setText(_translate("MainWindow", "Dietrich", None))
        self.actionPolyFit.setText(_translate("MainWindow", "PolyFit", None))
        self.actionAirPLS.setText(_translate("MainWindow", "AirPLS", None))
        self.actionFABC.setText(_translate("MainWindow", "FABC", None))
        self.actionKK.setText(_translate("MainWindow", "KK", None))
        self.actionMario.setText(_translate("MainWindow", "Mario", None))
        self.actionMedian.setText(_translate("MainWindow", "Median", None))
        self.actionRubberband.setText(_translate("MainWindow", "Rubberband", None))
        self.actionUndecimated_Wavelet.setText(_translate("MainWindow", "Undecimated Wavelet", None))
        self.actionRatio.setText(_translate("MainWindow", "Ratio", None))
        self.actionTommy_s_Methgod.setText(_translate("MainWindow", "Tommy\'s Method", None))
        self.actionPiecewise_Direct_Standardization.setText(_translate("MainWindow", "Piecewise Direct Standardization", None))
        self.actionPCA.setText(_translate("MainWindow", "PCA", None))
        self.actionICA.setText(_translate("MainWindow", "ICA", None))
        self.actionK_Means.setText(_translate("MainWindow", "K-Means", None))
        self.actionHierarchical.setText(_translate("MainWindow", "Hierarchical", None))
        self.actionOthers.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_2.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_3.setText(_translate("MainWindow", "Others...", None))
        self.actionPLS.setText(_translate("MainWindow", "PLS", None))
        self.actionSM_PLS.setText(_translate("MainWindow", "SM-PLS", None))
        self.actionICA_Regression.setText(_translate("MainWindow", "ICA Regression", None))
        self.actionGaussian_Process.setText(_translate("MainWindow", "Gaussian Process", None))
        self.actionMLP.setText(_translate("MainWindow", "MLP", None))
        self.actionSVM.setText(_translate("MainWindow", "SVM", None))
        self.actionOthers_4.setText(_translate("MainWindow", "Others...", None))
        self.actionOthers_5.setText(_translate("MainWindow", "Others...", None))
        self.actionIndex.setText(_translate("MainWindow", "Index", None))
        self.actionContent_2.setText(_translate("MainWindow", "Content", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionAbout_QtCreator.setText(_translate("MainWindow", "About Qt...", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionNormalization.setText(_translate("MainWindow", "Normalization", None))
        self.actionICA_2.setText(_translate("MainWindow", "ICA", None))
        self.actionPCA_2.setText(_translate("MainWindow", "PCA", None))
        self.actionPLS_DA.setText(_translate("MainWindow", "PLS-DA", None))
        self.actionSIMCA.setText(_translate("MainWindow", "SIMCA", None))
        self.actionK_means.setText(_translate("MainWindow", "K-means", None))
        self.actionHierarchical_2.setText(_translate("MainWindow", "Hierarchical", None))
        self.actionCross_Validation.setText(_translate("MainWindow", "Cross Validation", None))
        self.actionTrain.setText(_translate("MainWindow", "Train", None))
        self.actionPredict.setText(_translate("MainWindow", "Predict", None))
        self.actionLine_Plot.setText(_translate("MainWindow", "Line Plot", None))
        self.action1_to_1_Plot.setText(_translate("MainWindow", "1 to 1 Plot", None))
        self.actionScatter_Plot.setText(_translate("MainWindow", "Scatter Plot", None))
        self.actionSet_output_location.setText(_translate("MainWindow", "Output Location", None))
        self.actionCreate_N_Folds.setText(_translate("MainWindow", "Create N Folds", None))
        self.actionCreate_Test_Folds.setText(_translate("MainWindow", "Create Test Folds", None))
        self.actionSubmodel_Ranges.setText(_translate("MainWindow", "Submodel Ranges", None))

