# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sparccurationhelperwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mapclientplugins.sparccurationhelperstep.helpers.contextannotationwidget import ContextAnnotationWidget


class Ui_SparcCurationHelperWidget(object):
    def setupUi(self, SparcCurationHelperWidget):
        if not SparcCurationHelperWidget.objectName():
            SparcCurationHelperWidget.setObjectName(u"SparcCurationHelperWidget")
        SparcCurationHelperWidget.resize(824, 693)
        self.verticalLayout = QVBoxLayout(SparcCurationHelperWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(SparcCurationHelperWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.scaffold_annotation_tab = QWidget()
        self.scaffold_annotation_tab.setObjectName(u"scaffold_annotation_tab")
        self.gridLayout3 = QGridLayout(self.scaffold_annotation_tab)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.groupBoxScaffoldAnntotations = QGroupBox(self.scaffold_annotation_tab)
        self.groupBoxScaffoldAnntotations.setObjectName(u"groupBoxScaffoldAnntotations")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBoxScaffoldAnntotations)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.treeViewScaffoldAnnotations = QTreeView(self.groupBoxScaffoldAnntotations)
        self.treeViewScaffoldAnnotations.setObjectName(u"treeViewScaffoldAnnotations")

        self.horizontalLayout_2.addWidget(self.treeViewScaffoldAnnotations)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.thumbnail_preview_label = QLabel(self.groupBoxScaffoldAnntotations)
        self.thumbnail_preview_label.setObjectName(u"thumbnail_preview_label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbnail_preview_label.sizePolicy().hasHeightForWidth())
        self.thumbnail_preview_label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.thumbnail_preview_label)

        self.labelThumbnailPreview = QLabel(self.groupBoxScaffoldAnntotations)
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


        self.gridLayout3.addWidget(self.groupBoxScaffoldAnntotations, 0, 0, 1, 1)

        self.groupBoxErrors = QGroupBox(self.scaffold_annotation_tab)
        self.groupBoxErrors.setObjectName(u"groupBoxErrors")
        self.groupBoxErrors.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout2 = QGridLayout(self.groupBoxErrors)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.gridLayoutButtons = QGridLayout()
        self.gridLayoutButtons.setObjectName(u"gridLayoutButtons")
        self.annotate_scaffold_button = QPushButton(self.groupBoxErrors)
        self.annotate_scaffold_button.setObjectName(u"annotate_scaffold_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.annotate_scaffold_button.sizePolicy().hasHeightForWidth())
        self.annotate_scaffold_button.setSizePolicy(sizePolicy2)

        self.gridLayoutButtons.addWidget(self.annotate_scaffold_button, 0, 2, 1, 1)

        self.buttonFixError = QPushButton(self.groupBoxErrors)
        self.buttonFixError.setObjectName(u"buttonFixError")
        sizePolicy2.setHeightForWidth(self.buttonFixError.sizePolicy().hasHeightForWidth())
        self.buttonFixError.setSizePolicy(sizePolicy2)

        self.gridLayoutButtons.addWidget(self.buttonFixError, 0, 1, 1, 1)

        self.buttonFixAllErrors = QPushButton(self.groupBoxErrors)
        self.buttonFixAllErrors.setObjectName(u"buttonFixAllErrors")

        self.gridLayoutButtons.addWidget(self.buttonFixAllErrors, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBoxErrors)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayoutButtons.addWidget(self.pushButton_3, 1, 2, 1, 1)

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


        self.gridLayout3.addWidget(self.groupBoxErrors, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.scaffold_annotation_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBoxScaffoldMeta = QComboBox(self.groupBox)
        self.comboBoxScaffoldMeta.setObjectName(u"comboBoxScaffoldMeta")

        self.horizontalLayout_3.addWidget(self.comboBoxScaffoldMeta)

        self.comboBoxScaffoldView = QComboBox(self.groupBox)
        self.comboBoxScaffoldView.setObjectName(u"comboBoxScaffoldView")

        self.horizontalLayout_3.addWidget(self.comboBoxScaffoldView)

        self.comboBoxScaffoldThumbnail = QComboBox(self.groupBox)
        self.comboBoxScaffoldThumbnail.setObjectName(u"comboBoxScaffoldThumbnail")

        self.horizontalLayout_3.addWidget(self.comboBoxScaffoldThumbnail)

        self.pushButtonApply = QPushButton(self.groupBox)
        self.pushButtonApply.setObjectName(u"pushButtonApply")

        self.horizontalLayout_3.addWidget(self.pushButtonApply)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout3.addWidget(self.groupBox, 1, 0, 1, 1)

        self.tabWidget.addTab(self.scaffold_annotation_tab, "")
        self.plot_annotation_tab = QWidget()
        self.plot_annotation_tab.setObjectName(u"plot_annotation_tab")
        self.tabWidget.addTab(self.plot_annotation_tab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = ContextAnnotationWidget(self.tab)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_3.addWidget(self.widget)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.tableViewScaffoldAnnotations = QTableView(SparcCurationHelperWidget)
        self.tableViewScaffoldAnnotations.setObjectName(u"tableViewScaffoldAnnotations")
        sizePolicy1.setHeightForWidth(self.tableViewScaffoldAnnotations.sizePolicy().hasHeightForWidth())
        self.tableViewScaffoldAnnotations.setSizePolicy(sizePolicy1)
        self.tableViewScaffoldAnnotations.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableViewScaffoldAnnotations.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableViewScaffoldAnnotations.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableViewScaffoldAnnotations)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonDone = QPushButton(SparcCurationHelperWidget)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.horizontalLayout.addWidget(self.pushButtonDone)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SparcCurationHelperWidget)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(SparcCurationHelperWidget)
    # setupUi

    def retranslateUi(self, SparcCurationHelperWidget):
        SparcCurationHelperWidget.setWindowTitle(QCoreApplication.translate("SparcCurationHelperWidget", u"Sparc Curation Helper", None))
        self.groupBoxScaffoldAnntotations.setTitle(QCoreApplication.translate("SparcCurationHelperWidget", u"Scaffold annotations:", None))
        self.thumbnail_preview_label.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Thumbnail preview:", None))
        self.labelThumbnailPreview.setText("")
        self.groupBoxErrors.setTitle(QCoreApplication.translate("SparcCurationHelperWidget", u"Errors:", None))
        self.annotate_scaffold_button.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Annotate Scaffold", None))
        self.buttonFixError.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Fix Error", None))
        self.buttonFixAllErrors.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Fix All Errors", None))
        self.pushButton_3.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Don't Push", None))
        self.groupBox.setTitle(QCoreApplication.translate("SparcCurationHelperWidget", u"Manual assignment:", None))
        self.pushButtonApply.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scaffold_annotation_tab), QCoreApplication.translate("SparcCurationHelperWidget", u"Scaffold Annotation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plot_annotation_tab), QCoreApplication.translate("SparcCurationHelperWidget", u"Plot Annotation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SparcCurationHelperWidget", u"Context Annotation", None))
        self.pushButtonDone.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Done", None))
    # retranslateUi

