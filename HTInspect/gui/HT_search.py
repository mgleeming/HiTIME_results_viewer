# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HT_search.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1143, 845)
        self.gridLayout_7 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_9.addWidget(self.label_9, 0, 0, 1, 1)
        self.RP_HT_input_field = QtWidgets.QLineEdit(self.tab_2)
        self.RP_HT_input_field.setObjectName("RP_HT_input_field")
        self.gridLayout_9.addWidget(self.RP_HT_input_field, 0, 1, 1, 1)
        self.RP_HT_input_button = QtWidgets.QPushButton(self.tab_2)
        self.RP_HT_input_button.setObjectName("RP_HT_input_button")
        self.gridLayout_9.addWidget(self.RP_HT_input_button, 0, 2, 1, 1)
        self.submit = QtWidgets.QPushButton(self.tab_2)
        self.submit.setObjectName("submit")
        self.gridLayout_9.addWidget(self.submit, 0, 3, 1, 1)
        self.horizontalLayout_15.addLayout(self.gridLayout_9)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RP_heat_map = PlotWidget(self.tab_2)
        self.RP_heat_map.setObjectName("RP_heat_map")
        self.verticalLayout_2.addWidget(self.RP_heat_map)
        self.horizontalLayout_19.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.RP_mzML_input_field = QtWidgets.QLineEdit(self.tab_2)
        self.RP_mzML_input_field.setObjectName("RP_mzML_input_field")
        self.horizontalLayout_4.addWidget(self.RP_mzML_input_field)
        self.RP_mascot_input_button = QtWidgets.QPushButton(self.tab_2)
        self.RP_mascot_input_button.setObjectName("RP_mascot_input_button")
        self.horizontalLayout_4.addWidget(self.RP_mascot_input_button)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.RP_mzDelta = QtWidgets.QLineEdit(self.tab_2)
        self.RP_mzDelta.setObjectName("RP_mzDelta")
        self.horizontalLayout.addWidget(self.RP_mzDelta)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.RP_EIC_width = QtWidgets.QLineEdit(self.tab_2)
        self.RP_EIC_width.setObjectName("RP_EIC_width")
        self.horizontalLayout_2.addWidget(self.RP_EIC_width)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.RP_min_intensity = QtWidgets.QLineEdit(self.tab_2)
        self.RP_min_intensity.setObjectName("RP_min_intensity")
        self.horizontalLayout_6.addWidget(self.RP_min_intensity)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_3.addWidget(self.label_19)
        self.RP_output_file_field = QtWidgets.QLineEdit(self.tab_2)
        self.RP_output_file_field.setObjectName("RP_output_file_field")
        self.horizontalLayout_3.addWidget(self.RP_output_file_field)
        self.RP_output_file_button = QtWidgets.QPushButton(self.tab_2)
        self.RP_output_file_button.setObjectName("RP_output_file_button")
        self.horizontalLayout_3.addWidget(self.RP_output_file_button)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.RP_run_button = QtWidgets.QPushButton(self.tab_2)
        self.RP_run_button.setObjectName("RP_run_button")
        self.horizontalLayout_7.addWidget(self.RP_run_button)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.tab_6)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.HT_RV_load_results = QtWidgets.QPushButton(self.widget)
        self.HT_RV_load_results.setObjectName("HT_RV_load_results")
        self.horizontalLayout_22.addWidget(self.HT_RV_load_results)
        self.RV_reset = QtWidgets.QPushButton(self.widget)
        self.RV_reset.setObjectName("RV_reset")
        self.horizontalLayout_22.addWidget(self.RV_reset)
        self.verticalLayout_5.addLayout(self.horizontalLayout_22)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_29 = QtWidgets.QLabel(self.widget)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_4.addWidget(self.label_29)
        self.HT_RV_hitlist = QtWidgets.QTableWidget(self.widget)
        self.HT_RV_hitlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.HT_RV_hitlist.setObjectName("HT_RV_hitlist")
        self.HT_RV_hitlist.setColumnCount(4)
        self.HT_RV_hitlist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.HT_RV_hitlist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.HT_RV_hitlist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.HT_RV_hitlist.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.HT_RV_hitlist.setHorizontalHeaderItem(3, item)
        self.verticalLayout_4.addWidget(self.HT_RV_hitlist)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.HT_RV_up = QtWidgets.QPushButton(self.widget)
        self.HT_RV_up.setObjectName("HT_RV_up")
        self.horizontalLayout_23.addWidget(self.HT_RV_up)
        self.HT_RV_down = QtWidgets.QPushButton(self.widget)
        self.HT_RV_down.setObjectName("HT_RV_down")
        self.horizontalLayout_23.addWidget(self.HT_RV_down)
        self.verticalLayout_4.addLayout(self.horizontalLayout_23)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_28 = QtWidgets.QLabel(self.widget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_3.addWidget(self.label_28)
        self.HT_RV_accepted_list = QtWidgets.QTableWidget(self.widget)
        self.HT_RV_accepted_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.HT_RV_accepted_list.setAlternatingRowColors(False)
        self.HT_RV_accepted_list.setObjectName("HT_RV_accepted_list")
        self.HT_RV_accepted_list.setColumnCount(4)
        self.HT_RV_accepted_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.HT_RV_accepted_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.HT_RV_accepted_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.HT_RV_accepted_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.HT_RV_accepted_list.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.HT_RV_accepted_list)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.HT_RV_remove = QtWidgets.QPushButton(self.widget)
        self.HT_RV_remove.setObjectName("HT_RV_remove")
        self.horizontalLayout_8.addWidget(self.HT_RV_remove)
        self.HT_RV_write = QtWidgets.QPushButton(self.widget)
        self.HT_RV_write.setObjectName("HT_RV_write")
        self.horizontalLayout_8.addWidget(self.HT_RV_write)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_21 = QtWidgets.QLabel(self.widget1)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_25.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.widget1)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_25.addWidget(self.label_22)
        self.verticalLayout_8.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.HT_RV_HM_widget = PlotWidget(self.widget1)
        self.HT_RV_HM_widget.setObjectName("HT_RV_HM_widget")
        self.horizontalLayout_26.addWidget(self.HT_RV_HM_widget)
        self.HT_RV_EIC = PlotWidget(self.widget1)
        self.HT_RV_EIC.setObjectName("HT_RV_EIC")
        self.horizontalLayout_26.addWidget(self.HT_RV_EIC)
        self.verticalLayout_8.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_23 = QtWidgets.QLabel(self.widget1)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_27.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.widget1)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_27.addWidget(self.label_24)
        self.verticalLayout_8.addLayout(self.horizontalLayout_27)
        self.HT_RV_MS = PlotWidget(self.widget1)
        self.HT_RV_MS.setObjectName("HT_RV_MS")
        self.verticalLayout_8.addWidget(self.HT_RV_MS)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.HT_RV_accept = QtWidgets.QPushButton(self.widget1)
        self.HT_RV_accept.setObjectName("HT_RV_accept")
        self.horizontalLayout_28.addWidget(self.HT_RV_accept)
        self.HT_RV_reject = QtWidgets.QPushButton(self.widget1)
        self.HT_RV_reject.setObjectName("HT_RV_reject")
        self.horizontalLayout_28.addWidget(self.HT_RV_reject)
        self.verticalLayout_8.addLayout(self.horizontalLayout_28)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_9.setText(_translate("Dialog", "HiTIME Output File"))
        self.RP_HT_input_button.setText(_translate("Dialog", "Browse"))
        self.submit.setText(_translate("Dialog", "Submit"))
        self.label_15.setText(_translate("Dialog", "mzML File"))
        self.RP_mascot_input_button.setText(_translate("Dialog", "Browse"))
        self.label_17.setText(_translate("Dialog", "mzDelta"))
        self.label_18.setText(_translate("Dialog", "EIC Width"))
        self.label_14.setText(_translate("Dialog", "Minimum Intensity"))
        self.label_19.setText(_translate("Dialog", "Output File"))
        self.RP_output_file_button.setText(_translate("Dialog", "Browse"))
        self.RP_run_button.setText(_translate("Dialog", "Run Postprocessing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Results Postprocessing"))
        self.HT_RV_load_results.setText(_translate("Dialog", "Load Results"))
        self.RV_reset.setText(_translate("Dialog", "Reset"))
        self.label_29.setText(_translate("Dialog", "All Hits"))
        item = self.HT_RV_hitlist.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Hit"))
        item = self.HT_RV_hitlist.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "RT"))
        item = self.HT_RV_hitlist.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "m/z"))
        item = self.HT_RV_hitlist.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Score"))
        self.HT_RV_up.setText(_translate("Dialog", "Up"))
        self.HT_RV_down.setText(_translate("Dialog", "Down"))
        self.label_28.setText(_translate("Dialog", "Accepted Hits"))
        item = self.HT_RV_accepted_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Hit"))
        item = self.HT_RV_accepted_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "RT"))
        item = self.HT_RV_accepted_list.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "m/z"))
        item = self.HT_RV_accepted_list.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Score"))
        self.HT_RV_remove.setText(_translate("Dialog", "Remove"))
        self.HT_RV_write.setText(_translate("Dialog", "Write Results to File"))
        self.label_21.setText(_translate("Dialog", "Heat Map"))
        self.label_22.setText(_translate("Dialog", "EIC"))
        self.label_23.setText(_translate("Dialog", "MS1 Spectrum"))
        self.HT_RV_accept.setText(_translate("Dialog", "Accept"))
        self.HT_RV_reject.setText(_translate("Dialog", "Reject"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Dialog", "Results Viewer"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

