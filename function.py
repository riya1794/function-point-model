from PyQt4 import QtGui  
import sys  
import fp_model 
import math 
import os  


class FPApplication(QtGui.QMainWindow, fp_model.Ui_MainWindow): 
    def __init__(self):
        super(self.__class__, self).__init__()
        self.a = self.b = self.c = self.d = self.e = self.degree_influence = 0
        self.setupUi(self)  
        self.radioButton.toggled.connect(self.radioButton_clicked)
        self.radioButton_2.toggled.connect(self.radioButton_2_clicked)
        self.radioButton_3.toggled.connect(self.radioButton_3_clicked) 
                                 
    def radioButton_clicked(self, enabled):
        if enabled:
            self.a = 3
            self.b = 4
            self.c = 3
            self.d = 7
            self.e = 5
            self.display()

    def radioButton_2_clicked(self, enabled):
        if enabled:
            self.a = 4
            self.b = 5
            self.c = 4
            self.d = 10
            self.e = 7
            self.display()      	
        	
    def radioButton_3_clicked(self, enabled):
        if enabled:
            self.a = 6
            self.b = 7
            self.c = 6
            self.d = 15
            self.e = 10
            self.display()

    def display(self):
        n_inp = long(self.textEdit.toPlainText())
        n_out = long(self.textEdit_2.toPlainText())
        n_inq = long(self.textEdit_3.toPlainText())
        n_log = long(self.textEdit_4.toPlainText())
        n_ext = long(self.textEdit_5.toPlainText())
        self.degree_influence = long(self.textEdit_6.toPlainText())
        UAF = self.a * n_inp + self.b * n_out + self.c * n_inq + self.d * n_log + self.e * n_ext
        CAF = 0.65 + (0.01*self.degree_influence)
        FP = UAF + CAF
        self.label_6.setText(str(FP))
       	self.label_6.setStyleSheet('color: red') 
        
def main():
    app = QtGui.QApplication(sys.argv)  
    model = FPApplication()  
    model.show()  
    sys.exit(app.exec_())  


if __name__ == '__main__':  
    main()  