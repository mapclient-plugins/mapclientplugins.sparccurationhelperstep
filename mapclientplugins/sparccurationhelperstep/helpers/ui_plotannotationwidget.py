# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotannotationwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QTreeView, QVBoxLayout,
    QWidget)

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

        self.groupBoxPlots = QGroupBox(PlotAnnotationWidget)
        self.groupBoxPlots.setObjectName(u"groupBoxPlots")
        self.groupBoxPlots.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout2 = QGridLayout(self.groupBoxPlots)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.listViewPlots = QListView(self.groupBoxPlots)
        self.listViewPlots.setObjectName(u"listViewPlots")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listViewPlots.sizePolicy().hasHeightForWidth())
        self.listViewPlots.setSizePolicy(sizePolicy2)

        self.gridLayout2.addWidget(self.listViewPlots, 0, 5, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButtonAddPlot = QPushButton(self.groupBoxPlots)
        self.pushButtonAddPlot.setObjectName(u"pushButtonAddPlot")

        self.gridLayout.addWidget(self.pushButtonAddPlot, 0, 0, 1, 1)

        self.pushButtonAddAllPlot = QPushButton(self.groupBoxPlots)
        self.pushButtonAddAllPlot.setObjectName(u"pushButtonAddAllPlot")

        self.gridLayout.addWidget(self.pushButtonAddAllPlot, 1, 0, 1, 1)

        self.pushButtonRemovePlot = QPushButton(self.groupBoxPlots)
        self.pushButtonRemovePlot.setObjectName(u"pushButtonRemovePlot")

        self.gridLayout.addWidget(self.pushButtonRemovePlot, 2, 0, 1, 1)


        self.gridLayout2.addLayout(self.gridLayout, 0, 1, 1, 2)

        self.verticalLayoutPlotEditor = QVBoxLayout()
        self.verticalLayoutPlotEditor.setObjectName(u"verticalLayoutPlotEditor")
        self.PlotEditorsContainer = QWidget(self.groupBoxPlots)
        self.PlotEditorsContainer.setObjectName(u"PlotEditorsContainer")
        self.PlotEditorsContainer.setEnabled(False)
        self.gridLayoutPlotEditors = QGridLayout(self.PlotEditorsContainer)
        self.gridLayoutPlotEditors.setObjectName(u"gridLayoutPlotEditors")
        self.gridLayoutPlotEditors.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.PlotEditorsContainer)
        self.label.setObjectName(u"label")

        self.gridLayoutPlotEditors.addWidget(self.label, 2, 0, 1, 1)

        self.comboBoxPlotType = QComboBox(self.PlotEditorsContainer)
        self.comboBoxPlotType.addItem("")
        self.comboBoxPlotType.addItem("")
        self.comboBoxPlotType.setObjectName(u"comboBoxPlotType")

        self.gridLayoutPlotEditors.addWidget(self.comboBoxPlotType, 2, 1, 1, 1)

        self.label_5 = QLabel(self.PlotEditorsContainer)
        self.label_5.setObjectName(u"label_5")

        self.gridLayoutPlotEditors.addWidget(self.label_5, 3, 0, 1, 1)

        self.lineEditXColumn = QLineEdit(self.PlotEditorsContainer)
        self.lineEditXColumn.setObjectName(u"lineEditXColumn")

        self.gridLayoutPlotEditors.addWidget(self.lineEditXColumn, 3, 1, 1, 1)

        self.label_4 = QLabel(self.PlotEditorsContainer)
        self.label_4.setObjectName(u"label_4")

        self.gridLayoutPlotEditors.addWidget(self.label_4, 4, 0, 1, 1)

        self.lineEditYColumns = QLineEdit(self.PlotEditorsContainer)
        self.lineEditYColumns.setObjectName(u"lineEditYColumns")

        self.gridLayoutPlotEditors.addWidget(self.lineEditYColumns, 4, 1, 1, 1)

        self.label_3 = QLabel(self.PlotEditorsContainer)
        self.label_3.setObjectName(u"label_3")

        self.gridLayoutPlotEditors.addWidget(self.label_3, 5, 0, 1, 1)

        self.checkBoxHasHeader = QCheckBox(self.PlotEditorsContainer)
        self.checkBoxHasHeader.setObjectName(u"checkBoxHasHeader")
        self.checkBoxHasHeader.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxHasHeader.setAutoFillBackground(False)

        self.gridLayoutPlotEditors.addWidget(self.checkBoxHasHeader, 5, 1, 1, 1)

        self.label_2 = QLabel(self.PlotEditorsContainer)
        self.label_2.setObjectName(u"label_2")

        self.gridLayoutPlotEditors.addWidget(self.label_2, 6, 0, 1, 1)

        self.comboBoxDelimiter = QComboBox(self.PlotEditorsContainer)
        self.comboBoxDelimiter.addItem("")
        self.comboBoxDelimiter.addItem("")
        self.comboBoxDelimiter.setObjectName(u"comboBoxDelimiter")

        self.gridLayoutPlotEditors.addWidget(self.comboBoxDelimiter, 6, 1, 1, 1)

        self.pushButtonAnnotateCurrentPlot = QPushButton(self.PlotEditorsContainer)
        self.pushButtonAnnotateCurrentPlot.setObjectName(u"pushButtonAnnotateCurrentPlot")

        self.gridLayoutPlotEditors.addWidget(self.pushButtonAnnotateCurrentPlot, 7, 1, 1, 1)


        self.verticalLayoutPlotEditor.addWidget(self.PlotEditorsContainer)

        self.pushButtonAnnotateAllPlots = QPushButton(self.groupBoxPlots)
        self.pushButtonAnnotateAllPlots.setObjectName(u"pushButtonAnnotateAllPlots")

        self.verticalLayoutPlotEditor.addWidget(self.pushButtonAnnotateAllPlots)


        self.gridLayout2.addLayout(self.verticalLayoutPlotEditor, 0, 6, 1, 1)

        self.treeViewFileBrowser = QTreeView(self.groupBoxPlots)
        self.treeViewFileBrowser.setObjectName(u"treeViewFileBrowser")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.treeViewFileBrowser.sizePolicy().hasHeightForWidth())
        self.treeViewFileBrowser.setSizePolicy(sizePolicy3)

        self.gridLayout2.addWidget(self.treeViewFileBrowser, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBoxPlots)


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
        self.groupBoxPlots.setTitle(QCoreApplication.translate("PlotAnnotationWidget", u"Plots:", None))
        self.pushButtonAddPlot.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Add>>", None))
        self.pushButtonAddAllPlot.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Add All>>", None))
        self.pushButtonRemovePlot.setText(QCoreApplication.translate("PlotAnnotationWidget", u"<<Remove", None))
        self.label.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Plot type:", None))
        self.comboBoxPlotType.setItemText(0, QCoreApplication.translate("PlotAnnotationWidget", u"timeseries", None))
        self.comboBoxPlotType.setItemText(1, QCoreApplication.translate("PlotAnnotationWidget", u"heatmap", None))

        self.label_5.setText(QCoreApplication.translate("PlotAnnotationWidget", u"x column:", None))
        self.label_4.setText(QCoreApplication.translate("PlotAnnotationWidget", u"y columns:", None))
        self.label_3.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Has header:", None))
        self.label_2.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Delimiter:", None))
        self.comboBoxDelimiter.setItemText(0, QCoreApplication.translate("PlotAnnotationWidget", u"tab", None))
        self.comboBoxDelimiter.setItemText(1, QCoreApplication.translate("PlotAnnotationWidget", u"comma", None))

        self.pushButtonAnnotateCurrentPlot.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Annotate This Plot File", None))
        self.pushButtonAnnotateAllPlots.setText(QCoreApplication.translate("PlotAnnotationWidget", u"Annotate All Plot Files", None))
    # retranslateUi

