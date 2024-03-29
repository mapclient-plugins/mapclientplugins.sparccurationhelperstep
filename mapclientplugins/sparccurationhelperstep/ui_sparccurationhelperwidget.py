# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sparccurationhelperwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

from mapclientplugins.sparccurationhelperstep.helpers.contextannotationwidget import ContextAnnotationWidget
from mapclientplugins.sparccurationhelperstep.helpers.scaffoldannotationwidget import ScaffoldAnnotationWidget
from mapclientplugins.sparccurationhelperstep.helpers.plotannotationwidget import PlotAnnotationWidget

class Ui_SparcCurationHelperWidget(object):
    def setupUi(self, SparcCurationHelperWidget):
        if not SparcCurationHelperWidget.objectName():
            SparcCurationHelperWidget.setObjectName(u"SparcCurationHelperWidget")
        SparcCurationHelperWidget.resize(824, 693)
        self.verticalLayout = QVBoxLayout(SparcCurationHelperWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(SparcCurationHelperWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabScaffoldAnnotation = ScaffoldAnnotationWidget()
        self.tabScaffoldAnnotation.setObjectName(u"tabScaffoldAnnotation")
        self.tabWidget.addTab(self.tabScaffoldAnnotation, "")
        self.tabPlotAnnotation = PlotAnnotationWidget()
        self.tabPlotAnnotation.setObjectName(u"tabPlotAnnotation")
        self.tabWidget.addTab(self.tabPlotAnnotation, "")
        self.tabContextAnnotation = ContextAnnotationWidget()
        self.tabContextAnnotation.setObjectName(u"tabContextAnnotation")
        self.tabWidget.addTab(self.tabContextAnnotation, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonDocumentation = QPushButton(SparcCurationHelperWidget)
        self.pushButtonDocumentation.setObjectName(u"pushButtonDocumentation")

        self.horizontalLayout.addWidget(self.pushButtonDocumentation)

        self.pushButtonDone = QPushButton(SparcCurationHelperWidget)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.horizontalLayout.addWidget(self.pushButtonDone)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SparcCurationHelperWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SparcCurationHelperWidget)
    # setupUi

    def retranslateUi(self, SparcCurationHelperWidget):
        SparcCurationHelperWidget.setWindowTitle(QCoreApplication.translate("SparcCurationHelperWidget", u"Sparc Curation Helper", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabScaffoldAnnotation), QCoreApplication.translate("SparcCurationHelperWidget", u"Scaffold Annotation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlotAnnotation), QCoreApplication.translate("SparcCurationHelperWidget", u"Plot Annotation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabContextAnnotation), QCoreApplication.translate("SparcCurationHelperWidget", u"Context Annotation", None))
        self.pushButtonDocumentation.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Online Documentation", None))
        self.pushButtonDone.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Done", None))
    # retranslateUi

