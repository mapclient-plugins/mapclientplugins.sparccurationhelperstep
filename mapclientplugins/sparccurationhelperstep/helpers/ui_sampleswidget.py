# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sampleswidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_SamplesWidget(object):
    def setupUi(self, SamplesWidget):
        if not SamplesWidget.objectName():
            SamplesWidget.setObjectName(u"SamplesWidget")
        SamplesWidget.resize(400, 300)
        self.gridLayout = QGridLayout(SamplesWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelHeading = QLabel(SamplesWidget)
        self.labelHeading.setObjectName(u"labelHeading")

        self.gridLayout.addWidget(self.labelHeading, 0, 0, 1, 1)

        self.lineEditHeading = QLineEdit(SamplesWidget)
        self.lineEditHeading.setObjectName(u"lineEditHeading")

        self.gridLayout.addWidget(self.lineEditHeading, 0, 1, 1, 1)

        self.labelDOI = QLabel(SamplesWidget)
        self.labelDOI.setObjectName(u"labelDOI")

        self.gridLayout.addWidget(self.labelDOI, 1, 0, 1, 1)

        self.lineEditDOI = QLineEdit(SamplesWidget)
        self.lineEditDOI.setObjectName(u"lineEditDOI")

        self.gridLayout.addWidget(self.lineEditDOI, 1, 1, 1, 1)

        self.labelPath = QLabel(SamplesWidget)
        self.labelPath.setObjectName(u"labelPath")

        self.gridLayout.addWidget(self.labelPath, 2, 0, 1, 1)

        self.lineEditPath = QLineEdit(SamplesWidget)
        self.lineEditPath.setObjectName(u"lineEditPath")

        self.gridLayout.addWidget(self.lineEditPath, 2, 1, 1, 1)

        self.pushButtonPathFile = QPushButton(SamplesWidget)
        self.pushButtonPathFile.setObjectName(u"pushButtonPathFile")

        self.gridLayout.addWidget(self.pushButtonPathFile, 2, 2, 1, 1)

        self.labelAnnotation = QLabel(SamplesWidget)
        self.labelAnnotation.setObjectName(u"labelAnnotation")

        self.gridLayout.addWidget(self.labelAnnotation, 3, 0, 1, 1)

        self.lineEditAnnotation = QLineEdit(SamplesWidget)
        self.lineEditAnnotation.setObjectName(u"lineEditAnnotation")

        self.gridLayout.addWidget(self.lineEditAnnotation, 3, 1, 1, 1)

        self.labelView = QLabel(SamplesWidget)
        self.labelView.setObjectName(u"labelView")

        self.gridLayout.addWidget(self.labelView, 4, 0, 1, 1)

        self.comboBoxView = QComboBox(SamplesWidget)
        self.comboBoxView.addItem("")
        self.comboBoxView.setObjectName(u"comboBoxView")

        self.gridLayout.addWidget(self.comboBoxView, 4, 1, 2, 1)

        self.labelDescription = QLabel(SamplesWidget)
        self.labelDescription.setObjectName(u"labelDescription")

        self.gridLayout.addWidget(self.labelDescription, 5, 0, 2, 1)

        self.plainTextEditDescription = QPlainTextEdit(SamplesWidget)
        self.plainTextEditDescription.setObjectName(u"plainTextEditDescription")

        self.gridLayout.addWidget(self.plainTextEditDescription, 6, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 1, 1, 1)


        self.retranslateUi(SamplesWidget)

        QMetaObject.connectSlotsByName(SamplesWidget)
    # setupUi

    def retranslateUi(self, SamplesWidget):
        SamplesWidget.setWindowTitle(QCoreApplication.translate("SamplesWidget", u"SamplesWidget", None))
        self.labelHeading.setText(QCoreApplication.translate("SamplesWidget", u"Heading:", None))
        self.labelDOI.setText(QCoreApplication.translate("SamplesWidget", u"DOI:", None))
        self.labelPath.setText(QCoreApplication.translate("SamplesWidget", u"Path:", None))
        self.pushButtonPathFile.setText(QCoreApplication.translate("SamplesWidget", u"...", None))
        self.labelAnnotation.setText(QCoreApplication.translate("SamplesWidget", u"Annotation:", None))
        self.labelView.setText(QCoreApplication.translate("SamplesWidget", u"View:", None))
        self.comboBoxView.setItemText(0, QCoreApplication.translate("SamplesWidget", u"--", None))

        self.labelDescription.setText(QCoreApplication.translate("SamplesWidget", u"Description:", None))
    # retranslateUi

