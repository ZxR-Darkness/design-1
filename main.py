import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from dsa import Ui_MainWindow

class Login(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # use the Ui_MainWindow
        self.ui = Ui_MainWindow()       
        self.ui.setupUi(self)       

        
        self.btn1.clicked.connect(self.his)
        
        
        self.show()
    
    def his(self):
        print("test")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())