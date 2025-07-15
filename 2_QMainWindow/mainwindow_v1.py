from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon

class MainWindow_1(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.resize(800, 600)
        
        # Set stylesheet with hover effects
        self.setStyleSheet("""
            QMainWindow {
                background-color: lightgray;
            }
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #888;
                padding: 5px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QToolButton {
                background-color: transparent;
                border: 1px solid transparent;
                padding: 3px;
            }
            QToolButton:hover {
                background-color: #d0d0d0;
                border: 1px solid #888;
            }
            QToolBar {
                background-color: #e0e0e0;
                border-bottom: 1px solid #ccc;
                spacing: 3px;
            }
            QMenuBar {
                background-color: #e0e0e0;
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 5px 10px;
            }
            QMenuBar::item:hover {
                background-color: #d0d0d0;
            }
        """)
        
        self.setWindowTitle("Custom Main Window")
        
        # Menu bar setup
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Exit", self.close)
        
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")
        
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

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction("About")
        
        # Toolbar setup
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)
        
        action1 = QAction("Some Action", self)
        action1.setStatusTip("This is some action")
        action1.triggered.connect(self.toolbar_button_clicked)
        toolbar.addAction(action1)
        
        action2 = QAction(QIcon(r"D:\2025\pyside6\2_QMainWindow\start_button.jpg"), "Some Other Action", self)
        action2.setStatusTip("This is some other action")
        action2.triggered.connect(self.toolbar_button_clicked)
        toolbar.addAction(action2)
        
        toolbar.addSeparator()
        
        # Custom button with hover effect
        custom_button = QPushButton("Custom Button")
        custom_button.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #888;
                padding: 3px 8px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
        """)
        toolbar.addWidget(custom_button)
        
        # Status bar
        status_bar = QStatusBar(self)
        self.setStatusBar(status_bar)
        
        # Central widget
        button1 = QPushButton("Click Me")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)
    
    def toolbar_button_clicked(self):
        print("Toolbar button clicked!")
        self.statusBar().showMessage("Toolbar button clicked!", 3000)
    
    def button1_clicked(self):
        print("Button 1 clicked!")
        self.statusBar().showMessage("Button 1 clicked!", 3000)