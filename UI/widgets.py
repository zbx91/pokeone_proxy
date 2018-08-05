# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1391, 874)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_proxy = QtWidgets.QWidget()
        self.tab_proxy.setObjectName("tab_proxy")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_proxy)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_proxy)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_proxy_intercept = QtWidgets.QWidget()
        self.tab_proxy_intercept.setObjectName("tab_proxy_intercept")
        self.tabWidget_2.addTab(self.tab_proxy_intercept, "")
        self.tab_proxy_history = QtWidgets.QWidget()
        self.tab_proxy_history.setObjectName("tab_proxy_history")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_proxy_history)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.tab_proxy_history)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.proxy_history_table = QtWidgets.QTableWidget(self.splitter)
        self.proxy_history_table.setAutoFillBackground(True)
        self.proxy_history_table.setStyleSheet("QHeaderView::section { \n"
"    background-color:#dcdee3;\n"
"    border-radius: 45px;\n"
"    \n"
"}")
        self.proxy_history_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.proxy_history_table.setAlternatingRowColors(False)
        self.proxy_history_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.proxy_history_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.proxy_history_table.setShowGrid(True)
        self.proxy_history_table.setGridStyle(QtCore.Qt.SolidLine)
        self.proxy_history_table.setRowCount(0)
        self.proxy_history_table.setColumnCount(8)
        self.proxy_history_table.setObjectName("proxy_history_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.proxy_history_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.proxy_history_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.proxy_history_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.proxy_history_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.proxy_history_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.proxy_history_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.proxy_history_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.proxy_history_table.setHorizontalHeaderItem(7, item)
        self.proxy_history_table.horizontalHeader().setVisible(False)
        self.proxy_history_table.horizontalHeader().setCascadingSectionResizes(False)
        self.proxy_history_table.horizontalHeader().setDefaultSectionSize(100)
        self.proxy_history_table.horizontalHeader().setStretchLastSection(False)
        self.proxy_history_table.verticalHeader().setVisible(False)
        self.proxy_history_table.verticalHeader().setDefaultSectionSize(20)
        self.proxy_history_table.verticalHeader().setHighlightSections(False)
        self.proxy_history_table.verticalHeader().setMinimumSectionSize(0)
        self.proxy_history_table.verticalHeader().setSortIndicatorShown(False)
        self.proxy_history_table.verticalHeader().setStretchLastSection(False)
        self.proxy_packet_edit = QtWidgets.QTextEdit(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.proxy_packet_edit.setFont(font)
        self.proxy_packet_edit.setReadOnly(True)
        self.proxy_packet_edit.setObjectName("proxy_packet_edit")
        self.verticalLayout.addWidget(self.splitter)
        self.pushButton = QtWidgets.QPushButton(self.tab_proxy_history)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.tabWidget_2.addTab(self.tab_proxy_history, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_proxy, "")
        self.tab_repeater = QtWidgets.QWidget()
        self.tab_repeater.setObjectName("tab_repeater")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_repeater)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.repeater_edit = QtWidgets.QTextEdit(self.tab_repeater)
        self.repeater_edit.setReadOnly(False)
        self.repeater_edit.setObjectName("repeater_edit")
        self.verticalLayout_2.addWidget(self.repeater_edit)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_repeater)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.widget = QtWidgets.QWidget(self.tab_repeater)
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.tabWidget.addTab(self.tab_repeater, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.tabWidget.addTab(self.tab_settings, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1391, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_proxy_intercept), _translate("MainWindow", "Intercept"))
        self.proxy_history_table.setSortingEnabled(True)
        item = self.proxy_history_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.proxy_history_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Server Type"))
        item = self.proxy_history_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time"))
        item = self.proxy_history_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Packet Type"))
        item = self.proxy_history_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Grain"))
        item = self.proxy_history_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Connection #"))
        item = self.proxy_history_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Proxy Authority"))
        item = self.proxy_history_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Server Authority"))
        self.pushButton.setText(_translate("MainWindow", "Send to Repeater"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_proxy_history), _translate("MainWindow", "History"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_proxy), _translate("MainWindow", "Proxy"))
        self.pushButton_2.setText(_translate("MainWindow", "Send"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_repeater), _translate("MainWindow", "Repeater"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), _translate("MainWindow", "Settings"))

