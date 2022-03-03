# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewswidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ViewsWidget(object):
    def setupUi(self, ViewsWidget):
        if not ViewsWidget.objectName():
            ViewsWidget.setObjectName(u"ViewsWidget")
        ViewsWidget.resize(523, 338)
        self.gridLayout = QGridLayout(ViewsWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBoxAnnotation = QComboBox(ViewsWidget)
        self.comboBoxAnnotation.addItem("")
        self.comboBoxAnnotation.setObjectName(u"comboBoxAnnotation")
        self.comboBoxAnnotation.setEditable(True)

        self.gridLayout.addWidget(self.comboBoxAnnotation, 2, 3, 1, 1)

        self.labelSample = QLabel(ViewsWidget)
        self.labelSample.setObjectName(u"labelSample")

        self.gridLayout.addWidget(self.labelSample, 4, 1, 1, 1)

        self.labelPath = QLabel(ViewsWidget)
        self.labelPath.setObjectName(u"labelPath")

        self.gridLayout.addWidget(self.labelPath, 0, 1, 1, 1)

        self.lineEditThumbnail = QLineEdit(ViewsWidget)
        self.lineEditThumbnail.setObjectName(u"lineEditThumbnail")

        self.gridLayout.addWidget(self.lineEditThumbnail, 1, 3, 1, 1)

        self.labelDescription = QLabel(ViewsWidget)
        self.labelDescription.setObjectName(u"labelDescription")

        self.gridLayout.addWidget(self.labelDescription, 5, 1, 1, 1)

        self.labelAnnotation = QLabel(ViewsWidget)
        self.labelAnnotation.setObjectName(u"labelAnnotation")

        self.gridLayout.addWidget(self.labelAnnotation, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 3, 1, 1)

        self.pushButtonThumbnailFile = QPushButton(ViewsWidget)
        self.pushButtonThumbnailFile.setObjectName(u"pushButtonThumbnailFile")

        self.gridLayout.addWidget(self.pushButtonThumbnailFile, 1, 4, 1, 1)

        self.lineEditPath = QLineEdit(ViewsWidget)
        self.lineEditPath.setObjectName(u"lineEditPath")

        self.gridLayout.addWidget(self.lineEditPath, 0, 3, 1, 1)

        self.comboBoxSample = QComboBox(ViewsWidget)
        self.comboBoxSample.addItem("")
        self.comboBoxSample.setObjectName(u"comboBoxSample")

        self.gridLayout.addWidget(self.comboBoxSample, 4, 3, 1, 1)

        self.labelThumbnail = QLabel(ViewsWidget)
        self.labelThumbnail.setObjectName(u"labelThumbnail")

        self.gridLayout.addWidget(self.labelThumbnail, 1, 1, 1, 1)

        self.pushButtonViewFile = QPushButton(ViewsWidget)
        self.pushButtonViewFile.setObjectName(u"pushButtonViewFile")

        self.gridLayout.addWidget(self.pushButtonViewFile, 0, 4, 1, 1)

        self.plainTextEditDescription = QPlainTextEdit(ViewsWidget)
        self.plainTextEditDescription.setObjectName(u"plainTextEditDescription")

        self.gridLayout.addWidget(self.plainTextEditDescription, 5, 3, 1, 1)


        self.retranslateUi(ViewsWidget)

        QMetaObject.connectSlotsByName(ViewsWidget)
    # setupUi

    def retranslateUi(self, ViewsWidget):
        ViewsWidget.setWindowTitle(QCoreApplication.translate("ViewsWidget", u"ViewsWidget", None))
        self.comboBoxAnnotation.setItemText(0, QCoreApplication.translate("ViewsWidget", u"--", None))

        self.labelSample.setText(QCoreApplication.translate("ViewsWidget", u"Sample:", None))
#if QT_CONFIG(tooltip)
        self.labelPath.setToolTip(QCoreApplication.translate("ViewsWidget", u"Relative path from dataset root directory", None))
#endif // QT_CONFIG(tooltip)
        self.labelPath.setText(QCoreApplication.translate("ViewsWidget", u"Path:", None))
#if QT_CONFIG(tooltip)
        self.lineEditThumbnail.setToolTip(QCoreApplication.translate("ViewsWidget", u"Relative path from dataset root directory", None))
#endif // QT_CONFIG(tooltip)
        self.labelDescription.setText(QCoreApplication.translate("ViewsWidget", u"Description:", None))
        self.labelAnnotation.setText(QCoreApplication.translate("ViewsWidget", u"Annotation:", None))
        self.pushButtonThumbnailFile.setText(QCoreApplication.translate("ViewsWidget", u"...", None))
#if QT_CONFIG(tooltip)
        self.lineEditPath.setToolTip(QCoreApplication.translate("ViewsWidget", u"Relative path from dataset root directory", None))
#endif // QT_CONFIG(tooltip)
        self.comboBoxSample.setItemText(0, QCoreApplication.translate("ViewsWidget", u"--", None))

#if QT_CONFIG(tooltip)
        self.labelThumbnail.setToolTip(QCoreApplication.translate("ViewsWidget", u"Relative path from dataset root directory", None))
#endif // QT_CONFIG(tooltip)
        self.labelThumbnail.setText(QCoreApplication.translate("ViewsWidget", u"Thumbnail:", None))
        self.pushButtonViewFile.setText(QCoreApplication.translate("ViewsWidget", u"...", None))
    # retranslateUi

