# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowfKTkey.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 502)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setMaximumSize(QSize(400, 600))
        self.actionAccount = QAction(MainWindow)
        self.actionAccount.setObjectName(u"actionAccount")
        self.action_account = QAction(MainWindow)
        self.action_account.setObjectName(u"action_account")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.user_profile_pic_label = QLabel(self.groupBox_2)
        self.user_profile_pic_label.setObjectName(u"user_profile_pic_label")
        self.user_profile_pic_label.setMinimumSize(QSize(100, 100))
        self.user_profile_pic_label.setMaximumSize(QSize(100, 100))
        self.user_profile_pic_label.setFrameShape(QFrame.Panel)
        self.user_profile_pic_label.setFrameShadow(QFrame.Sunken)
        self.user_profile_pic_label.setLineWidth(2)
        self.user_profile_pic_label.setMargin(5)

        self.horizontalLayout.addWidget(self.user_profile_pic_label, 0, Qt.AlignTop)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.user_screen_name_label = QLabel(self.groupBox_2)
        self.user_screen_name_label.setObjectName(u"user_screen_name_label")

        self.verticalLayout.addWidget(self.user_screen_name_label)

        self.user_display_name_label = QLabel(self.groupBox_2)
        self.user_display_name_label.setObjectName(u"user_display_name_label")

        self.verticalLayout.addWidget(self.user_display_name_label)

        self.user_block_count_label = QLabel(self.groupBox_2)
        self.user_block_count_label.setObjectName(u"user_block_count_label")
        self.user_block_count_label.setTextFormat(Qt.PlainText)

        self.verticalLayout.addWidget(self.user_block_count_label)

        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.vertical_spacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(0, 200))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.target_user_profile_pic_label = QLabel(self.groupBox)
        self.target_user_profile_pic_label.setObjectName(u"target_user_profile_pic_label")
        self.target_user_profile_pic_label.setMinimumSize(QSize(100, 100))
        self.target_user_profile_pic_label.setMaximumSize(QSize(100, 100))
        self.target_user_profile_pic_label.setLayoutDirection(Qt.LeftToRight)
        self.target_user_profile_pic_label.setFrameShape(QFrame.Panel)
        self.target_user_profile_pic_label.setFrameShadow(QFrame.Sunken)
        self.target_user_profile_pic_label.setLineWidth(2)
        self.target_user_profile_pic_label.setTextFormat(Qt.AutoText)
        self.target_user_profile_pic_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.target_user_profile_pic_label.setMargin(5)

        self.horizontalLayout_2.addWidget(self.target_user_profile_pic_label, 0, Qt.AlignTop)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.target_user_screen_name_input = QLineEdit(self.groupBox)
        self.target_user_screen_name_input.setObjectName(u"target_user_screen_name_input")
        self.target_user_screen_name_input.setInputMask(u"")

        self.horizontalLayout_3.addWidget(self.target_user_screen_name_input)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.target_user_display_name_label = QLabel(self.groupBox)
        self.target_user_display_name_label.setObjectName(u"target_user_display_name_label")

        self.verticalLayout_3.addWidget(self.target_user_display_name_label)

        self.target_user_stats_label = QLabel(self.groupBox)
        self.target_user_stats_label.setObjectName(u"target_user_stats_label")

        self.verticalLayout_3.addWidget(self.target_user_stats_label)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 80))
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 256, 85))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, -1, -1)
        self.target_user_description_label = QLabel(self.scrollAreaWidgetContents)
        self.target_user_description_label.setObjectName(u"target_user_description_label")
        sizePolicy1.setHeightForWidth(self.target_user_description_label.sizePolicy().hasHeightForWidth())
        self.target_user_description_label.setSizePolicy(sizePolicy1)
        self.target_user_description_label.setMinimumSize(QSize(0, 0))
        self.target_user_description_label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setStrikeOut(False)
        self.target_user_description_label.setFont(font)
        self.target_user_description_label.setTextFormat(Qt.AutoText)
        self.target_user_description_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.target_user_description_label.setWordWrap(True)
        self.target_user_description_label.setOpenExternalLinks(True)

        self.horizontalLayout_5.addWidget(self.target_user_description_label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.block_reason_input = QLineEdit(self.centralwidget)
        self.block_reason_input.setObjectName(u"block_reason_input")

        self.verticalLayout_2.addWidget(self.block_reason_input)

        self.block_user_button = QPushButton(self.centralwidget)
        self.block_user_button.setObjectName(u"block_user_button")

        self.verticalLayout_2.addWidget(self.block_user_button)

        self.continue_blocking_button = QPushButton(self.centralwidget)
        self.continue_blocking_button.setObjectName(u"continue_blocking_button")

        self.verticalLayout_2.addWidget(self.continue_blocking_button)

        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout_2.addWidget(self.status_label)

        self.progress_bar = QProgressBar(self.centralwidget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_2.addWidget(self.progress_bar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 19))
        self.menusettings = QMenu(self.menubar)
        self.menusettings.setObjectName(u"menusettings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menusettings.menuAction())
        self.menusettings.addAction(self.action_account)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Twitter Mass Blocker", None))
        self.actionAccount.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.action_account.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Your account", None))
        self.user_profile_pic_label.setText("")
        self.user_screen_name_label.setText(QCoreApplication.translate("MainWindow", u"Screen Name", None))
        self.user_display_name_label.setText(QCoreApplication.translate("MainWindow", u"Display Name", None))
        self.user_block_count_label.setText(QCoreApplication.translate("MainWindow", u"Block Count", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Account to block", None))
        self.target_user_profile_pic_label.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"@", None))
        self.target_user_screen_name_input.setText("")
        self.target_user_screen_name_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter target user's @name", None))
        self.target_user_display_name_label.setText("")
        self.target_user_stats_label.setText("")
        self.target_user_description_label.setText("")
        self.block_reason_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Reason for Blocking", None))
        self.block_user_button.setText(QCoreApplication.translate("MainWindow", u"Block user and their followers", None))
        self.continue_blocking_button.setText(QCoreApplication.translate("MainWindow", u"Continue blocking", None))
        self.status_label.setText("")
        self.menusettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

