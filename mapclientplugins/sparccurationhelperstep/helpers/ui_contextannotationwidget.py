# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contextannotationwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_ContextAnnotationWidget(object):
    def setupUi(self, ContextAnnotationWidget):
        if not ContextAnnotationWidget.objectName():
            ContextAnnotationWidget.setObjectName(u"ContextAnnotationWidget")
        ContextAnnotationWidget.resize(825, 579)
        self.verticalLayout = QVBoxLayout(ContextAnnotationWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(ContextAnnotationWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEditAnnotationMapFile = QLineEdit(ContextAnnotationWidget)
        self.lineEditAnnotationMapFile.setObjectName(u"lineEditAnnotationMapFile")

        self.horizontalLayout.addWidget(self.lineEditAnnotationMapFile)

        self.pushButtonAnnotationMapFile = QPushButton(ContextAnnotationWidget)
        self.pushButtonAnnotationMapFile.setObjectName(u"pushButtonAnnotationMapFile")

        self.horizontalLayout.addWidget(self.pushButtonAnnotationMapFile)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(ContextAnnotationWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabSummary = QWidget()
        self.tabSummary.setObjectName(u"tabSummary")
        self.gridLayout = QGridLayout(self.tabSummary)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelSummaryHeading = QLabel(self.tabSummary)
        self.labelSummaryHeading.setObjectName(u"labelSummaryHeading")

        self.gridLayout.addWidget(self.labelSummaryHeading, 0, 0, 1, 1)

        self.lineEditSummaryHeading = QLineEdit(self.tabSummary)
        self.lineEditSummaryHeading.setObjectName(u"lineEditSummaryHeading")

        self.gridLayout.addWidget(self.lineEditSummaryHeading, 0, 1, 1, 1)

        self.labelSummaryDescription = QLabel(self.tabSummary)
        self.labelSummaryDescription.setObjectName(u"labelSummaryDescription")

        self.gridLayout.addWidget(self.labelSummaryDescription, 1, 0, 1, 1)

        self.plainTextEditSummaryDescription = QPlainTextEdit(self.tabSummary)
        self.plainTextEditSummaryDescription.setObjectName(u"plainTextEditSummaryDescription")

        self.gridLayout.addWidget(self.plainTextEditSummaryDescription, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tabSummary, "")
        self.tabSamples = QWidget()
        self.tabSamples.setObjectName(u"tabSamples")
        self.verticalLayout_2 = QVBoxLayout(self.tabSamples)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonSamplesAdd = QPushButton(self.tabSamples)
        self.pushButtonSamplesAdd.setObjectName(u"pushButtonSamplesAdd")

        self.horizontalLayout_2.addWidget(self.pushButtonSamplesAdd)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidgetSamples = QTabWidget(self.tabSamples)
        self.tabWidgetSamples.setObjectName(u"tabWidgetSamples")
        self.tabWidgetSamples.setTabsClosable(True)

        self.verticalLayout_2.addWidget(self.tabWidgetSamples)

        self.tabWidget.addTab(self.tabSamples, "")
        self.tabViews = QWidget()
        self.tabViews.setObjectName(u"tabViews")
        self.verticalLayout_3 = QVBoxLayout(self.tabViews)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonViewsAdd = QPushButton(self.tabViews)
        self.pushButtonViewsAdd.setObjectName(u"pushButtonViewsAdd")

        self.horizontalLayout_3.addWidget(self.pushButtonViewsAdd)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tabWidgetViews = QTabWidget(self.tabViews)
        self.tabWidgetViews.setObjectName(u"tabWidgetViews")
        self.tabWidgetViews.setTabsClosable(True)

        self.verticalLayout_3.addWidget(self.tabWidgetViews)

        self.tabWidget.addTab(self.tabViews, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ContextAnnotationWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ContextAnnotationWidget)
    # setupUi

    def retranslateUi(self, ContextAnnotationWidget):
        ContextAnnotationWidget.setWindowTitle(QCoreApplication.translate("ContextAnnotationWidget", u"ContextAnnotationWidget", None))
        self.label.setText(QCoreApplication.translate("ContextAnnotationWidget", u"Scaffold annotation map file:", None))
        self.pushButtonAnnotationMapFile.setText(QCoreApplication.translate("ContextAnnotationWidget", u"...", None))
        self.labelSummaryHeading.setText(QCoreApplication.translate("ContextAnnotationWidget", u"Heading:", None))
        self.labelSummaryDescription.setText(QCoreApplication.translate("ContextAnnotationWidget", u"Description:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSummary), QCoreApplication.translate("ContextAnnotationWidget", u"Summary", None))
        self.pushButtonSamplesAdd.setText(QCoreApplication.translate("ContextAnnotationWidget", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSamples), QCoreApplication.translate("ContextAnnotationWidget", u"Samples", None))
        self.pushButtonViewsAdd.setText(QCoreApplication.translate("ContextAnnotationWidget", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabViews), QCoreApplication.translate("ContextAnnotationWidget", u"Views", None))
    # retranslateUi

