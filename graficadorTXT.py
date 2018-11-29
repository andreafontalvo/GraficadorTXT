#   Interfaz de pruebas UI V0.0
#   Proyecto: SANA
#   Escrito por: Andrea Fontalvo
#   Noviembre 2018

"""
       Este script permite:
       * cargar señal desde TXT y visualizarla
       * plotear señal de prueba
       * Limpiar pantalla
"""

from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtGui  # (the example applies equally well to PySide)
import pyqtgraph as pg
import numpy as np
import serial
import serial.tools.list_ports # Para revisar archivos conectados

# ---------------------LAYOUT------------------------
## Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

# Define a top-level widget to hold everything
w = QtGui.QWidget()

## Create some widgets to be placed inside
Button1 = QtGui.QPushButton('Cargar txt')
Button2 = QtGui.QPushButton('Test plot')
Button3 = QtGui.QPushButton('Limpiar')
Text    = QtGui.QLineEdit('enter text')
Listw   = QtGui.QListWidget()
Plt     = pg.PlotWidget()                       # to add a new set of data to an existing plot widget

## Create a grid layout to manage the widgets size and position
layout = QtGui.QGridLayout()
w.setLayout(layout)

## Add widgets to the layout in their proper positions
layout.addWidget(Button1, 0, 0)                 # button goes in upper-left
layout.addWidget(Button2, 1, 0)                 # button goes in upper-left
layout.addWidget(Button3, 2, 0)                 # button goes in upper-left
layout.addWidget(Plt, 0, 1, 4, 1)               # plot goes on right side, spanning 3 rows


# ---------------------FUNCIONES---------------------
def getdata(): 
        testplot()

def testplot():
    Plt.clear()
    DATOS = np.random.normal(size=(300))
    y_DATOS = np.linspace(0,len(DATOS),len(DATOS))
    print(type(y_DATOS))
    print(type(DATOS))
    Plt.plot(y_DATOS,DATOS)
#     pg.plot(y_DATOS,DATOS)

def graficartxt():
    Plt.clear()
    with open('DATAEMG.txt') as f:
        lines = f.readlines()
        x_emg = [float(line.split()[0]) for line in lines]
        y_emg = [float(line.split()[1]) for line in lines]
        x = np.array(x_emg)
        y = np.array(y_emg)
        Plt.plot(x,y)

def clearplot():
    Plt.clear()

def openFile():    
        filename = QtGui.QFileDialog.getOpenFileName(None)
        if filename:
                print(filename[0])
                ruta = str(filename[0])
                with open(ruta) as f:
                        lines = f.readlines()
                        x_emg = [float(line.split()[0]) for line in lines]
                        y_emg = [float(line.split()[1]) for line in lines]
                        x = np.array(x_emg)
                        y = np.array(y_emg)
                        Plt.plot(x,y)
# ---------------------------------------------------


Button1.clicked.connect(openFile)
Button2.clicked.connect(getdata)
Button3.clicked.connect(clearplot)

## Display the widget as a new window
w.show()

## Start the Qt event loop
app.exec_()