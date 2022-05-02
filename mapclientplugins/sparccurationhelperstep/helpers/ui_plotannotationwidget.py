# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotannotationwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PlotAnnotationWidget(object):
    def setupUi(self, PlotAnnotationWidget):
        if not PlotAnnotationWidget.objectName():
            PlotAnnotationWidget.setObjectName(u"PlotAnnotationWidget")
        PlotAnnotationWidget.resize(927, 753)
        self.verticalLayout = QVBoxLayout(PlotAnnotationWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxPlotAnntotations = QGroupBox(PlotAnnotationWidget)
        self.groupBoxPlotAnntotations.setObjectName(u"groupBoxPlotAnntotations")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBoxPlotAnntotations)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.treeViewPlotAnnotations = QTreeView(self.groupBoxPlotAnntotations)
        self.treeViewPlotAnnotations.setObjectName(u"treeViewPlotAnnotations")

        self.horizontalLayout_2.addWidget(self.treeViewPlotAnnotations)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.thumbnail_preview_label = QLabel(self.groupBoxPlotAnntotations)
        self.thumbnail_preview_label.setObjectName(u"thumbnail_preview_label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbnail_preview_label.sizePolicy().hasHeightForWidth())
        self.thumbnail_preview_label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.thumbnail_preview_label)

        self.labelThumbnailPreview = QLabel(self.groupBoxPlotAnntotations)
        self.labelThumbnailPreview.setObjectName(u"labelThumbnailPreview")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelThumbnailPreview.sizePolicy().hasHeightForWidth())
        self.labelThumbnailPreview.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.labelThumbnailPreview)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.groupBoxPlotAnntotations)

        self.groupBox = QGroupBox(PlotAnnotationWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBoxAnnotationSubject = QComboBox(self.groupBox)
        self.comboBoxAnnotationSubject.setObjectName(u"comboBoxAnnotationSubject")

        self.horizontalLayout_3.addWidget(self.comboBoxAnnotationSubject)

        self.comboBoxSAnnotationPredicate = QComboBox(self.groupBox)
        self.comboBoxSAnnotationPredicate.setObjectName(u"comboBoxSAnnotationPredicate")

        self.horizontalLayout_3.addWidget(self.comboBoxSAnnotationPredicate)

        self.comboBoxAnnotationObject = QComboBox(self.groupBox)
        self.comboBoxAnnotationObject.setObjectName(u"comboBoxAnnotationObject")

        self.horizontalLayout_3.addWidget(self.comboBoxAnnotationObject)

        self.pushButtonApply = QPushButton(self.groupBox)
        self.pushButtonApply.setObjectName(u"pushButtonApply")

        self.horizontalLayout_3.addWidget(self.pushButtonApply)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBoxErrors = QGroupBox(PlotAnnotationWidget)
        self.groupBoxErrors.setObjectName(u"groupBoxErrors")
        self.groupBoxErrors.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout2 = QGridLayout(self.groupBoxErrors)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayoutButtons = QGridLayout()
        self.gridLayoutButtons.setObjectName(u"gridLayoutButtons")
        self.pushButtonFixAllErrors = QPushButton(self.groupBoxErrors)
        self.pushButtonFixAllErrors.setObjectName(u"pushButtonFixAllErrors")

        self.gridLayoutButtons.addWidget(self.pushButtonFixAllErrors, 1, 1, 1, 1)

        self.pushButtonFixError = QPushButton(self.groupBoxErrors)
        self.pushButtonFixError.setObjectName(u"pushButtonFixError")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonFixError.sizePolicy().hasHeightForWidth())
        self.pushButtonFixError.setSizePolicy(sizePolicy2)

        self.gridLayoutButtons.addWidget(self.pushButtonFixError, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayoutButtons.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)


        self.gridLayout2.addLayout(self.gridLayoutButtons, 0, 1, 1, 1)

        self.listViewErrors = QListView(self.groupBoxErrors)
        self.listViewErrors.setObjectName(u"listViewErrors")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listViewErrors.sizePolicy().hasHeightForWidth())
        self.listViewErrors.setSizePolicy(sizePolicy3)

        self.gridLayout2.addWidget(self.listViewErrors, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBoxErrors)


        self.retranslateUi(PlotAnnotationWidget)

        QMetaObject.connectSlotsByName(PlotAnnotationWidget)
    # setupUi

    def retranslateUi(self, PlotAnnotationWidget):
        PlotAnnotationWidget.setWindowTitle(QCoreApplication.translate("PlotAnnotationWidget", u"PlotAnnotationWidget", None))
        self.groupBoxPlotAnntotations.setTitle(QCoreApplication.translate("PlotAnnotationWidget", u"Plot annotations:", None))
        self.thumbnail_preview_label.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Thumbnail preview:", None))
        self.labelThumbnailPreview.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("PlotAnnotationWidget", u"Manual annotation:", None))
        self.pushButtonApply.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Apply", None))
        self.groupBoxErrors.setTitle(QCoreApplication.translate("PlotAnnotationWidget", u"Plots:", None))
        self.pushButtonFixAllErrors.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Annotate Plot Files", None))
        self.pushButtonFixError.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Generate Thumbnail", None))
    # retranslateUi

