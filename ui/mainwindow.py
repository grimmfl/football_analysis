# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(773, 546)
        icon = QtGui.QIcon.fromTheme("Fußball")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("backgounrd-color: rgb(84, 84, 84)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.grid = QtWidgets.QGridLayout()
        self.grid.setContentsMargins(11, 11, 11, 11)
        self.grid.setSpacing(6)
        self.grid.setObjectName("grid")
        self.gridLayout.addLayout(self.grid, 1, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.compare = QtWidgets.QPushButton(self.centralWidget)
        self.compare.setObjectName("compare")
        self.gridLayout_2.addWidget(self.compare, 2, 0, 1, 2)
        self.team2 = QtWidgets.QComboBox(self.centralWidget)
        self.team2.setObjectName("team2")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/Ägypten.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/Argentinien.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/Australien.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../images/Belgien.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../images/Brasilien.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../images/Costa Rica.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../images/Dänemark.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../images/Deutschland.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../images/England.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../images/Frankreich.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../images/Iran.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../images/Island.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon11, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../images/Japan.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon12, "")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../images/Kolumbien.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon13, "")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../images/Kroatien.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon14, "")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../images/Marokko.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon15, "")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("../images/Mexiko.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon16, "")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("../images/Nigeria.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon17, "")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("../images/Panama.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon18, "")
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("../images/Peru.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon19, "")
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("../images/Polen.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon20, "")
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("../images/Portugal.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon21, "")
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("../images/Russland.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon22, "")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("../images/Saudi-Arabien.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon23, "")
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("../images/Schweden.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon24, "")
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("../images/Schweiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon25, "")
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("../images/Senegal.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon26, "")
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("../images/Serbien.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon27, "")
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("../images/Spanien.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon28, "")
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("../images/Südkorea.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon29, "")
        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("../images/Tunesien.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon30, "")
        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("../images/Uruguay.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.team2.addItem(icon31, "")
        self.gridLayout_2.addWidget(self.team2, 0, 1, 1, 1)
        self.team1 = QtWidgets.QComboBox(self.centralWidget)
        self.team1.setObjectName("team1")
        self.team1.addItem(icon, "")
        self.team1.addItem(icon1, "")
        self.team1.addItem(icon2, "")
        self.team1.addItem(icon3, "")
        self.team1.addItem(icon4, "")
        self.team1.addItem(icon5, "")
        self.team1.addItem(icon6, "")
        self.team1.addItem(icon7, "")
        self.team1.addItem(icon8, "")
        self.team1.addItem(icon9, "")
        self.team1.addItem(icon10, "")
        self.team1.addItem(icon11, "")
        self.team1.addItem(icon12, "")
        self.team1.addItem(icon13, "")
        self.team1.addItem(icon14, "")
        self.team1.addItem(icon15, "")
        self.team1.addItem(icon16, "")
        self.team1.addItem(icon17, "")
        self.team1.addItem(icon18, "")
        self.team1.addItem(icon19, "")
        self.team1.addItem(icon20, "")
        self.team1.addItem(icon21, "")
        self.team1.addItem(icon22, "")
        self.team1.addItem(icon23, "")
        self.team1.addItem(icon24, "")
        self.team1.addItem(icon25, "")
        self.team1.addItem(icon26, "")
        self.team1.addItem(icon27, "")
        self.team1.addItem(icon28, "")
        self.team1.addItem(icon29, "")
        self.team1.addItem(icon30, "")
        self.team1.addItem(icon31, "")
        self.gridLayout_2.addWidget(self.team1, 0, 0, 1, 1)
        self.statistic1 = QtWidgets.QPushButton(self.centralWidget)
        self.statistic1.setObjectName("statistic1")
        self.gridLayout_2.addWidget(self.statistic1, 1, 0, 1, 1)
        self.statistic2 = QtWidgets.QPushButton(self.centralWidget)
        self.statistic2.setObjectName("statistic2")
        self.gridLayout_2.addWidget(self.statistic2, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 773, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.compare.setText(_translate("MainWindow", "Vergleichen"))
        self.team2.setItemText(0, _translate("MainWindow", "Ägypten"))
        self.team2.setItemText(1, _translate("MainWindow", "Argentinien"))
        self.team2.setItemText(2, _translate("MainWindow", "Australien"))
        self.team2.setItemText(3, _translate("MainWindow", "Belgien"))
        self.team2.setItemText(4, _translate("MainWindow", "Brasilien"))
        self.team2.setItemText(5, _translate("MainWindow", "Costa Rica"))
        self.team2.setItemText(6, _translate("MainWindow", "Dänemark"))
        self.team2.setItemText(7, _translate("MainWindow", "Deutschland"))
        self.team2.setItemText(8, _translate("MainWindow", "England"))
        self.team2.setItemText(9, _translate("MainWindow", "Frankreich"))
        self.team2.setItemText(10, _translate("MainWindow", "Iran"))
        self.team2.setItemText(11, _translate("MainWindow", "Island"))
        self.team2.setItemText(12, _translate("MainWindow", "Japan"))
        self.team2.setItemText(13, _translate("MainWindow", "Kolumbien"))
        self.team2.setItemText(14, _translate("MainWindow", "Kroatien"))
        self.team2.setItemText(15, _translate("MainWindow", "Marokko"))
        self.team2.setItemText(16, _translate("MainWindow", "Mexiko"))
        self.team2.setItemText(17, _translate("MainWindow", "Nigeria"))
        self.team2.setItemText(18, _translate("MainWindow", "Panama"))
        self.team2.setItemText(19, _translate("MainWindow", "Peru"))
        self.team2.setItemText(20, _translate("MainWindow", "Polen"))
        self.team2.setItemText(21, _translate("MainWindow", "Portugal"))
        self.team2.setItemText(22, _translate("MainWindow", "Russland"))
        self.team2.setItemText(23, _translate("MainWindow", "Saudi-Arabien"))
        self.team2.setItemText(24, _translate("MainWindow", "Schweden"))
        self.team2.setItemText(25, _translate("MainWindow", "Schweiz"))
        self.team2.setItemText(26, _translate("MainWindow", "Senegal"))
        self.team2.setItemText(27, _translate("MainWindow", "Serbien"))
        self.team2.setItemText(28, _translate("MainWindow", "Spanien"))
        self.team2.setItemText(29, _translate("MainWindow", "Südkorea"))
        self.team2.setItemText(30, _translate("MainWindow", "Tunesien"))
        self.team2.setItemText(31, _translate("MainWindow", "Uruguay"))
        self.team1.setItemText(0, _translate("MainWindow", "Ägypten"))
        self.team1.setItemText(1, _translate("MainWindow", "Argentinien"))
        self.team1.setItemText(2, _translate("MainWindow", "Australien"))
        self.team1.setItemText(3, _translate("MainWindow", "Belgien"))
        self.team1.setItemText(4, _translate("MainWindow", "Brasilien"))
        self.team1.setItemText(5, _translate("MainWindow", "Costa Rica"))
        self.team1.setItemText(6, _translate("MainWindow", "Dänemark"))
        self.team1.setItemText(7, _translate("MainWindow", "Deutschland"))
        self.team1.setItemText(8, _translate("MainWindow", "England"))
        self.team1.setItemText(9, _translate("MainWindow", "Frankreich"))
        self.team1.setItemText(10, _translate("MainWindow", "Iran"))
        self.team1.setItemText(11, _translate("MainWindow", "Island"))
        self.team1.setItemText(12, _translate("MainWindow", "Japan"))
        self.team1.setItemText(13, _translate("MainWindow", "Kolumbien"))
        self.team1.setItemText(14, _translate("MainWindow", "Kroatien"))
        self.team1.setItemText(15, _translate("MainWindow", "Marokko"))
        self.team1.setItemText(16, _translate("MainWindow", "Mexiko"))
        self.team1.setItemText(17, _translate("MainWindow", "Nigeria"))
        self.team1.setItemText(18, _translate("MainWindow", "Panama"))
        self.team1.setItemText(19, _translate("MainWindow", "Peru"))
        self.team1.setItemText(20, _translate("MainWindow", "Polen"))
        self.team1.setItemText(21, _translate("MainWindow", "Portugal"))
        self.team1.setItemText(22, _translate("MainWindow", "Russland"))
        self.team1.setItemText(23, _translate("MainWindow", "Saudi-Arabien"))
        self.team1.setItemText(24, _translate("MainWindow", "Schweden"))
        self.team1.setItemText(25, _translate("MainWindow", "Schweiz"))
        self.team1.setItemText(26, _translate("MainWindow", "Senegal"))
        self.team1.setItemText(27, _translate("MainWindow", "Serbien"))
        self.team1.setItemText(28, _translate("MainWindow", "Spanien"))
        self.team1.setItemText(29, _translate("MainWindow", "Südkorea"))
        self.team1.setItemText(30, _translate("MainWindow", "Tunesien"))
        self.team1.setItemText(31, _translate("MainWindow", "Uruguay"))
        self.statistic1.setText(_translate("MainWindow", "Zeige Statistik"))
        self.statistic2.setText(_translate("MainWindow", "Zeige Statistik"))

