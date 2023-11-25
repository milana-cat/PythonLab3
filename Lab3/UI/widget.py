import sys
from typing import Optional
import PySide6.QtCore
sys.path.append('../library/')

from PySide6.QtWidgets import QWidget,QMessageBox,QTableWidgetItem
from library.calc import *
from UI.inputHandler import *
from UI.outputHandler import *
from UI.ui_function_calc import Ui_MainWindow

class Widget(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Function calculus")

        self.Calculate.clicked.connect(self.calculate)
    
    def calculate(self):
        #print(self.SpinBoxA.value())
        parameters = [float(self.SpinBoxA.value()),
                      float(self.SpinBoxB.value()),
                      float(self.SpinBoxH.value()),
                      float(self.SpinBoxK.value()),]
        check = CheckParameters(parameters)
        
        if check == "":
            Widget.HandleOutputWidget(parameters,LinearList(parameters),self)
            #LinearList(parameters)
        else:
            self.msgbox = QMessageBox(self)
            self.msgbox.setWindowTitle("Error")
            self.msgbox.setText(check)
    
        
    def HandleOutputWidget(inputParameters:[],functionResult:[],self):
        leftBorder = inputParameters[0]
        rightBorder = inputParameters[1]
        step = inputParameters[2]
        #self.tableWidget.insertColumn(0)
        #self.tableWidget.insertColumn(1)
        #self.tableWidget.insertColumn(2)
        self.tableWidget.setColumnCount(3)
        
        for i in np.arange(leftBorder,rightBorder+step,step):
            
            currentRowCount =self.tableWidget.rowCount() #necessary even when there are no rows in the table
            #self.tableWidget.insertRow(currentRowCount, 0, QTableWidgetItem(str(counter)))
            #d=self.tableWidget.columnCount()
            Widget.add_row(self,currentRowCount,i,functionResult[currentRowCount])
            currentRowCount =+1
            
    
    def add_row(self,counter,xValue,functionResult):
        #rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(counter)      
        #self.tableWidget.setRowCount(rowPosition)
        self.tableWidget.setItem(counter,0,QTableWidgetItem(str(counter)))
        self.tableWidget.setItem(counter,1,QTableWidgetItem(str(xValue)))
        self.tableWidget.setItem(counter,2,QTableWidgetItem(str(functionResult)))