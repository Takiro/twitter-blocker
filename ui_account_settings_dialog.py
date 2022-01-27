# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_settings_dialogwsgOpZ.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_settings_dialog(object):
    def setupUi(self, settings_dialog):
        if not settings_dialog.objectName():
            settings_dialog.setObjectName(u"settings_dialog")
        settings_dialog.setWindowModality(Qt.ApplicationModal)
        settings_dialog.resize(535, 200)
        settings_dialog.setMinimumSize(QSize(470, 200))
        self.verticalLayout_2 = QVBoxLayout(settings_dialog)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.label = QLabel(settings_dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.consumer_key_edit = QLineEdit(settings_dialog)
        self.consumer_key_edit.setObjectName(u"consumer_key_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.consumer_key_edit)

        self.label_2 = QLabel(settings_dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.consumer_secret_edit = QLineEdit(settings_dialog)
        self.consumer_secret_edit.setObjectName(u"consumer_secret_edit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.consumer_secret_edit)

        self.label_3 = QLabel(settings_dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.access_token_key_edit = QLineEdit(settings_dialog)
        self.access_token_key_edit.setObjectName(u"access_token_key_edit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.access_token_key_edit)

        self.label_4 = QLabel(settings_dialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.access_token_secret_edit = QLineEdit(settings_dialog)
        self.access_token_secret_edit.setObjectName(u"access_token_secret_edit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.access_token_secret_edit)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(settings_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(settings_dialog)
        self.buttonBox.accepted.connect(settings_dialog.accept)
        self.buttonBox.rejected.connect(settings_dialog.reject)

        QMetaObject.connectSlotsByName(settings_dialog)
    # setupUi

    def retranslateUi(self, settings_dialog):
        settings_dialog.setWindowTitle(QCoreApplication.translate("settings_dialog", u"Account Settings", None))
        self.label.setText(QCoreApplication.translate("settings_dialog", u"Consumer Key", None))
        self.label_2.setText(QCoreApplication.translate("settings_dialog", u"Consumer Secret", None))
        self.label_3.setText(QCoreApplication.translate("settings_dialog", u"Access Token Key", None))
        self.label_4.setText(QCoreApplication.translate("settings_dialog", u"Access Token Secret", None))
    # retranslateUi

