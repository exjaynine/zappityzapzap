import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QFileDialog)
from PyQt6.QtGui import QIcon, QAction

from pathlib import Path
import sys, glob, os

class PrimaryWindow(QMainWindow):
    """Everything about the primary initial window including menubar
    will go into this very class."""
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        #Menubar
        MenuBar = self.menuBar()
        FileMenu = MenuBar.addMenu('&File')
        EditMenu = MenuBar.addMenu('&Edit')
        SettingsMenu = MenuBar.addMenu('&Settings')
        HelpMenu = MenuBar.addMenu('&Help')


        #Lets open a file
        OpenFile = QAction('open', self)
        OpenFile.triggered.connect(self.FileGrab) #See function below

        FileMenu.addAction(OpenFile)

        #Now, lets give ability to terminate the application
        ByeBye = QAction('&Exit', self)
        
        #Add it as an option to the FileMenu
        FileMenu.addAction(ByeBye)

        #Almost forgot, have to have ByeBye actually do something
        ByeBye.triggered.connect(QApplication.instance().quit)

        
        self.setGeometry(800,600, 300, 450)
        self.setWindowTitle('zappityzapzap - A screenwriting program')

        self.show()

    def FileGrab(self):
        DEFAULTPATH = str(Path.home())
        FILE = QFileDialog.getOpenFileName(self, 'Open File', DEFAULTPATH)

        print(FILE[0]) #For now, it's fine just printing the full path.
        #Later, something will be done with the actual file.
        



def EntryPoint():
    Application = QApplication(sys.argv)
    M = PrimaryWindow()
    sys.exit(Application.exec())


if __name__ == '__main__':
    EntryPoint()

#End of file
    
