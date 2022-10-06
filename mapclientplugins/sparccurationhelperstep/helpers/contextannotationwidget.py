import csv
import json
import os.path

from PySide2 import QtWidgets, QtGui, QtCore
from sparc.curation.tools.utilities import convert_to_bytes

from mapclientplugins.sparccurationhelperstep.helpers.ui_contextannotationwidget import Ui_ContextAnnotationWidget
from mapclientplugins.sparccurationhelperstep.helpers.sampleswidget import SamplesWidget
from mapclientplugins.sparccurationhelperstep.helpers.viewswidget import ViewsWidget

import sparc.curation.tools.context_annotations as context_annotations
from sparc.curation.tools.contextinfo import ContextInfoAnnotation
from sparc.curation.tools.ondisk import is_annotation_csv_file, OnDiskFiles


class ContextAnnotationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ContextAnnotationWidget, self).__init__(parent)
        self._ui = Ui_ContextAnnotationWidget()
        self._ui.setupUi(self)

        self._location = None

        self._previous_location = QtCore.QDir.homePath()
        self._scaffold_annotations = None
        self._context_info_list = []
        self._current_context_info = None

        self._make_connections()

    def update_info(self, location):
        self._location = location
        max_size = convert_to_bytes('3MiB')
        OnDiskFiles().setup_dataset(location, max_size)
        metadata_files = OnDiskFiles().get_scaffold_data().get_metadata_files()
        subject_list = [*metadata_files]

        subject_model = _build_list_model(subject_list)
        self._ui.comboBoxContextMetadata.setModel(subject_model)

        # Initial context data.
        for metadata_file in metadata_files:
            metadata_filename = os.path.basename(metadata_file)
            context_info_filename = metadata_filename.split(".")[0]+"_context_info.json"
            metadata_file_path = os.path.join("derivative", metadata_filename)
            self._context_info_list.append(ContextInfoAnnotation(metadata_file_path, context_info_filename))

        # Find context data.
        context_files = context_annotations.search_for_context_data_files(location, convert_to_bytes("2MiB"))
        for context_file in context_files:
            with open(context_file, encoding='utf-8') as f:
                json_data = json.load(f)
                for context_info in self._context_info_list:
                    if json_data["metadata"] == context_info._metadata_file:
                        context_info.from_dict(json_data)
                        if json_data["metadata"] in self._ui.comboBoxContextMetadata.currentText():
                            self._current_context_info = context_info
        
        if self._current_context_info:
            self._populate_ui(self._current_context_info)

        # Find annotation file.
        annotation_files = context_annotations.search_for_annotation_csv_files(location, convert_to_bytes("2MiB"))
        self._load_view_annotations(annotation_files)

    def previous_location(self):
        return self._previous_location

    def set_previous_location(self, previous_location):
        self._previous_location = previous_location

    def clean_ui(self):
        self._ui.lineEditSummaryHeading.setText("")
        self._ui.plainTextEditSummaryDescription.setPlainText("")
        self._ui.tabWidgetViews.clear()
        self._ui.tabWidgetSamples.clear()

    def _populate_ui(self, data):
        self.clean_ui()
        self._ui.lineEditSummaryHeading.setText(data._context_heading)
        self._ui.plainTextEditSummaryDescription.setPlainText(data._context_description)
        for view in data._views:
            self._create_view(view["id"])

        for sample in data._samples:
            self._create_sample(sample["id"])
            self._add_sample_to_views(sample["id"])

        view_headers = self._view_tab_headers()
        for view_header in view_headers:
            self._add_view_to_samples(view_header)

        for i, view in enumerate(data._views):
            v = self._ui.tabWidgetViews.widget(i)
            v.from_dict(view)

        for i, sample in enumerate(data._samples):
            s = self._ui.tabWidgetSamples.widget(i)
            s.from_dict(sample)

    def _make_connections(self):
        self._ui.pushButtonAnnotationMapFile.clicked.connect(self._open_annotation_map_file)
        self._ui.pushButtonSamplesAdd.clicked.connect(self._samples_add_clicked)
        self._ui.pushButtonViewsAdd.clicked.connect(self._views_add_clicked)
        self._ui.tabWidgetSamples.tabCloseRequested.connect(self._sample_tab_close_requested)
        self._ui.tabWidgetViews.tabCloseRequested.connect(self._view_tab_close_requested)
        self._ui.comboBoxContextMetadata.currentTextChanged.connect(self._on_metadata_changed)

    def create_annotation_data_json(self, data):
        views = data["views"]
        samples = data["samples"]
        annotation_data = {
            "version": "0.2.0",
            "id": "sparc.science.annotation_data",
        }

        def _add_entry(_annotation_data, annotation, value):
            if annotation and annotation != "--":
                if annotation in _annotation_data:
                    _annotation_data[annotation].append(value)
                else:
                    _annotation_data[annotation] = [value]

        for v in views:
            _add_entry(annotation_data, v["annotation"], v["id"])
            if v["annotation"] != "--":
                context_annotations.update_anatomical_entity(os.path.join(self._location, v["path"]), v["annotation"])

        for s in samples:
            _add_entry(annotation_data, s["annotation"], s["id"])
        
        return annotation_data
        
    def write_context_annotation(self):
        self.update_current_context_info()
        for context_info in self._context_info_list:
            context_info_location = context_annotations.get_context_info_file(context_info._fileName)
            data = context_info.get_context_json()
            context_annotations.write_context_info(context_info_location, data)
            annotation_data = self.create_annotation_data_json(data)
            context_annotations.update_additional_type(context_info_location)
            context_annotations.update_supplemental_json(context_info_location, json.dumps(annotation_data))

    def _open_annotation_map_file(self):
        _is_annotation_csv_file = False
        result = QtWidgets.QFileDialog.getOpenFileName(self, "Open annotation map file", self._previous_location)
        file_name = result[0]
        if file_name:
            self._previous_location = os.path.dirname(file_name)
            with open(file_name) as f:
                try:
                    result = csv.reader(f)
                except UnicodeDecodeError:
                    return

                _is_annotation_csv_file = is_annotation_csv_file(result)

        if _is_annotation_csv_file:
            self._ui.lineEditAnnotationMapFile.setText(file_name)
            self._load_view_annotations([file_name])

    def _load_view_annotations(self, annotation_files):
        scaffold_annotations = []
        for annotation_file in annotation_files:
            with open(annotation_file) as f:
                csv_reader = csv.reader(f)

                skip = True
                for row in csv_reader:
                    if skip:
                        skip = False
                    else:
                        scaffold_annotations.append(row)

        self._scaffold_annotations = scaffold_annotations
        self._update_view_annotations()

    def _on_metadata_changed(self, current_text):
        self.update_current_context_info()
        for context_info in self._context_info_list:
            if context_info._metadata_file in current_text:
                self._current_context_info = context_info
                self._populate_ui(self._current_context_info)
                return
        self.clean_ui()

    def update_current_context_info(self):
        self._current_context_info._context_heading = self._ui.lineEditSummaryHeading.text()
        self._current_context_info._context_description = self._ui.plainTextEditSummaryDescription.toPlainText()
        samples = []
        samples_tab_bar = self._ui.tabWidgetSamples.tabBar()
        for i in range(self._ui.tabWidgetSamples.count()):
            s = self._ui.tabWidgetSamples.widget(i)
            header = samples_tab_bar.tabText(i)
            samples.append(s.as_dict(header))

        views = []
        views_tab_bar = self._ui.tabWidgetViews.tabBar()
        for i in range(self._ui.tabWidgetViews.count()):
            v = self._ui.tabWidgetViews.widget(i)
            header = views_tab_bar.tabText(i)
            views.append(v.as_dict(header))

        self._current_context_info._views = views
        self._current_context_info._samples = samples

    def _update_view_annotations(self):
        for index in range(self._ui.tabWidgetViews.count()):
            self._ui.tabWidgetViews.widget(index).add_annotations(self._scaffold_annotations)

    def _next_tab_header(self, source):
        if source == "Sample":
            headers = self._sample_tab_headers()
        else:
            headers = self._view_tab_headers()

        count = 0
        next_header = f"{source} {count + 1}"
        while next_header in headers:
            count += 1
            next_header = f"{source} {count + 1}"

        return next_header

    def _sample_view_changed(self, value):
        tab_bar = self._ui.tabWidgetSamples.tabBar()
        sample = tab_bar.tabText(tab_bar.currentIndex())
        view_headers = self._view_tab_headers()
        view_index = view_headers.index(value)
        v = self._ui.tabWidgetViews.widget(view_index)
        v.set_sample(sample)

    def _view_sample_changed(self, value):
        tab_bar = self._ui.tabWidgetViews.tabBar()
        view = tab_bar.tabText(tab_bar.currentIndex())
        sample_headers = self._sample_tab_headers()
        sample_index = sample_headers.index(value)
        s = self._ui.tabWidgetSamples.widget(sample_index)
        s.set_view(view)

    def _samples_add_clicked(self):
        view_headers = self._view_tab_headers()
        sample_header = self._next_tab_header("Sample")
        sample = self._create_sample(sample_header)
        sample.populate_views(view_headers)

    def _create_sample(self, header):
        sample = SamplesWidget(self)
        sample.view_changed.connect(self._sample_view_changed)
        self._ui.tabWidgetSamples.addTab(sample, header)
        self._ui.tabWidgetSamples.setCurrentWidget(sample)
        self._add_sample_to_views(header)
        return sample

    def _views_add_clicked(self):
        sample_headers = self._sample_tab_headers()
        view_header = self._next_tab_header("View")
        view = self._create_view(view_header)
        view.populate_samples(sample_headers)

    def _create_view(self, header):
        view = ViewsWidget(self._scaffold_annotations, self)
        view.set_location(self._location)
        view.sample_changed.connect(self._view_sample_changed)
        self._ui.tabWidgetViews.addTab(view, header)
        self._ui.tabWidgetViews.setCurrentWidget(view)
        self._add_view_to_samples(header)
        return view

    def _view_tab_close_requested(self, index):
        view_headers_before = self._view_tab_headers()
        self._ui.tabWidgetViews.removeTab(index)
        removed_tab_header = view_headers_before[index]
        self._remove_view_from_samples(removed_tab_header)

    def _sample_tab_close_requested(self, index):
        sample_headers_before = self._sample_tab_headers()
        self._ui.tabWidgetSamples.removeTab(index)
        removed_tab_header = sample_headers_before[index]
        self._remove_sample_from_views(removed_tab_header)

    def _add_sample_to_views(self, sample):
        for i in range(self._ui.tabWidgetViews.count()):
            v = self._ui.tabWidgetViews.widget(i)
            v.add_sample(sample)

    def _add_view_to_samples(self, view):
        for i in range(self._ui.tabWidgetSamples.count()):
            s = self._ui.tabWidgetSamples.widget(i)
            s.add_view(view)

    def _remove_sample_from_views(self, sample):
        for i in range(self._ui.tabWidgetViews.count()):
            v = self._ui.tabWidgetViews.widget(i)
            v.remove_sample(sample)

    def _remove_view_from_samples(self, view):
        for i in range(self._ui.tabWidgetSamples.count()):
            s = self._ui.tabWidgetSamples.widget(i)
            s.remove_view(view)

    def _sample_tab_headers(self):
        tab_bar = self._ui.tabWidgetSamples.tabBar()
        count = tab_bar.count()
        return [tab_bar.tabText(i) for i in range(count)]

    def _view_tab_headers(self):
        tab_bar = self._ui.tabWidgetViews.tabBar()
        count = tab_bar.count()
        return [tab_bar.tabText(i) for i in range(count)]

def _build_list_model(annotation_items):
    model = QtGui.QStandardItemModel()
    for i in annotation_items:
        item = QtGui.QStandardItem(str(i))
        item.setData(i, QtCore.Qt.UserRole)
        item.setEditable(False)
        model.appendRow(item)
    return model
