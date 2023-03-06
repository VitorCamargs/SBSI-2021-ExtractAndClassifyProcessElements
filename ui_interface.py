# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'novo layout ic.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1141, 680)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(185, 185, 185);")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.page_select_extract = QWidget()
        self.page_select_extract.setObjectName(u"page_select_extract")
        self.verticalLayout_4 = QVBoxLayout(self.page_select_extract)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.page_select_extract)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.text_filesBPMN = QLineEdit(self.frame_2)
        self.text_filesBPMN.setObjectName(u"text_filesBPMN")
        self.text_filesBPMN.setMinimumSize(QSize(200, 0))
        self.text_filesBPMN.setFont(font)

        self.horizontalLayout_2.addWidget(self.text_filesBPMN)

        self.button_browseBPMN = QPushButton(self.frame_2)
        self.button_browseBPMN.setObjectName(u"button_browseBPMN")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_browseBPMN.sizePolicy().hasHeightForWidth())
        self.button_browseBPMN.setSizePolicy(sizePolicy1)
        self.button_browseBPMN.setMinimumSize(QSize(0, 40))
        self.button_browseBPMN.setFont(font)
        self.button_browseBPMN.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.horizontalLayout_2.addWidget(self.button_browseBPMN)

        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMaximumSize(QSize(16777215, 120))
        font1 = QFont()
        font1.setPointSize(4)
        self.frame_3.setFont(font1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(50, 10, 50, 0)
        self.button_extract = QPushButton(self.frame_3)
        self.button_extract.setObjectName(u"button_extract")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_extract.sizePolicy().hasHeightForWidth())
        self.button_extract.setSizePolicy(sizePolicy3)
        self.button_extract.setMinimumSize(QSize(0, 40))
        self.button_extract.setFont(font)
        self.button_extract.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.horizontalLayout_3.addWidget(self.button_extract)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 7)
        self.verticalLayout_3.setStretch(2, 1)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_select_extract)
        self.page_select_classify = QWidget()
        self.page_select_classify.setObjectName(u"page_select_classify")
        self.verticalLayout_6 = QVBoxLayout(self.page_select_classify)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.page_select_classify)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.verticalLayout_5.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(50, -1, 50, -1)
        self.text_filesCSV = QLineEdit(self.frame_4)
        self.text_filesCSV.setObjectName(u"text_filesCSV")
        self.text_filesCSV.setMinimumSize(QSize(200, 0))
        self.text_filesCSV.setFont(font)

        self.horizontalLayout_4.addWidget(self.text_filesCSV)

        self.button_browseCSV = QPushButton(self.frame_4)
        self.button_browseCSV.setObjectName(u"button_browseCSV")
        sizePolicy1.setHeightForWidth(self.button_browseCSV.sizePolicy().hasHeightForWidth())
        self.button_browseCSV.setSizePolicy(sizePolicy1)
        self.button_browseCSV.setMinimumSize(QSize(0, 40))
        self.button_browseCSV.setFont(font)
        self.button_browseCSV.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_browseCSV)

        self.horizontalLayout_4.setStretch(0, 7)
        self.horizontalLayout_4.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_filter = QCheckBox(self.frame_6)
        self.checkBox_filter.setObjectName(u"checkBox_filter")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_filter.sizePolicy().hasHeightForWidth())
        self.checkBox_filter.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setPointSize(12)
        self.checkBox_filter.setFont(font2)

        self.horizontalLayout_6.addWidget(self.checkBox_filter)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setMaximumSize(QSize(16777215, 120))
        self.frame_5.setFont(font1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(50, 10, 50, 0)
        self.button_classify = QPushButton(self.frame_5)
        self.button_classify.setObjectName(u"button_classify")
        sizePolicy3.setHeightForWidth(self.button_classify.sizePolicy().hasHeightForWidth())
        self.button_classify.setSizePolicy(sizePolicy3)
        self.button_classify.setMinimumSize(QSize(0, 40))
        self.button_classify.setFont(font)
        self.button_classify.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.horizontalLayout_5.addWidget(self.button_classify)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.verticalLayout_5.setStretch(0, 2)
        self.verticalLayout_5.setStretch(1, 5)
        self.verticalLayout_5.setStretch(2, 2)
        self.verticalLayout_5.setStretch(3, 1)

        self.verticalLayout_6.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_select_classify)
        self.page_filter = QWidget()
        self.page_filter.setObjectName(u"page_filter")
        self.verticalLayout_9 = QVBoxLayout(self.page_filter)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_11 = QFrame(self.page_filter)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_11)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_7.addWidget(self.label_3)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_12)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy5.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy5)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(25)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.checkBox_participant = QCheckBox(self.frame_7)
        self.checkBox_participant.setObjectName(u"checkBox_participant")
        font3 = QFont()
        font3.setPointSize(13)
        self.checkBox_participant.setFont(font3)

        self.verticalLayout_7.addWidget(self.checkBox_participant)

        self.checkBox_messageFlow = QCheckBox(self.frame_7)
        self.checkBox_messageFlow.setObjectName(u"checkBox_messageFlow")
        self.checkBox_messageFlow.setFont(font3)

        self.verticalLayout_7.addWidget(self.checkBox_messageFlow)

        self.checkBox_association = QCheckBox(self.frame_7)
        self.checkBox_association.setObjectName(u"checkBox_association")
        self.checkBox_association.setFont(font3)

        self.verticalLayout_7.addWidget(self.checkBox_association)

        self.checkBox_textAnnotation = QCheckBox(self.frame_7)
        self.checkBox_textAnnotation.setObjectName(u"checkBox_textAnnotation")
        self.checkBox_textAnnotation.setFont(font3)

        self.verticalLayout_7.addWidget(self.checkBox_textAnnotation)

        self.checkBox_exclusiveGateway = QCheckBox(self.frame_7)
        self.checkBox_exclusiveGateway.setObjectName(u"checkBox_exclusiveGateway")
        self.checkBox_exclusiveGateway.setFont(font3)

        self.verticalLayout_7.addWidget(self.checkBox_exclusiveGateway)

        self.checkBox_parallelGateway = QCheckBox(self.frame_7)
        self.checkBox_parallelGateway.setObjectName(u"checkBox_parallelGateway")
        self.checkBox_parallelGateway.setFont(font3)

        self.verticalLayout_7.addWidget(self.checkBox_parallelGateway)

        self.complexGateway = QCheckBox(self.frame_7)
        self.complexGateway.setObjectName(u"complexGateway")
        self.complexGateway.setFont(font3)

        self.verticalLayout_7.addWidget(self.complexGateway)

        self.checkBox_eventBasedGateway = QCheckBox(self.frame_7)
        self.checkBox_eventBasedGateway.setObjectName(u"checkBox_eventBasedGateway")
        self.checkBox_eventBasedGateway.setFont(font3)

        self.verticalLayout_7.addWidget(self.checkBox_eventBasedGateway)

        self.checkBox_inclusiveGateway = QCheckBox(self.frame_7)
        self.checkBox_inclusiveGateway.setObjectName(u"checkBox_inclusiveGateway")
        self.checkBox_inclusiveGateway.setFont(font3)

        self.verticalLayout_7.addWidget(self.checkBox_inclusiveGateway)

        self.checkBox_adHocSubProcess = QCheckBox(self.frame_7)
        self.checkBox_adHocSubProcess.setObjectName(u"checkBox_adHocSubProcess")
        self.checkBox_adHocSubProcess.setFont(font3)

        self.verticalLayout_7.addWidget(self.checkBox_adHocSubProcess)

        self.checkBox_task = QCheckBox(self.frame_7)
        self.checkBox_task.setObjectName(u"checkBox_task")
        self.checkBox_task.setFont(font3)

        self.verticalLayout_7.addWidget(self.checkBox_task)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.checkBox_dataObjectReference = QCheckBox(self.frame_7)
        self.checkBox_dataObjectReference.setObjectName(u"checkBox_dataObjectReference")
        self.checkBox_dataObjectReference.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkBox_dataObjectReference)

        self.checkBox_dataStoreReference = QCheckBox(self.frame_7)
        self.checkBox_dataStoreReference.setObjectName(u"checkBox_dataStoreReference")
        self.checkBox_dataStoreReference.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkBox_dataStoreReference)

        self.checkBox_boundaryEvent = QCheckBox(self.frame_7)
        self.checkBox_boundaryEvent.setObjectName(u"checkBox_boundaryEvent")
        self.checkBox_boundaryEvent.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkBox_boundaryEvent)

        self.checkBox_endEvent = QCheckBox(self.frame_7)
        self.checkBox_endEvent.setObjectName(u"checkBox_endEvent")
        self.checkBox_endEvent.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkBox_endEvent)

        self.checkBox_startEvent = QCheckBox(self.frame_7)
        self.checkBox_startEvent.setObjectName(u"checkBox_startEvent")
        self.checkBox_startEvent.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkBox_startEvent)

        self.checkBox_intermediateCatchEvent = QCheckBox(self.frame_7)
        self.checkBox_intermediateCatchEvent.setObjectName(u"checkBox_intermediateCatchEvent")
        self.checkBox_intermediateCatchEvent.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkBox_intermediateCatchEvent)

        self.checkBox_intermediateThrowEvent = QCheckBox(self.frame_7)
        self.checkBox_intermediateThrowEvent.setObjectName(u"checkBox_intermediateThrowEvent")
        self.checkBox_intermediateThrowEvent.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkBox_intermediateThrowEvent)

        self.checkBox_textAnnotation_2 = QCheckBox(self.frame_7)
        self.checkBox_textAnnotation_2.setObjectName(u"checkBox_textAnnotation_2")
        self.checkBox_textAnnotation_2.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkBox_textAnnotation_2)

        self.checkBox_collaboration = QCheckBox(self.frame_7)
        self.checkBox_collaboration.setObjectName(u"checkBox_collaboration")
        self.checkBox_collaboration.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkBox_collaboration)

        self.checkBox_lane = QCheckBox(self.frame_7)
        self.checkBox_lane.setObjectName(u"checkBox_lane")
        self.checkBox_lane.setFont(font3)

        self.verticalLayout_8.addWidget(self.checkBox_lane)


        self.horizontalLayout_8.addLayout(self.verticalLayout_8)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.checkBox_scriptTask = QCheckBox(self.frame_7)
        self.checkBox_scriptTask.setObjectName(u"checkBox_scriptTask")
        self.checkBox_scriptTask.setFont(font3)

        self.verticalLayout_10.addWidget(self.checkBox_scriptTask)

        self.checkBox_callActivity = QCheckBox(self.frame_7)
        self.checkBox_callActivity.setObjectName(u"checkBox_callActivity")
        self.checkBox_callActivity.setFont(font3)

        self.verticalLayout_10.addWidget(self.checkBox_callActivity)

        self.checkBox_subProcess = QCheckBox(self.frame_7)
        self.checkBox_subProcess.setObjectName(u"checkBox_subProcess")
        self.checkBox_subProcess.setFont(font3)

        self.verticalLayout_10.addWidget(self.checkBox_subProcess)

        self.checkBox_transaction = QCheckBox(self.frame_7)
        self.checkBox_transaction.setObjectName(u"checkBox_transaction")
        self.checkBox_transaction.setFont(font3)

        self.verticalLayout_10.addWidget(self.checkBox_transaction)

        self.checkBox_sendTask = QCheckBox(self.frame_7)
        self.checkBox_sendTask.setObjectName(u"checkBox_sendTask")
        self.checkBox_sendTask.setFont(font3)

        self.verticalLayout_10.addWidget(self.checkBox_sendTask)

        self.checkBox_receiveTask = QCheckBox(self.frame_7)
        self.checkBox_receiveTask.setObjectName(u"checkBox_receiveTask")
        self.checkBox_receiveTask.setFont(font3)

        self.verticalLayout_10.addWidget(self.checkBox_receiveTask)

        self.checkBox_userTask = QCheckBox(self.frame_7)
        self.checkBox_userTask.setObjectName(u"checkBox_userTask")
        self.checkBox_userTask.setFont(font3)

        self.verticalLayout_10.addWidget(self.checkBox_userTask)

        self.checkBox_manualTask = QCheckBox(self.frame_7)
        self.checkBox_manualTask.setObjectName(u"checkBox_manualTask")
        self.checkBox_manualTask.setFont(font3)

        self.verticalLayout_10.addWidget(self.checkBox_manualTask)

        self.checkBox_businessRuleTask = QCheckBox(self.frame_7)
        self.checkBox_businessRuleTask.setObjectName(u"checkBox_businessRuleTask")
        self.checkBox_businessRuleTask.setFont(font3)

        self.verticalLayout_10.addWidget(self.checkBox_businessRuleTask)

        self.checkBox_serviceTask = QCheckBox(self.frame_7)
        self.checkBox_serviceTask.setObjectName(u"checkBox_serviceTask")
        self.checkBox_serviceTask.setFont(font3)

        self.verticalLayout_10.addWidget(self.checkBox_serviceTask)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)


        self.horizontalLayout_11.addWidget(self.frame_7)


        self.verticalLayout_11.addWidget(self.frame_12)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 12)

        self.verticalLayout_9.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.page_filter)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBox_rmvNonEnglish = QCheckBox(self.frame_10)
        self.checkBox_rmvNonEnglish.setObjectName(u"checkBox_rmvNonEnglish")
        sizePolicy4.setHeightForWidth(self.checkBox_rmvNonEnglish.sizePolicy().hasHeightForWidth())
        self.checkBox_rmvNonEnglish.setSizePolicy(sizePolicy4)
        self.checkBox_rmvNonEnglish.setFont(font2)

        self.horizontalLayout_9.addWidget(self.checkBox_rmvNonEnglish)


        self.verticalLayout_9.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.page_filter)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.button_filter = QPushButton(self.frame_9)
        self.button_filter.setObjectName(u"button_filter")
        sizePolicy3.setHeightForWidth(self.button_filter.sizePolicy().hasHeightForWidth())
        self.button_filter.setSizePolicy(sizePolicy3)
        self.button_filter.setMinimumSize(QSize(0, 40))
        self.button_filter.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.horizontalLayout_10.addWidget(self.button_filter)


        self.verticalLayout_9.addWidget(self.frame_9)

        self.verticalLayout_9.setStretch(0, 8)
        self.verticalLayout_9.setStretch(2, 1)
        self.stackedWidget.addWidget(self.page_filter)
        self.page_classify = QWidget()
        self.page_classify.setObjectName(u"page_classify")
        self.horizontalLayout_39 = QHBoxLayout(self.page_classify)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.frame_29 = QFrame(self.page_classify)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_28 = QFrame(self.frame_29)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(320, 461))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_28)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.img_label = QLabel(self.frame_28)
        self.img_label.setObjectName(u"img_label")
        self.img_label.setFrameShape(QFrame.Panel)
        self.img_label.setPixmap(QPixmap(u":/user/imagens/userTask.png"))

        self.verticalLayout_20.addWidget(self.img_label)

        self.text_element_name = QPlainTextEdit(self.frame_28)
        self.text_element_name.setObjectName(u"text_element_name")
        self.text_element_name.setEnabled(True)
        self.text_element_name.setFont(font2)
        self.text_element_name.setReadOnly(True)

        self.verticalLayout_20.addWidget(self.text_element_name)

        self.verticalLayout_20.setStretch(0, 8)
        self.verticalLayout_20.setStretch(1, 2)

        self.verticalLayout_21.addLayout(self.verticalLayout_20)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(12)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.button_prev = QPushButton(self.frame_28)
        self.button_prev.setObjectName(u"button_prev")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.button_prev.sizePolicy().hasHeightForWidth())
        self.button_prev.setSizePolicy(sizePolicy6)
        self.button_prev.setMinimumSize(QSize(40, 40))
        self.button_prev.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.horizontalLayout_29.addWidget(self.button_prev)

        self.button_next = QPushButton(self.frame_28)
        self.button_next.setObjectName(u"button_next")
        sizePolicy6.setHeightForWidth(self.button_next.sizePolicy().hasHeightForWidth())
        self.button_next.setSizePolicy(sizePolicy6)
        self.button_next.setMinimumSize(QSize(40, 40))
        self.button_next.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.horizontalLayout_29.addWidget(self.button_next)


        self.horizontalLayout_31.addLayout(self.horizontalLayout_29)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_16 = QLabel(self.frame_28)
        self.label_16.setObjectName(u"label_16")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy7)
        self.label_16.setFont(font2)

        self.verticalLayout_19.addWidget(self.label_16)

        self.text_element_count = QLabel(self.frame_28)
        self.text_element_count.setObjectName(u"text_element_count")
        font4 = QFont()
        font4.setPointSize(11)
        self.text_element_count.setFont(font4)

        self.verticalLayout_19.addWidget(self.text_element_count)


        self.horizontalLayout_31.addLayout(self.verticalLayout_19)

        self.horizontalLayout_31.setStretch(0, 2)
        self.horizontalLayout_31.setStretch(1, 3)

        self.verticalLayout_21.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.button_save = QPushButton(self.frame_28)
        self.button_save.setObjectName(u"button_save")
        sizePolicy3.setHeightForWidth(self.button_save.sizePolicy().hasHeightForWidth())
        self.button_save.setSizePolicy(sizePolicy3)
        self.button_save.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.horizontalLayout_30.addWidget(self.button_save)

        self.button_stop = QPushButton(self.frame_28)
        self.button_stop.setObjectName(u"button_stop")
        sizePolicy3.setHeightForWidth(self.button_stop.sizePolicy().hasHeightForWidth())
        self.button_stop.setSizePolicy(sizePolicy3)
        self.button_stop.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.horizontalLayout_30.addWidget(self.button_stop)


        self.verticalLayout_21.addLayout(self.horizontalLayout_30)

        self.verticalLayout_21.setStretch(0, 5)
        self.verticalLayout_21.setStretch(1, 1)
        self.verticalLayout_21.setStretch(2, 1)

        self.horizontalLayout_38.addWidget(self.frame_28)

        self.frame_27 = QFrame(self.frame_29)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(911, 461))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_25 = QFrame(self.frame_27)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_17 = QLabel(self.frame_25)
        self.label_17.setObjectName(u"label_17")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy8)

        self.horizontalLayout_28.addWidget(self.label_17)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_7 = QLabel(self.frame_25)
        self.label_7.setObjectName(u"label_7")
        sizePolicy8.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy8)

        self.horizontalLayout_24.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_25)
        self.label_8.setObjectName(u"label_8")
        sizePolicy8.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy8)

        self.horizontalLayout_24.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_25)
        self.label_9.setObjectName(u"label_9")
        sizePolicy8.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy8)

        self.horizontalLayout_24.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_25)
        self.label_10.setObjectName(u"label_10")
        sizePolicy8.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy8)

        self.horizontalLayout_24.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_25)
        self.label_11.setObjectName(u"label_11")
        sizePolicy8.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy8)

        self.horizontalLayout_24.addWidget(self.label_11)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_28.setStretch(0, 2)
        self.horizontalLayout_28.setStretch(1, 8)

        self.horizontalLayout_35.addLayout(self.horizontalLayout_28)


        self.verticalLayout_18.addWidget(self.frame_25)

        self.frame_23 = QFrame(self.frame_27)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_13 = QLabel(self.frame_23)
        self.label_13.setObjectName(u"label_13")
        sizePolicy8.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy8)
        self.label_13.setMinimumSize(QSize(154, 0))
        self.label_13.setFont(font2)

        self.horizontalLayout_25.addWidget(self.label_13)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(65)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(60, -1, -1, -1)
        self.radio_pp1 = QRadioButton(self.frame_23)
        self.radio_pp1.setObjectName(u"radio_pp1")
        self.radio_pp1.setAutoExclusive(True)

        self.horizontalLayout_21.addWidget(self.radio_pp1)

        self.radio_pp2 = QRadioButton(self.frame_23)
        self.radio_pp2.setObjectName(u"radio_pp2")
        self.radio_pp2.setAutoExclusive(True)

        self.horizontalLayout_21.addWidget(self.radio_pp2)

        self.radio_pp3 = QRadioButton(self.frame_23)
        self.radio_pp3.setObjectName(u"radio_pp3")
        self.radio_pp3.setAutoRepeat(False)
        self.radio_pp3.setAutoExclusive(True)

        self.horizontalLayout_21.addWidget(self.radio_pp3)

        self.radio_pp4 = QRadioButton(self.frame_23)
        self.radio_pp4.setObjectName(u"radio_pp4")
        self.radio_pp4.setAutoExclusive(True)

        self.horizontalLayout_21.addWidget(self.radio_pp4)

        self.radio_pp5 = QRadioButton(self.frame_23)
        self.radio_pp5.setObjectName(u"radio_pp5")
        self.radio_pp5.setIconSize(QSize(30, 30))
        self.radio_pp5.setAutoExclusive(True)

        self.horizontalLayout_21.addWidget(self.radio_pp5)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_25.setStretch(0, 2)
        self.horizontalLayout_25.setStretch(1, 8)

        self.horizontalLayout_34.addLayout(self.horizontalLayout_25)


        self.verticalLayout_18.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_27)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_14 = QLabel(self.frame_24)
        self.label_14.setObjectName(u"label_14")
        sizePolicy8.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy8)
        self.label_14.setMinimumSize(QSize(154, 0))
        self.label_14.setFont(font2)

        self.horizontalLayout_26.addWidget(self.label_14)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(65)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(60, -1, -1, -1)
        self.radio_stt1 = QRadioButton(self.frame_24)
        self.radio_stt1.setObjectName(u"radio_stt1")

        self.horizontalLayout_22.addWidget(self.radio_stt1)

        self.radio_stt2 = QRadioButton(self.frame_24)
        self.radio_stt2.setObjectName(u"radio_stt2")

        self.horizontalLayout_22.addWidget(self.radio_stt2)

        self.radio_stt3 = QRadioButton(self.frame_24)
        self.radio_stt3.setObjectName(u"radio_stt3")

        self.horizontalLayout_22.addWidget(self.radio_stt3)

        self.radio_stt4 = QRadioButton(self.frame_24)
        self.radio_stt4.setObjectName(u"radio_stt4")

        self.horizontalLayout_22.addWidget(self.radio_stt4)

        self.radio_stt5 = QRadioButton(self.frame_24)
        self.radio_stt5.setObjectName(u"radio_stt5")
        self.radio_stt5.setIconSize(QSize(30, 30))

        self.horizontalLayout_22.addWidget(self.radio_stt5)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_26.setStretch(0, 2)
        self.horizontalLayout_26.setStretch(1, 8)

        self.horizontalLayout_33.addLayout(self.horizontalLayout_26)


        self.verticalLayout_18.addWidget(self.frame_24)

        self.frame_26 = QFrame(self.frame_27)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_15 = QLabel(self.frame_26)
        self.label_15.setObjectName(u"label_15")
        sizePolicy8.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy8)
        self.label_15.setFont(font2)

        self.horizontalLayout_27.addWidget(self.label_15)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(65)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(60, -1, -1, -1)
        self.radio_pdi1 = QRadioButton(self.frame_26)
        self.radio_pdi1.setObjectName(u"radio_pdi1")

        self.horizontalLayout_23.addWidget(self.radio_pdi1)

        self.radio_pdi2 = QRadioButton(self.frame_26)
        self.radio_pdi2.setObjectName(u"radio_pdi2")

        self.horizontalLayout_23.addWidget(self.radio_pdi2)

        self.radio_pdi3 = QRadioButton(self.frame_26)
        self.radio_pdi3.setObjectName(u"radio_pdi3")

        self.horizontalLayout_23.addWidget(self.radio_pdi3)

        self.radio_pdi4 = QRadioButton(self.frame_26)
        self.radio_pdi4.setObjectName(u"radio_pdi4")

        self.horizontalLayout_23.addWidget(self.radio_pdi4)

        self.radio_pdi5 = QRadioButton(self.frame_26)
        self.radio_pdi5.setObjectName(u"radio_pdi5")
        self.radio_pdi5.setIconSize(QSize(30, 30))

        self.horizontalLayout_23.addWidget(self.radio_pdi5)


        self.horizontalLayout_27.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_27.setStretch(0, 2)
        self.horizontalLayout_27.setStretch(1, 8)

        self.horizontalLayout_32.addLayout(self.horizontalLayout_27)


        self.verticalLayout_18.addWidget(self.frame_26)


        self.horizontalLayout_36.addLayout(self.verticalLayout_18)


        self.horizontalLayout_38.addWidget(self.frame_27)


        self.horizontalLayout_39.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.page_classify)
        self.page_first = QWidget()
        self.page_first.setObjectName(u"page_first")
        self.horizontalLayout = QHBoxLayout(self.page_first)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.page_first)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(700, 600))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(150)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.button_extract_page = QPushButton(self.frame)
        self.button_extract_page.setObjectName(u"button_extract_page")
        sizePolicy3.setHeightForWidth(self.button_extract_page.sizePolicy().hasHeightForWidth())
        self.button_extract_page.setSizePolicy(sizePolicy3)
        self.button_extract_page.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setKerning(True)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.button_extract_page.setFont(font5)
        self.button_extract_page.setLayoutDirection(Qt.LeftToRight)
        self.button_extract_page.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.verticalLayout_2.addWidget(self.button_extract_page)

        self.button_classify_page = QPushButton(self.frame)
        self.button_classify_page.setObjectName(u"button_classify_page")
        sizePolicy3.setHeightForWidth(self.button_classify_page.sizePolicy().hasHeightForWidth())
        self.button_classify_page.setSizePolicy(sizePolicy3)
        self.button_classify_page.setFont(font)
        self.button_classify_page.setStyleSheet(u"QPushButton{\n"
"	Border: 2px solid rgb(37,39,48);\n"
"	Border-radius: 20px;\n"
"	background-color: rgb(103, 115, 125);\n"
"}\n"
"QPushButton:hover{\n"
"	Border: 2px solid rgb(50,50,48);\n"
"	background-color: rgb(116, 134, 144);\n"
"}\n"
"QPushButton:pressed{\n"
"	Border: 2px solid rgb(255, 255, 255);\n"
"	background-color: rgb(80, 100, 125);\n"
"}")

        self.verticalLayout_2.addWidget(self.button_classify_page)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_first)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Chose files .bpmn to be extracted</span></p></body></html>", None))
        self.button_browseBPMN.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.button_extract.setText(QCoreApplication.translate("MainWindow", u"Extract Elements", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Select .csv with the elements to be classified</span></p></body></html>", None))
        self.button_browseCSV.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.checkBox_filter.setText(QCoreApplication.translate("MainWindow", u"Pre filter Elements", None))
        self.button_classify.setText(QCoreApplication.translate("MainWindow", u"Classify Elements", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Elements types to Remove</span></p></body></html>", None))
        self.checkBox_participant.setText(QCoreApplication.translate("MainWindow", u"participant", None))
        self.checkBox_messageFlow.setText(QCoreApplication.translate("MainWindow", u"messageFlow", None))
        self.checkBox_association.setText(QCoreApplication.translate("MainWindow", u"association", None))
        self.checkBox_textAnnotation.setText(QCoreApplication.translate("MainWindow", u"textAnnotation", None))
        self.checkBox_exclusiveGateway.setText(QCoreApplication.translate("MainWindow", u"exclusiveGateway", None))
        self.checkBox_parallelGateway.setText(QCoreApplication.translate("MainWindow", u"parallelGateway", None))
        self.complexGateway.setText(QCoreApplication.translate("MainWindow", u"complexGateway", None))
        self.checkBox_eventBasedGateway.setText(QCoreApplication.translate("MainWindow", u"eventBasedGateway", None))
        self.checkBox_inclusiveGateway.setText(QCoreApplication.translate("MainWindow", u"inclusiveGateway", None))
        self.checkBox_adHocSubProcess.setText(QCoreApplication.translate("MainWindow", u"adHocSubProcess", None))
        self.checkBox_task.setText(QCoreApplication.translate("MainWindow", u"task", None))
        self.checkBox_dataObjectReference.setText(QCoreApplication.translate("MainWindow", u"dataObjectReference", None))
        self.checkBox_dataStoreReference.setText(QCoreApplication.translate("MainWindow", u"dataStoreReference", None))
        self.checkBox_boundaryEvent.setText(QCoreApplication.translate("MainWindow", u"boundaryEvent", None))
        self.checkBox_endEvent.setText(QCoreApplication.translate("MainWindow", u"endEvent", None))
        self.checkBox_startEvent.setText(QCoreApplication.translate("MainWindow", u"startEvent", None))
        self.checkBox_intermediateCatchEvent.setText(QCoreApplication.translate("MainWindow", u"intermediateCatchEvent", None))
        self.checkBox_intermediateThrowEvent.setText(QCoreApplication.translate("MainWindow", u"intermediateThrowEvent", None))
        self.checkBox_textAnnotation_2.setText(QCoreApplication.translate("MainWindow", u"textAnnotation", None))
        self.checkBox_collaboration.setText(QCoreApplication.translate("MainWindow", u"collaboration", None))
        self.checkBox_lane.setText(QCoreApplication.translate("MainWindow", u"lane", None))
        self.checkBox_scriptTask.setText(QCoreApplication.translate("MainWindow", u"scriptTask", None))
        self.checkBox_callActivity.setText(QCoreApplication.translate("MainWindow", u"callActivity", None))
        self.checkBox_subProcess.setText(QCoreApplication.translate("MainWindow", u"subProcess", None))
        self.checkBox_transaction.setText(QCoreApplication.translate("MainWindow", u"transaction", None))
        self.checkBox_sendTask.setText(QCoreApplication.translate("MainWindow", u"sendTask", None))
        self.checkBox_receiveTask.setText(QCoreApplication.translate("MainWindow", u"receiveTask", None))
        self.checkBox_userTask.setText(QCoreApplication.translate("MainWindow", u"userTask", None))
        self.checkBox_manualTask.setText(QCoreApplication.translate("MainWindow", u"manualTask", None))
        self.checkBox_businessRuleTask.setText(QCoreApplication.translate("MainWindow", u"businessRuleTask", None))
        self.checkBox_serviceTask.setText(QCoreApplication.translate("MainWindow", u"serviceTask", None))
        self.checkBox_rmvNonEnglish.setText(QCoreApplication.translate("MainWindow", u"Remove Non-English (Google translate)", None))
        self.button_filter.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.img_label.setText("")
        self.button_prev.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.button_next.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Classifyed elements:</span></p></body></html>", None))
        self.text_element_count.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.button_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_17.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Strongly</span></p><p align=\"center\"><span style=\" font-size:12pt;\">disagree</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Disagree</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Neutral</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Agree</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Strongly</span></p><p align=\"center\"><span style=\" font-size:12pt;\">agree</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Process</p><p align=\"center\"> Participant</p></body></html>", None))
        self.radio_pp1.setText("")
        self.radio_pp2.setText("")
        self.radio_pp3.setText("")
        self.radio_pp4.setText("")
        self.radio_pp5.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">System, tools and</p><p align=\"center\"> technologies</p></body></html>", None))
        self.radio_stt1.setText("")
        self.radio_stt2.setText("")
        self.radio_stt3.setText("")
        self.radio_stt4.setText("")
        self.radio_stt5.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Processed Documents</p><p align=\"center\"> and information</p></body></html>", None))
        self.radio_pdi1.setText("")
        self.radio_pdi2.setText("")
        self.radio_pdi3.setText("")
        self.radio_pdi4.setText("")
        self.radio_pdi5.setText("")
        self.button_extract_page.setText(QCoreApplication.translate("MainWindow", u"Extract Elements From .bpmn file", None))
        self.button_classify_page.setText(QCoreApplication.translate("MainWindow", u"Classify Extracted Elements", None))
    # retranslateUi

