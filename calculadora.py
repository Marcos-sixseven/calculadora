# Calculadora PyQt6 – Diseño Moderno + Corrección de errores

```python
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

        self.setWindowTitle("Calculadora Neon")
        self.setGeometry(100, 100, 380, 500)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Pantalla
        self.pantalla = QLineEdit()
        self.pantalla.setFont(QFont("Consolas", 24))
        self.pantalla.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.pantalla.setFixedHeight(70)
        self.pantalla.setReadOnly(False)

        self.layout.addWidget(self.pantalla, 0, 0, 1, 5)

        botones = [
            'C', '(', ')', '/', 'sqrt',
            '7', '8', '9', '*', '^',
            '4', '5', '6', '-', 'log',
            '1', '2', '3', '+', 'sin',
            '0', '.', '=', 'cos', 'tan'
        ]

        fila = 1
        col = 0

        for texto in botones:
            boton = QPushButton(texto)
            boton.setFont(QFont("Arial", 13, QFont.Weight.Bold))
            boton.setFixedSize(65, 65)
            boton.clicked.connect(self.click_boton)

            # Colores distintos
            if texto == "=":
                boton.setStyleSheet("""
                    QPushButton {
                        background-color: #00c853;
                        color: white;
                        border-radius: 15px;
                    }
                    QPushButton:hover {
                        background-color: #00e676;
                    }
                """)

            elif texto in ['+', '-', '*', '/', '^']:
                boton.setStyleSheet("""
                    QPushButton {
                        background-color: #ff9100;
                        color: white;
                        border-radius: 15px;
                    }
                    QPushButton:hover {
                        background-color: #ffab40;
                    }
                """)

            elif texto in ['sin', 'cos', 'tan', 'log', 'sqrt']:
                boton.setStyleSheet("""
                    QPushButton {
                        background-color: #2979ff;
                        color: white;
                        border-radius: 15px;
                    }
                    QPushButton:hover {
                        background-color: #5393ff;
                    }
                """)

            else:
                boton.setStyleSheet("""
                    QPushButton {
                        background-color: #1f1f1f;
                        color: white;
                        border-radius: 15px;
                        border: 1px solid #333;
                    }
                    QPushButton:hover {
                        background-color: #333333;
                    }
                """)

            self.layout.addWidget(boton, fila, col)

            col += 1
            if col > 4:
                col = 0
                fila += 1

        self.setStyleSheet("""
            QWidget {
                background-color: #0f0f0f;
            }

            QLineEdit {
                background-color: #151515;
                color: #00ffcc;
                border: 2px solid #00ffcc;
                border-radius: 15px;
                padding: 10px;
            }
        """)

    def keyPressEvent(self, event):
        tecla = event.text()

        if tecla in "0123456789+-*/().":
            self.pantalla.setText(self.pantalla.text() + tecla)

        elif event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
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
            expresion = self.pantalla.text()
            resultado = eval(expresion)
            self.pantalla.setText(str(resultado))

        except Exception:
            self.pantalla.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())
