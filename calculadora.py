import sys
import math
from PyQt6.QtWidgets import (
    QApplication, QWidget, QGridLayout,
    QPushButton, QLineEdit
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora PRO")
        self.setGeometry(100, 100, 360, 450)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        self.pantalla = QLineEdit()
        self.pantalla.setFont(QFont("Arial", 20))
        self.pantalla.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.pantalla.setFixedHeight(50)
        self.layout.addWidget(self.pantalla, 0, 0, 1, 5)

        botones = [
            '7','8','9','/','sqrt',
            '4','5','6','*','^',
            '1','2','3','-','log',
            '0','.','=','+','sin',
            'C','(',')','cos','tan'
        ]

        fila, col = 1, 0

        for boton in botones:
            btn = QPushButton(boton)
            btn.setFont(QFont("Arial", 12))
            btn.setFixedHeight(50)
            btn.clicked.connect(self.click_boton)

            self.layout.addWidget(btn, fila, col)

            col += 1
            if col > 4:
                col = 0
                fila += 1

        self.set_dark_mode()
    def set_dark_mode(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
            }
            QLineEdit {
                background-color: #1e1e1e;
                color: white;
                border: 2px solid #333;
                padding: 5px;
            }
            QPushButton {
                background-color: #2b2b2b;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #3c3c3c;
            }
        """)
    def keyPressEvent(self, event):
        tecla = event.text()

        if tecla in "0123456789+-*/().":
            self.pantalla.setText(self.pantalla.text() + tecla)
        elif event.key() == Qt.Key.Key_Return:
            self.calcular()
        elif event.key() == Qt.Key.Key_Backspace:
            self.pantalla.setText(self.pantalla.text()[:-1])

    def click_boton(self):
        boton = self.sender().text()

        if boton == "=":
            self.calcular()
        elif boton == "C":
            self.pantalla.clear()
        elif boton == "sqrt":
            self.pantalla.setText(self.pantalla.text() + "math.sqrt(")
        elif boton == "sin":
            self.pantalla.setText(self.pantalla.text() + "math.sin(")
        elif boton == "cos":
            self.pantalla.setText(self.pantalla.text() + "math.cos(")
        elif boton == "tan":
            self.pantalla.setText(self.pantalla.text() + "math.tan(")
        elif boton == "log":
            self.pantalla.setText(self.pantalla.text() + "math.log10(")
        elif boton == "^":
            self.pantalla.setText(self.pantalla.text() + "**")
        else:
            self.pantalla.setText(self.pantalla.text() + boton)
    def calcular(self):
        try:
            resultado = eval(self.pantalla.text())
            self.pantalla.setText(str(resultado))
        except:
            self.pantalla.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())
