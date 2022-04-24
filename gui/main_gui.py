from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QGridLayout, \
    QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox, QComboBox, QCheckBox, \
    QRadioButton, QGroupBox, QButtonGroup, QSpinBox, QSlider, QProgressBar, QTabWidget, \
    QTableWidget, QTableWidgetItem, QListWidget, QListWidgetItem, QListView, QInputDialog
# create a class for our main window
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        # call the init function of QWidget
        super().__init__()
        # set the title of the window
        self.setWindowTitle("PyQt5 GUI")
        # set the size of the window
        self.resize(1000, 600)
        # call our first method
        self.first_button()
        self.input_box()

    # create a button on the center that prints "Hello World"
    def first_button(self):
        btn = QPushButton("Click Me", self)
        btn.move(300, 300)
        btn.clicked.connect(self.click_me)
        # make the button 2x bigger
        btn.resize(btn.sizeHint() * 2)

    def click_me(self):
        print("Hello World!")

    # create an input box in the center of the window
    def input_box(self):
        # create a line edit widget
        line_edit = QLineEdit(self)
        # set its position
        line_edit.move(300, 400)
        # set its placeholder text
        line_edit.setPlaceholderText("Enter your name here")
        # set its callback function
        line_edit.textChanged.connect(self.text_changed)

    def text_changed(self, text):
        print(text)

    # create an instance of QApplication


app = QApplication(sys.argv)
# create an instance of our class
gui = MainWindow()
# show the window
gui.show()
# execute the app
sys.exit(app.exec_())
