import sys
import os
import datetime

from ui_interface import Ui_MainWindow
from PySide2.QtCore import QPoint, QSize, Qt
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QFileDialog,
    QShortcut
)
from PySide2.QtGui import QPixmap, QPainter, QPen, QKeySequence

from Extractor import extractor
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
        self.who = ''
        self.text_saida = ''
        # Buttons effects
        # First page
        self.button_extract_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_select_extract))
        self.button_classify_page.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_select_classify))
        # choose bpmn to extract
        self.Button_voltar_bpmn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_first))
        self.button_browseBPMN.clicked.connect(self.browse_bpmn)
        self.button_extract.clicked.connect(self.extract)
        # choose csv to classify
        self.Button_voltar_csv.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_first))
        self.button_browseCSV.clicked.connect(self.browse_csv)
        self.button_classify.clicked.connect(self.classify)
        # filter page
        self.Button_voltar_filter.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_first))
        self.button_filter.clicked.connect(self.filter)
        # classify page
        self.button_next.clicked.connect(lambda: self.change_element(1))
        self.button_prev.clicked.connect(lambda: self.change_element(-1))
        self.button_save.clicked.connect(lambda: self.df.to_csv(self.text_saida, index=False))
        self.button_stop.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_first))
        self.button_prev.setDisabled(True)
        self.button_next.setDisabled(True)
        self.whoClassify.textChanged.connect(self.disable)

        QShortcut(QKeySequence("left"), self.button_prev, lambda: self.change_element(-1))
        QShortcut(QKeySequence("right"), self.button_next, lambda: self.change_element(1))
    def disable(self):
        """
        Disable Next and Prev Buttons until a classifier name is given
        :return:
        """
        self.who = self.whoClassify.text()
        if self.whoClassify.text() == '':
            self.button_prev.setDisabled(True)
            self.button_next.setDisabled(True)
        else:
            self.button_prev.setEnabled(True)
            self.button_next.setEnabled(True)



    def browse_bpmn(self):
        """
        Open a browse window that accepts multiple .bpmn files.
        The selected files are displayed at the filesBPMN label as a list, but in a string format
        :return:
        """
        fname = QFileDialog.getOpenFileNames(self, "Choose file", filter="BPMN Files,(*.bpmn)")
        self.text_filesBPMN.setText(str(fname[0])[1:-1])

    def extract(self):
        """
        calls the outer function extractor from Extractor. The extractor function receives the files names already
        split in a list, makes the elements' extraction of each of then and compile all these data into a file called
        'Elements_Names.csv' located at the application folder
        :return:
        """
        lista = self.text_filesBPMN.text().replace("'", "").split(",")
        saida = QFileDialog.getSaveFileName(self, 'Save output as', '', filter='CSV File,(*.csv)')
        print(saida)
        extractor(lista, saida[0])
        msg = QMessageBox()
        msg.setText(f'Extraction concluded at {saida[0]}')
        msg.exec_()
        self.stackedWidget.setCurrentWidget(self.page_first)


    def browse_csv(self):
        """
        Open a browse window that accepts only a .csv file.
        The selected file is displayed at the filesCSV label
        :return:
        """
        fname = QFileDialog.getOpenFileName(self, "Choose file", filter="CSV Files,(*.csv)")
        self.text_filesCSV.setText(fname[0])

    def classify(self):
        """
        In case of the filter checkbox are checked the interface is set to the filter page. If the file already
        passed through the filter (and it is unchecked) the outer function openfile is called, with the text present
        in filesCSV label as parameter. In case of error in opening the file the function returns a str with the
        error message, in case of success, the function returns a Pandas dataframe. the initial index is set to the
        firs non-classified element, and it's corresponding img and name are displayed in the interface
        :return:
        """
        if self.checkBox_filter.isChecked():
            self.stackedWidget.setCurrentWidget(self.page_filter)

        else:
            self.text_saida = self.text_filesCSV.text()
            self.df = openfile(self.text_filesCSV.text())
            if type(self.df) == str:
                msg = QMessageBox()
                msg.setText(self.df)
                msg.exec_()
            else:
                self.index = self.df[self.df["Classified"] == False].index[0]
                self.get_img()
                self.stackedWidget.setCurrentWidget(self.page_classify)
            pass

    def filter(self):
        """
        Get all the non-desired elements in a list that is passed as parameter for the outer function pre_classify
        from PreClassify.py. These function returns the passed dataframe reformatted to the manual classifier format
        (e.g. includes the "Classified" column) and without the selected elements. If the Remove Non-English checkbox
        is marked it also remove elements where the Name label wasn't detected as english by the Google Translate
        api. It also redirects to the classification page with the firs element already displayed

        :return:
        """
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

        saida = QFileDialog.getSaveFileName(self, 'Save output as', os.path.dirname(os.path.abspath(__file__)), filter='CSV File,(*.csv)')
        try:
            self.text_saida = saida[0]
            pre_classify(self.text_filesCSV.text(), saida[0], excluir,
                                       self.checkBox_rmvNonEnglish.isChecked())
            self.df = openfile(saida[0])
            if type(self.df) == str:
                msg = QMessageBox()
                msg.setText(self.df)
                msg.exec_()
            else:
                self.index = 0
                self.get_img()
                self.stackedWidget.setCurrentWidget(self.page_classify)

        except Exception as e:
            print(e)

    def get_img(self):
        """
        call the outer function img_file from fileHandler.py to handle the image file name and characteristic (e.g.
        loop, parallel) based on the elements data present in the datagram. Once the file names are handled the img
        is displayed and the name label updated.
        :return:
        """
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
        self.text_element_count.setText(f"{self.index+1}/{self.df.shape[0]}")

    def get_radio(self, layout, category, direction):
        """
        Receives the layout where the radio buttons are grouped and its respective category (Process Participants,
        System, tools, and technologies, Processed documents and information). The value correspondent to the selected
        radio is registered in the dataframe at the correspondent column.
        In case of navigating trough already classified elements this function can recover the value and autocheck the
        correct radio button automatically
        :param layout:
        :param category:
        :param  direction:
        :return:
        """
        for i in range(layout.count()):
            radio = layout.itemAt(i).widget()
            if radio.isChecked():
                self.df.at[self.index, category] = radio.objectName()[-1:]
                radio.setAutoExclusive(False)
                radio.setChecked(False)
                radio.setAutoExclusive(True)
        if self.index + direction in range(self.df.shape[0]) and self.df.at[self.index + direction, 'Classified']:
            if type(self.df.at[self.index + direction, category]) == str:
                radio = layout.itemAt(int(self.df.at[self.index + direction, category]) - 1).widget()
                radio.setAutoExclusive(False)
                radio.setChecked(True)
                radio.setAutoExclusive(True)
            if self.df.at[self.index + direction, 'Language_error']:
                self.check_error.setChecked(True)
            if self.df.at[self.index + direction, 'Orthography_error']:
                self.checkBox.setChecked(True)
            if self.df.at[self.index + direction, 'Others_error']:
                self.checkBox_2.setChecked(True)

    def change_element(self, direction):
        """
        Saves the classification of the actual element in the dataframe and navigate through the other elements
        according to the direction parameter. It is also check if the index is in the range of the dataframe shape,
        warning if already reach the last element.

        :param direction:
        :return:
        """

        if self.check_error.isChecked():
            self.check_error.setChecked(False)
            self.df.at[self.index,'Language_error'] = True
        else:
            self.df.at[self.index, 'Language_error'] = False

        if self.checkBox.isChecked():
            self.checkBox.setChecked(False)
            self.df.at[self.index,'Orthography_error'] = True
        else:
            self.df.at[self.index, 'Orthography_error'] = False

        if self.checkBox_2.isChecked():
            self.checkBox_2.setChecked(False)
            self.df.at[self.index,'Others_error'] = True
        else:
            self.df.at[self.index, 'Others_error'] = False

        self.df.at[self.index, 'Classified'] = True
        self.df.at[self.index, 'Who_Classified'] = self.who
        self.df.at[self.index, 'timestamp'] = datetime.datetime.now()

        self.get_radio(self.horizontalLayout_21, 'Process Participants', direction)
        self.get_radio(self.horizontalLayout_22, 'System, tools, and technologies', direction)
        self.get_radio(self.horizontalLayout_23, 'Processed documents and information', direction)
        self.text_element_count.setText(f"{self.index}/{self.df.shape[0]}")

        if self.index + direction in range(self.df.shape[0]):
            self.index += direction
            self.get_img()
        else:
            if self.index > self.df.shape[0]-2:
                msg = QMessageBox()
                msg.setText('End of File, please save before close the app')
                msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Interface()

    window.show()
    app.exec_()
