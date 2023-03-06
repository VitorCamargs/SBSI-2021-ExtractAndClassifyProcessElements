import sys
import os
import datetime

from ui_interface import Ui_MainWindow
from PySide2.QtCore import QPoint, QSize
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QFileDialog,
)
from PySide2.QtGui import QPixmap, QPainter, QPen

from Extrator import extrator
from PreClassify import pre_classify
from fileHandler import openfile, img_file


imagens = os.listdir('imagens')


class Interface(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(Interface, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Extractor and Classifier")
        self.df = None
        self.index = 0
        self.who = 'Vitor'
        # Buttons effects
        # First page
        self.button_extract_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_select_extract))
        self.button_classify_page.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_select_classify))
        # choose bpmn to extract
        self.button_browseBPMN.clicked.connect(self.browse_bpmn)
        self.button_extract.clicked.connect(self.extract)
        # choose csv to classify
        self.button_browseCSV.clicked.connect(self.browse_csv)
        self.button_classify.clicked.connect(self.classify)
        # filter page
        self.button_filter.clicked.connect(self.filter)
        # classify page
        self.button_next.clicked.connect(self.next)
        self.button_prev.clicked.connect(self.prev)
        self.button_save.clicked.connect(lambda: self.df.to_csv(self.text_filesCSV.text(), index=False))

    def browse_bpmn(self):
        fname = QFileDialog.getOpenFileNames(self, "Choose file", filter="BPMN Files,(*.bpmn)")
        self.text_filesBPMN.setText(str(fname[0])[1:-1])

    def extract(self):
        lista = self.text_filesBPMN.text().replace("'", "").split(",")
        extrator(lista, "")
        msg = QMessageBox()
        msg.setText('"Element_names.csv" with the extracted elements generated at application folder')
        msg.exec_()

    def browse_csv(self):
        fname = QFileDialog.getOpenFileName(self, "Choose file", filter="CSV Files,(*.csv)")
        self.text_filesCSV.setText(fname[0])

    def classify(self):
        if self.checkBox_filter.isChecked():
            self.stackedWidget.setCurrentWidget(self.page_filter)

        else:
            # call classificador
            self.df = openfile(self.text_filesCSV.text())
            if type(self.df) == str:
                msg = QMessageBox()
                msg.setText(self.df)
                msg.exec_()
            else:
                self.index = self.df[self.df["Classified"] == False].index[0]
                print(self.index)
                # futura funcao de pegar img e texto
                #################
                file_name, characteristic = img_file(self.df, self.index)
                canvas = QPixmap(file_name)
                # loop/parallel
                if characteristic != '':
                    p = QPainter(canvas)
                    p.drawPixmap(QPoint(92, 220), QPixmap('imagens/parallel.png').scaled(QSize(15, 15)))
                    p.end()
                self.img_label.setPixmap(canvas)
                self.text_element_name.clear()
                self.text_element_name.appendPlainText(self.df.at[self.index, 'Name'])
                print(self.index)
                ###################
                self.stackedWidget.setCurrentWidget(self.page_classify)
            pass

    def filter(self):
        excluir = []
        for i in range(self.verticalLayout_7.count()):
            checkb = self.verticalLayout_7.itemAt(i).widget()
            if checkb.isChecked():
                excluir.append(checkb.text())
        for i in range(self.verticalLayout_8.count()):
            checkb = self.verticalLayout_8.itemAt(i).widget()
            if checkb.isChecked():
                excluir.append(checkb.text())
        for i in range(self.verticalLayout_10.count()):
            checkb = self.verticalLayout_10.itemAt(i).widget()
            if checkb.isChecked():
                excluir.append(checkb.text())
        try:
            self.df = pre_classify(self.text_filesCSV.text(), 'saida.csv', excluir,
                                   self.checkBox_rmvNonEnglish.isChecked())
            self.get_img()
            self.stackedWidget.setCurrentWidget(self.page_classify)
        except Exception as e:
            print(e)
    def get_img(self):
        file_name, characteristic = img_file(self.df, self.index)
        canvas = QPixmap(file_name)
        # loop/parallel
        if characteristic != '':
            p = QPainter(canvas)
            p.drawPixmap(QPoint(92, 220), QPixmap(f'imagens/{characteristic}.png').scaled(QSize(15, 15)))
            p.end()
        self.img_label.setPixmap(canvas)
        self.text_element_name.clear()
        self.text_element_name.appendPlainText(self.df.at[self.index, 'Name'])

    def next(self):
        self.df.at[self.index, 'Classified'] = True
        self.df.at[self.index, 'Who_Classified'] = self.who
        self.df.at[self.index, 'timestamp'] = datetime.datetime.now()

        for i in range(self.horizontalLayout_21.count()):
            radio = self.horizontalLayout_21.itemAt(i).widget()
            if radio.isChecked():
                self.df.at[self.index, 'Process Participants'] = radio.objectName()[-1:]
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)

        for i in range(self.horizontalLayout_22.count()):
            radio = self.horizontalLayout_22.itemAt(i).widget()
            if radio.isChecked():
                self.df.at[self.index, 'System, tools, and technologies'] = radio.objectName()[-1:]
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)

        for i in range(self.horizontalLayout_23.count()):
            radio = self.horizontalLayout_23.itemAt(i).widget()
            if radio.isChecked():
                self.df.at[self.index, 'Processed documents and information'] = radio.objectName()[-1:]
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)

        self.index += 1
        self.get_img()

    def prev(self):
        self.df.at[self.index, 'Classified'] = True
        self.df.at[self.index, 'Who_Classified'] = self.who
        self.df.at[self.index, 'timestamp'] = datetime.datetime.now()

        for i in range(self.horizontalLayout_21.count()):
            radio = self.horizontalLayout_21.itemAt(i).widget()
            if radio.isChecked():
                self.df.at[self.index, 'Process Participants'] = radio.objectName()[-1:]
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
        print(self.df.at[self.index, 'Process Participants'])
        radio = self.horizontalLayout_21.itemAt(int(self.df.at[self.index - 1, 'Process Participants']) - 1).widget()
        radio.setAutoExclusive(False)
        radio.setChecked(True)
        radio.setAutoExclusive(True)

        for i in range(self.horizontalLayout_22.count()):
            radio = self.horizontalLayout_22.itemAt(i).widget()
            if radio.isChecked():
                self.df.at[self.index, 'System, tools, and technologies'] = radio.objectName()[-1:]
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
        radio = self.horizontalLayout_22.itemAt(
            int(self.df.at[self.index - 1, 'System, tools, and technologies']) - 1).widget()
        radio.setAutoExclusive(False)
        radio.setChecked(True)
        radio.setAutoExclusive(True)

        for i in range(self.horizontalLayout_23.count()):
            radio = self.horizontalLayout_23.itemAt(i).widget()
            if radio.isChecked():
                self.df.at[self.index, 'Processed documents and information'] = radio.objectName()[-1:]
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
        radio = self.horizontalLayout_23.itemAt(
            int(self.df.at[self.index - 1, 'Processed documents and information']) - 1).widget()
        radio.setAutoExclusive(False)
        radio.setChecked(True)
        radio.setAutoExclusive(True)
        self.index -= 1
        self.get_img()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Interface()

    window.show()
    app.exec_()
