import csv
import json
import os.path
import pathlib

from packaging.version import Version

from PySide6 import QtCore, QtGui, QtWidgets

from sparc.curation.tools.utilities import convert_to_bytes

from mapclientplugins.sparccurationhelperstep.helpers.ui_contextannotationwidget import Ui_ContextAnnotationWidget
from mapclientplugins.sparccurationhelperstep.helpers.sampleswidget import SamplesWidget
from mapclientplugins.sparccurationhelperstep.helpers.viewswidget import ViewsWidget

import sparc.curation.tools.context_annotations as context_annotations
from sparc.curation.tools.models.contextinfo import ContextInfoAnnotation
from sparc.curation.tools.helpers.file_helper import is_annotation_csv_file, OnDiskFiles, search_for_context_data_files


class ContextAnnotationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ContextAnnotationWidget, self).__init__(parent)
        self._ui = Ui_ContextAnnotationWidget()
        self._ui.setupUi(self)

        self._location = None

        self._previous_location = QtCore.QDir.homePath()
        self._scaffold_annotations = None
        self._context_info_list = []
        self._current_index = -1

        self._make_connections()

    def update_info(self, location):
        self._location = location
        metadata_files = OnDiskFiles().get_metadata_files()
        metadata_list = [*metadata_files]

        metadata_list_model = _build_list_model(metadata_list)
        self._ui.comboBoxContextMetadata.blockSignals(True)
        self._ui.comboBoxContextMetadata.setModel(metadata_list_model)
        self._current_index = 0
        self._ui.comboBoxContextMetadata.blockSignals(False)

        thumbnail_files = OnDiskFiles().get_all_image_files()

        thumbnail_list_model = _build_list_model(thumbnail_files)

        context_files = search_for_context_data_files(location, convert_to_bytes("2MiB"))
        # Upgrade old version 0.1.0 context info files. Load version 0.2.0 context info files.
        for context_file in context_files:
            with open(context_file, encoding='utf-8') as f:
                json_data = json.load(f)
                if Version(json_data['version']) == Version("0.1.0"):
                    # Associate this context information file with a metadata file in the same directory.
                    # Or, with any other single context information file.  Otherwise, report warning.
                    context_dir = os.path.dirname(context_file)
                    matching = [m for m in metadata_files if os.path.dirname(m) == context_dir]
                    metadata_file = None
                    if len(matching) == 1:
                        metadata_file = matching[0]
                    else:
                        if len(metadata_files) == 1:
                            metadata_file = metadata_files[0]

                    if metadata_file is None:
                        print('Warning: Could not match version 0.1.0 context information file to a scaffold metadata file, ignoring.')
                    else:
                        context_info = ContextInfoAnnotation(self.to_serialisable_path(metadata_file), context_file)
                        if 'banner' in json_data:
                            json_data['banner'] = pathlib.PureWindowsPath(json_data['banner']).as_posix()

                        modified_views = []
                        for v in json_data['views']:
                            v['path'] = pathlib.PureWindowsPath(v['path']).as_posix()
                            v['thumbnail'] = pathlib.PureWindowsPath(v['thumbnail']).as_posix()
                            modified_views.append(v)

                        json_data['views'] = modified_views

                        modified_samples = []
                        for s in json_data['samples']:
                            s['path'] = pathlib.PureWindowsPath(s['path']).as_posix()
                            modified_samples.append(s)

                        json_data['samples'] = modified_samples
                        context_info.update(json_data)
                        self._context_info_list.append(context_info)
                elif Version(json_data['version']) >= Version("0.2.0"):
                    context_info = ContextInfoAnnotation(self.to_serialisable_path(json_data['metadata']), context_file)
                    context_info.from_dict(json_data)
                    self._context_info_list.append(context_info)

        # Initial context data for metadata files without an associated existing context info file.
        for metadata_file in metadata_files:
            context_info_filename = metadata_file.rsplit(".", 1)[0] + "_context_info.json"
            metadata_path = self.to_serialisable_path(metadata_file)
            found = [ci.get_metadata_file() == metadata_path for ci in self._context_info_list]
            if not any(found):
                self._context_info_list.append(ContextInfoAnnotation(metadata_path, context_info_filename))

        # Basis of the interface relies on the context info list being the same size as the metadata files list.
        assert len(self._context_info_list) == len(metadata_files)

        self._ui.comboBoxBanner.blockSignals(True)
        self._ui.comboBoxBanner.setModel(thumbnail_list_model)
        self._ui.comboBoxBanner.blockSignals(False)
        if self._current_index != -1:
            self._populate_ui(self._context_info_list[self._current_index])

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
        self._ui.lineEditSummaryHeading.setText(data.get_heading())
        banner_index = self._ui.comboBoxBanner.findText(self._from_partial_path(data.get_banner()))
        if banner_index > -1:
            self._ui.comboBoxBanner.blockSignals(True)
            self._ui.comboBoxBanner.setCurrentIndex(banner_index)
            self._ui.comboBoxBanner.blockSignals(False)
        self._ui.plainTextEditSummaryDescription.setPlainText(data.get_description())
        for view in data.get_views():
            self._create_view(view["id"])

        for sample in data.get_samples():
            self._create_sample(sample["id"])
            self._add_sample_to_views(sample["id"])

        view_headers = self._view_tab_headers()
        for view_header in view_headers:
            self._add_view_to_samples(view_header)

        for i, view in enumerate(data.get_views()):
            v = self._ui.tabWidgetViews.widget(i)
            v.from_dict(view)

        for i, sample in enumerate(data.get_samples()):
            s = self._ui.tabWidgetSamples.widget(i)
            s.from_dict(sample)

    def _make_connections(self):
        self._ui.pushButtonAnnotationMapFile.clicked.connect(self._open_annotation_map_file)
        self._ui.pushButtonSamplesAdd.clicked.connect(self._samples_add_clicked)
        self._ui.pushButtonViewsAdd.clicked.connect(self._views_add_clicked)
        self._ui.tabWidgetSamples.tabCloseRequested.connect(self._sample_tab_close_requested)
        self._ui.tabWidgetViews.tabCloseRequested.connect(self._view_tab_close_requested)
        self._ui.comboBoxContextMetadata.currentTextChanged.connect(self._on_metadata_changed)
        self._ui.comboBoxBanner.currentTextChanged.connect(self._on_banner_changed)

    def write_context_annotation(self):
        self.update_current_context_info()
        for context_info in self._context_info_list:
            context_annotations.update_context_info(context_info)
            context_annotations.annotate_context_info(context_info)

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

    def _on_metadata_changed(self):
        # Apply any changes to the current context information.
        self.update_current_context_info()
        # Load the new context information.
        self._current_index = self._ui.comboBoxContextMetadata.currentIndex()
        self._populate_ui(self._context_info_list[self._current_index])

    def to_serialisable_path(self, path):
        return pathlib.PureWindowsPath(os.path.relpath(path, self._location)).as_posix() if path else ""

    def _from_partial_path(self, partial):
        return pathlib.PureWindowsPath(os.path.join(self._location, partial)).as_posix()

    def _on_banner_changed(self, current_text):
        self._context_info_list[self._current_index].update({
            "banner": self.to_serialisable_path(current_text)
        })

    def update_current_context_info(self):
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

        self._context_info_list[self._current_index].update({
            "banner": self.to_serialisable_path(self._ui.comboBoxBanner.currentText()),
            "heading": self._ui.lineEditSummaryHeading.text(),
            "description": self._ui.plainTextEditSummaryDescription.toPlainText(),
            "views": views,
            "samples": samples,
        })

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
