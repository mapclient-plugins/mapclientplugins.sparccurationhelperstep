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


class Ui_SparcCurationHelperWidget(object):
    def setupUi(self, SparcCurationHelperWidget):
        if not SparcCurationHelperWidget.objectName():
            SparcCurationHelperWidget.setObjectName(u"SparcCurationHelperWidget")
        SparcCurationHelperWidget.resize(578, 521)
        self.gridLayout = QGridLayout(SparcCurationHelperWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(SparcCurationHelperWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.scaffold_annotation_tab = QWidget()
        self.scaffold_annotation_tab.setObjectName(u"scaffold_annotation_tab")
        self.gridLayout1 = QGridLayout(self.scaffold_annotation_tab)
        self.gridLayout1.setObjectName(u"gridLayout1")
        self.groupBox = QGroupBox(self.scaffold_annotation_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout2 = QGridLayout(self.groupBox)
        self.gridLayout2.setObjectName(u"gridLayout2")
        self.scaffold_annotations_listView = QListView(self.groupBox)
        self.scaffold_annotations_listView.setObjectName(u"scaffold_annotations_listView")

        self.gridLayout2.addWidget(self.scaffold_annotations_listView, 0, 0, 1, 1)

        self.scaffold_annotation_label = QLabel(self.groupBox)
        self.scaffold_annotation_label.setObjectName(u"scaffold_annotation_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaffold_annotation_label.sizePolicy().hasHeightForWidth())
        self.scaffold_annotation_label.setSizePolicy(sizePolicy)

        self.gridLayout2.addWidget(self.scaffold_annotation_label, 0, 1, 1, 1)


        self.gridLayout1.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox1 = QGroupBox(self.scaffold_annotation_tab)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout3 = QGridLayout(self.groupBox1)
        self.gridLayout3.setObjectName(u"gridLayout3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.annotate_scaffold_button = QPushButton(self.groupBox1)
        self.annotate_scaffold_button.setObjectName(u"annotate_scaffold_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.annotate_scaffold_button.sizePolicy().hasHeightForWidth())
        self.annotate_scaffold_button.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.annotate_scaffold_button, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox1)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox1)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)


        self.gridLayout3.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.errors_listView = QListView(self.groupBox1)
        self.errors_listView.setObjectName(u"errors_listView")

        self.gridLayout3.addWidget(self.errors_listView, 0, 0, 1, 1)


        self.gridLayout1.addWidget(self.groupBox1, 3, 0, 1, 1)

        self.groupBox2 = QGroupBox(self.scaffold_annotation_tab)
        self.groupBox2.setObjectName(u"groupBox2")
        self.gridLayout4 = QGridLayout(self.groupBox2)
        self.gridLayout4.setObjectName(u"gridLayout4")
        self.scaffold_metadata_listView = QListView(self.groupBox2)
        self.scaffold_metadata_listView.setObjectName(u"scaffold_metadata_listView")

        self.gridLayout4.addWidget(self.scaffold_metadata_listView, 0, 0, 1, 1)

        self.scaffold_metadata_label = QLabel(self.groupBox2)
        self.scaffold_metadata_label.setObjectName(u"scaffold_metadata_label")
        sizePolicy.setHeightForWidth(self.scaffold_metadata_label.sizePolicy().hasHeightForWidth())
        self.scaffold_metadata_label.setSizePolicy(sizePolicy)

        self.gridLayout4.addWidget(self.scaffold_metadata_label, 0, 1, 1, 1)


        self.gridLayout1.addWidget(self.groupBox2, 2, 0, 1, 1)

        self.tabWidget.addTab(self.scaffold_annotation_tab, "")
        self.plot_annotation_tab = QWidget()
        self.plot_annotation_tab.setObjectName(u"plot_annotation_tab")
        self.tabWidget.addTab(self.plot_annotation_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.pushButtonDone = QPushButton(SparcCurationHelperWidget)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.gridLayout.addWidget(self.pushButtonDone, 1, 0, 1, 1)


        self.retranslateUi(SparcCurationHelperWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SparcCurationHelperWidget)
    # setupUi

    def retranslateUi(self, SparcCurationHelperWidget):
        SparcCurationHelperWidget.setWindowTitle(QCoreApplication.translate("SparcCurationHelperWidget", u"Sparc Curation Helper", None))
        self.groupBox.setTitle(QCoreApplication.translate("SparcCurationHelperWidget", u"Annotated Scaffold Files:", None))
        self.scaffold_annotation_label.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"TextLabel", None))
        self.groupBox1.setTitle(QCoreApplication.translate("SparcCurationHelperWidget", u"Errors:", None))
        self.annotate_scaffold_button.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Annotate Scaffold", None))
        self.pushButton_2.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"TextLabel", None))
        self.groupBox2.setTitle(QCoreApplication.translate("SparcCurationHelperWidget", u"Files detected as Scaffold:", None))
        self.scaffold_metadata_label.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scaffold_annotation_tab), QCoreApplication.translate("SparcCurationHelperWidget", u"Scaffold Annotation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plot_annotation_tab), QCoreApplication.translate("SparcCurationHelperWidget", u"Plot Annotation", None))
        self.pushButtonDone.setText(QCoreApplication.translate("SparcCurationHelperWidget", u"Done", None))
    # retranslateUi

