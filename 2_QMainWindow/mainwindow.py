from PySide6.QtWidgets import QMainWindow,QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import Qt 
from PySide6.QtCore import QSize #Qsize is used for setting the window size
from PySide6.QtGui import QAction, QIcon
# This file is part of the PySide6 examples.
class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app
        self.resize(800, 600)
        self.setStyleSheet("background-color: lightgray;")
        self.setWindowTitle("Custom Main Window")
        
        # Menu bar setup can be done here
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action= file_menu.addAction("Exit", self.close)
        # quit_action.triggered.connect(self.quit_app)
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        # add more actions as needed
        window_menu = menu_bar.addMenu("Window")
        window_menu.addAction("Minimize", self.showMinimized)
        window_menu.addAction("Maximize", self.showMaximized)
        window_menu.addAction("Restore", self.showNormal)
        window_menu.addAction("Close", self.close)
        
        setting_menu = menu_bar.addMenu("Settings")
        setting_menu.addAction("Preferences")
        setting_menu.addAction("Options")
        setting_menu.addAction("Configure")
        setting_menu.addAction("Customize")
        setting_menu.addAction("Reset to Default")
        setting_menu.addAction("Advanced Settings")

        # Help menu setup
        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction("About")
        
        # working with toolbars
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))  # Set icon size for
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)
        # toolbar.addAction("New")
        
        # Adding a button to the toolbar
        action1 = QAction("Some Action", self)
        action1.setStatusTip("This is some action")
        action1.triggered.connect(self.toolbar_button_clicked)
        toolbar.addAction(action1)
        
        # You can add more actions to the toolbar as needed
        action2 = QAction(QIcon(r"D:\2025\pyside6\2_QMainWindow\start_button.jpg"), "Some Other Action", self)
        action2.setStatusTip("This is some other action")
        action2.triggered.connect(self.toolbar_button_clicked)
        # action2.setCheckable(True)
        toolbar.addAction(action2)
        
        # Adding a custom button to the toolbar
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Custom Button"))
        
        # Working with status bar
        status_bar = QStatusBar(self)
        self.setStatusBar(status_bar)
        
        button1 = QPushButton("Click Me")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)
        
    # def quit_app(self):
    #     self.app.quit()
    
    def toolbar_button_clicked(self):
        print("Toolbar button clicked!")
        # You can add more functionality here
        self.statusBar().showMessage("Toolbar button clicked!", 3000)  # Show message in status bar for 3 seconds
    
    def button1_clicked(self):
        print("Button 1 clicked!")
        # You can add more functionality here
        self.statusBar().showMessage("Button 1 clicked!", 3000)