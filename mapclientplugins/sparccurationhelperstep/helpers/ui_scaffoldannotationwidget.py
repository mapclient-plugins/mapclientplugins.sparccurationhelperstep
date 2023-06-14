# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scaffoldannotationwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QTreeView, QVBoxLayout, QWidget)

class Ui_ScaffoldAnnotationWidget(object):
    def setupUi(self, ScaffoldAnnotationWidget):
        if not ScaffoldAnnotationWidget.objectName():
            ScaffoldAnnotationWidget.setObjectName(u"ScaffoldAnnotationWidget")
        ScaffoldAnnotationWidget.resize(927, 753)
        self.verticalLayout = QVBoxLayout(ScaffoldAnnotationWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBoxScaffoldAnntotations = QGroupBox(ScaffoldAnnotationWidget)
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


        self.verticalLayout.addWidget(self.groupBoxScaffoldAnntotations)

        self.groupBox = QGroupBox(ScaffoldAnnotationWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBoxAnnotationSubject = QComboBox(self.groupBox)
        self.comboBoxAnnotationSubject.setObjectName(u"comboBoxAnnotationSubject")

        self.horizontalLayout_3.addWidget(self.comboBoxAnnotationSubject)

        self.comboBoxSAnnotationPredicate = QComboBox(self.groupBox)
        self.comboBoxSAnnotationPredicate.setObjectName(u"comboBoxSAnnotationPredicate")

        self.horizontalLayout_3.addWidget(self.comboBoxSAnnotationPredicate)

        self.checkBoxAnnotationMode = QCheckBox(self.groupBox)
        self.checkBoxAnnotationMode.setObjectName(u"checkBoxAnnotationMode")

        self.horizontalLayout_3.addWidget(self.checkBoxAnnotationMode)

        self.comboBoxAnnotationObject = QComboBox(self.groupBox)
        self.comboBoxAnnotationObject.setObjectName(u"comboBoxAnnotationObject")

        self.horizontalLayout_3.addWidget(self.comboBoxAnnotationObject)

        self.pushButtonApply = QPushButton(self.groupBox)
        self.pushButtonApply.setObjectName(u"pushButtonApply")

        self.horizontalLayout_3.addWidget(self.pushButtonApply)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBoxErrors = QGroupBox(ScaffoldAnnotationWidget)
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


        self.retranslateUi(ScaffoldAnnotationWidget)

        QMetaObject.connectSlotsByName(ScaffoldAnnotationWidget)
    # setupUi

    def retranslateUi(self, ScaffoldAnnotationWidget):
        ScaffoldAnnotationWidget.setWindowTitle(QCoreApplication.translate("ScaffoldAnnotationWidget", u"ScaffoldAnnotationWidget", None))
        self.groupBoxScaffoldAnntotations.setTitle(QCoreApplication.translate("ScaffoldAnnotationWidget", u"Scaffold annotations:", None))
        self.thumbnail_preview_label.setText(QCoreApplication.translate("ScaffoldAnnotationWidget", u"Thumbnail preview:", None))
        self.labelThumbnailPreview.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("ScaffoldAnnotationWidget", u"Manual annotation:", None))
#if QT_CONFIG(tooltip)
        self.checkBoxAnnotationMode.setToolTip(QCoreApplication.translate("ScaffoldAnnotationWidget", u"Append or replace entry", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxAnnotationMode.setText(QCoreApplication.translate("ScaffoldAnnotationWidget", u"Append", None))
        self.pushButtonApply.setText(QCoreApplication.translate("ScaffoldAnnotationWidget", u"Apply", None))
        self.groupBoxErrors.setTitle(QCoreApplication.translate("ScaffoldAnnotationWidget", u"Errors:", None))
        self.pushButtonFixAllErrors.setText(QCoreApplication.translate("ScaffoldAnnotationWidget", u"Fix All Errors", None))
        self.pushButtonFixError.setText(QCoreApplication.translate("ScaffoldAnnotationWidget", u"Fix Error", None))
    # retranslateUi

