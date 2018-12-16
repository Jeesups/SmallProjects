import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit,QPushButton,QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Kalkulator(QWidget):
        def __init__(self, parent=None):
                super().__init__(parent)

                self.liczba1Edt = QLineEdit()
                self.liczba2Edt = QLineEdit()
                self.wynikEdt = QLineEdit()
                self.wynikEdt.readonly = True
                self.wynikEdt.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')



                self.interfejs()



        def interfejs(self):
                #self.resize(300,100)
                uklad = QGridLayout()
                ukladH = QHBoxLayout()
                self.setLayout(uklad)
                self.setGeometry(20,20,300,100)
                self.setWindowTitle("Super Kalkulator")
                #Etykiety
                etykieta1 = QLabel("Liczba 1:",self)
                etykieta2 = QLabel("Liczba 2:",self)
                etykieta3 = QLabel("Wynik:",self)
                #Przyciski
                dodajBtn = QPushButton("&Dodaj",self)
                odejmijBtn = QPushButton("&Odejmij",self)
                dzielBtn = QPushButton("&Dziel",self)
                mnozBtn = QPushButton("&Mnoz",self)
                pierwBtn = QPushButton("&Pierwiastkuj", self)
                koniecBtn = QPushButton("&Koniec",self)
                procentBtn = QPushButton("&Procent", self)
                odwBtn = QPushButton("&Odwrotna",self)
                sqrBtn = QPushButton("&Kwadrat",self)
                
                koniecBtn.resize(koniecBtn.sizeHint())

                #Uklad H
                ukladH.addWidget(dodajBtn)
                ukladH.addWidget(odejmijBtn)
                ukladH.addWidget(dzielBtn)
                ukladH.addWidget(mnozBtn)
                ukladH.addWidget(pierwBtn)


                uklad.addWidget(etykieta1,0,0)
                uklad.addWidget(etykieta2,0,1)
                uklad.addWidget(etykieta3,0,2)
                uklad.addWidget(self.liczba1Edt,1,0)
                uklad.addWidget(self.liczba2Edt,1,1)
                uklad.addWidget(self.wynikEdt,1,2)

                uklad.addLayout(ukladH,2,0,1,3)
                uklad.addWidget(koniecBtn,3,0,1,3)

                #Eventy
                koniecBtn.clicked.connect(self.koniec)
                dodajBtn.clicked.connect(self.dzialanie)
                odejmijBtn.clicked.connect(self.dzialanie)
                mnozBtn.clicked.connect(self.dzialanie)
                dzielBtn.clicked.connect(self.dzialanie)
                pierwBtn.clicked.connect(self.dzialanie)
                procentBtn.clicked.connect(self.dzialanie)
                odwBtn.clicked.connect(self.dzialanie)
                sqrBtn.clicked.connect(self.dzialanie)


                self.show()

        def koniec(self):
                self.close()
        def keyPressEvent(self,e):
                if e.key() == Qt.Key_Escape:
                        self.close()

        def closeEvent(self,event):
                odp = QMessageBox.question(self,'Komunikat',"Czy napewno koniec?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if odp == QMessageBox.Yes:
                        event.accept()
                else:
                        event.ignore()

        def dzialanie(self):
                nadawca = self.sender()
                try:
                        if(nadawca.text() == "&Pierwiastkuj"):
                                liczba1 = float(self.liczba1Edt.text())
                                try:
                                        wynik = str(math.sqrt(liczba1))
                                        
                                except ValueError:
                                        QMessageBox.critical(self,"Błąd!","Nie można uzyskać pierwiastka z liczby mniejszej od 0!")
                                        
                        if(nadawca.text())
                        else:
                                liczba1 = float(self.liczba1Edt.text())
                                liczba2 = float(self.liczba2Edt.text())
                                wynik = 0
                                if nadawca.text() == "&Dodaj":
                                        wynik = liczba1 + liczba2
                                elif nadawca.text() == "&Odejmij":
                                        wynik = liczba1 - liczba2
                                elif nadawca.text() == "&Mnoz":
                                        wynik = liczba1 * liczba2

                                elif nadawca.text() == "&Dziel":
                                        try:
                                                wynik = round(liczba1/liczba2,9)
                                        except ZeroDivisionError:
                                                QMessageBox.critical(self,"Błąd", "Nie można dzielić przez zero!")
                                                return
                                        
                        self.wynikEdt.setText(str(wynik))
                except ValueError:
                        QMessageBox.warning(self,"Błąd","Błędne dane", QMessageBox.Ok)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        okno = Kalkulator()
        sys.exit(app.exec_())