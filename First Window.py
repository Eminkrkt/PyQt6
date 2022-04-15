# We include the library
from PyQt6.QtWidgets import QApplication,QWidget
import sys

# We create the main window object 
class Main_Win (QWidget):
    def __init__(self):
        super().__init__()
        # Variable is important - - - > self 


# Next we create an instance of QApplication
app = QApplication(sys.argv)
# Next we create an instance of a QWidget
win = Main_Win()
# Show the QWidget
win.show()
# Finally we call app.exec() to start up the event loop
app.exec()