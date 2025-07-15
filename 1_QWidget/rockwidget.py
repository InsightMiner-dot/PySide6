from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class RockWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Rock Widget")
        self.resize(400, 300)
        self.setStyleSheet("background-color: lightblue;")
        
        # Create buttons
        button1 = QPushButton("Left", self)
        button2 = QPushButton("Right", self)
        button3 = QPushButton("Top", self)
        button4 = QPushButton("Down", self)
        
        # Connect button clicks to their respective functions
        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)
        button3.clicked.connect(self.button3_clicked)
        button4.clicked.connect(self.button4_clicked)
        
        # Create a horizontal layout for first two buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        
        # Create a vertical layout for the other buttons
        buttonv_layout = QVBoxLayout()
        buttonv_layout.addWidget(button3)
        buttonv_layout.addWidget(button4)
        
        # Add the vertical layout to the horizontal layout
        button_layout.addLayout(buttonv_layout)
        
        # Set the combined layout as the main layout
        self.setLayout(button_layout)
    
    # Class methods for button clicks
    def button1_clicked(self):
        print("Left button clicked!")
        
    def button2_clicked(self):
        print("Right Button clicked!")
        
    def button3_clicked(self):
        print("Top Button clicked!")
        
    def button4_clicked(self):
        print("Down Button clicked!")