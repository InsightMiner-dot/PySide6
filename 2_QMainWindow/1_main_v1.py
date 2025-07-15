from PySide6.QtWidgets import QApplication
from mainwindow_v1 import MainWindow_1
import sys

app = QApplication(sys.argv)
window = MainWindow_1(app)
window.show()
app.exec()