#####################################################
##  Plantilla para importar de Qt Designer a Maya  ##
##            Kames Andrade edit 1.0               ##
#####################################################

try:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
    from shiboken2 import wrapInstance
except:
    from PySide.QtGui import *
    from PySide.QtCore import * 
    from shiboken import wrapInstance

import os
import maya.cmds as cmds
import maya.OpenMayaUI as omui

from PySide2 import QtWidgets as QtWidgets
from PySide2 import QtCore as QtCore
from PySide2 import QtGui as QtGui

def getMayaWindow():
    ptr = omui.MQtUtil.mainWindow()
    if ptr:
        return wrapInstance(long(ptr),QMainWindow)
    
    
#### Cambia el nombre de la funcion por el nombre personalizado en:
#### win = NombrePersonalizado
####def run():
    ### global win 
    ### win = NombrePersonalizado (parent=getMayaWindow())
    ### win.show()
    
def run():
    global win 
    win = CAMBIA_ESTE_NOMBRE_PERSONALIZADO (parent=getMayaWindow())
    win.show()

#### Cambia la clase como la tienes en el ejemplo
     ##### Dentro del ejemplo de clase cambia el nombre de la clase: 
     ##### Class NombrePersonalizado (QDialog) y despues de super: super (NombrePersonalizado, self.__init.__(parent))

class CAMBIA_ESTE_NOMBRE_PERSONALIZADO(QDialog):
    def __init__(self, parent =None):
        super (CAMBIA_ESTE_NOMBRE_PERSONALIZADO , self).__init__(parent)

#### Copia aqui toda la clase del convertidor de QT sin la clase
#### Reemplaza los MainWindow. por self.
#### >>>>>>>>>>>>












###### <<<<<<<<<<<<<     
#### Comentar estas funciones para desactivarlas
    #### self.SetCentralWidget
    #### self.retranslateUI
    #### self.tabWidget
    #### QtCore.QmetaObject
    #### def retranslateUi
    #### import ..nombredelUi...

#### No olvides poner un self.show() entre la ultima linea de self. y el import pero dentro de la clase;
####    self.pushButton_DefBody.setText(QtWidgets.QApplication.translate("MainWindow", "Deform Body", None, -1))

####    self.show()

#### import ....

############### En maya usar este codigo para llamar a la funcion:

'''import nombredecarpeta.nombredearchivo as ventana

reload (ventana)
w = ventana.run()'''

#### fin de la funcion

if __name__=='__main__':
    run()