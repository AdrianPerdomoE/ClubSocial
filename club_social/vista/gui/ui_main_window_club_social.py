# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_club_socialuZzrBE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1028, 535)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_banner = QLabel(self.centralwidget)
        self.label_banner.setObjectName(u"label_banner")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_banner.sizePolicy().hasHeightForWidth())
        self.label_banner.setSizePolicy(sizePolicy)
        self.label_banner.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.label_banner.setPixmap(QPixmap(u"img/banner_club.jpg"))

        self.verticalLayout.addWidget(self.label_banner)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listview_socios = QListView(self.groupBox)
        self.listview_socios.setObjectName(u"listview_socios")

        self.verticalLayout_3.addWidget(self.listview_socios)

        self.pbutton_afiliar_socio = QPushButton(self.groupBox)
        self.pbutton_afiliar_socio.setObjectName(u"pbutton_afiliar_socio")

        self.verticalLayout_3.addWidget(self.pbutton_afiliar_socio)


        self.horizontalLayout.addWidget(self.groupBox)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 0, 2, -1)
        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineedit_cedula = QLineEdit(self.groupBox_2)
        self.lineedit_cedula.setObjectName(u"lineedit_cedula")
        self.lineedit_cedula.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineedit_cedula)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineedit_nombre = QLineEdit(self.groupBox_2)
        self.lineedit_nombre.setObjectName(u"lineedit_nombre")
        self.lineedit_nombre.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineedit_nombre)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.pbutton_registrar_consumo = QPushButton(self.frame_3)
        self.pbutton_registrar_consumo.setObjectName(u"pbutton_registrar_consumo")

        self.verticalLayout_4.addWidget(self.pbutton_registrar_consumo)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.listview_facturas = QListView(self.groupBox_3)
        self.listview_facturas.setObjectName(u"listview_facturas")

        self.verticalLayout_5.addWidget(self.listview_facturas)

        self.pbutton_pagar_factura = QPushButton(self.groupBox_3)
        self.pbutton_pagar_factura.setObjectName(u"pbutton_pagar_factura")

        self.verticalLayout_5.addWidget(self.pbutton_pagar_factura)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.listwidget_autorizados = QListWidget(self.groupBox_4)
        self.listwidget_autorizados.setObjectName(u"listwidget_autorizados")

        self.verticalLayout_6.addWidget(self.listwidget_autorizados)

        self.pbutton_agregar_autorizado = QPushButton(self.groupBox_4)
        self.pbutton_agregar_autorizado.setObjectName(u"pbutton_agregar_autorizado")

        self.verticalLayout_6.addWidget(self.pbutton_agregar_autorizado)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_banner.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Lista de socios", None))
        self.pbutton_afiliar_socio.setText(QCoreApplication.translate("MainWindow", u"Afiliar socio", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Datos del socio", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"C\u00e9dula:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.pbutton_registrar_consumo.setText(QCoreApplication.translate("MainWindow", u"Registrar consumo", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Facturas pendientes", None))
        self.pbutton_pagar_factura.setText(QCoreApplication.translate("MainWindow", u"Pagar factura", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Lista de autorizados", None))
        self.pbutton_agregar_autorizado.setText(QCoreApplication.translate("MainWindow", u"Agregar autorizado", None))
    # retranslateUi

