import csv
import json
import os.path

from PySide2 import QtCore, QtWidgets

from mapclientplugins.sparccurationhelperstep.helpers.ui_contextannotationwidget import Ui_ContextAnnotationWidget
from mapclientplugins.sparccurationhelperstep.helpers.sampleswidget import SamplesWidget
from mapclientplugins.sparccurationhelperstep.helpers.viewswidget import ViewsWidget


class ContextAnnotationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ContextAnnotationWidget, self).__init__(parent)
        self._ui = Ui_ContextAnnotationWidget()
        self._ui.setupUi(self)

        self._previous_location = QtCore.QDir.homePath()
        self._scaffold_annotations = None

        self._make_connections()

    def _make_connections(self):
        self._ui.pushButtonAnnotationMapFile.clicked.connect(self._open_annotation_map_file)
        self._ui.pushButtonSamplesAdd.clicked.connect(self._samples_add_clicked)
        self._ui.pushButtonViewsAdd.clicked.connect(self._views_add_clicked)
        self._ui.tabWidgetSamples.tabCloseRequested.connect(self._sample_tab_close_requested)
        self._ui.tabWidgetViews.tabCloseRequested.connect(self._view_tab_close_requested)
        self._ui.pushButtonWriteAnnotation.clicked.connect(self._write_annotation_clicked)

    def _write_annotation_clicked(self):
        context_heading = self._ui.lineEditSummaryHeading.text()
        context_description = self._ui.plainTextEditSummaryDescription.toPlainText()

        data = {
            "version": "0.1.0",
            "heading": context_heading,
            "description": context_description,
            "samples": [],
            "views": [],
        }

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

        data["views"] = views
        data["samples"] = samples

        print(json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=2))

        annotation_data = {}

        for v in views:
            if v["annotation"]:
                annotation_data[v["annotation"]] = v["id"]

        for s in samples:
            if s["annotation"]:
                annotation_data[s["annotation"]] = s["id"]

        print(json.dumps(annotation_data, default=lambda o: o.__dict__, sort_keys=True, indent=2))

    def _open_annotation_map_file(self):
        result = QtWidgets.QFileDialog.getOpenFileName(self, "Open annotation map file", self._previous_location)
        file_name = result[0]
        if file_name:
            self._previous_location = os.path.dirname(file_name)
            with open(file_name) as f:
                try:
                    result = csv.reader(f)
                except UnicodeDecodeError:
                    return

                if _is_annotation_map_data(result):
                    f.seek(0)
                    scaffold_annotations = []
                    self._scaffold_annotations = None

                    self._ui.lineEditAnnotationMapFile.setText(file_name)
                    skip = True
                    for row in result:
                        if skip:
                            skip = False
                        else:
                            scaffold_annotations.append(row)

                    if scaffold_annotations:
                        self._scaffold_annotations = scaffold_annotations

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
        sample = SamplesWidget(view_headers)
        sample.view_changed.connect(self._sample_view_changed)
        sample_header = self._next_tab_header("Sample")
        self._ui.tabWidgetSamples.addTab(sample, sample_header)
        self._add_sample_to_views(sample_header)

    def _views_add_clicked(self):
        sample_headers = self._sample_tab_headers()
        view = ViewsWidget(sample_headers, self._scaffold_annotations)
        view.sample_changed.connect(self._view_sample_changed)
        view_header = self._next_tab_header("View")
        self._ui.tabWidgetViews.addTab(view, view_header)
        self._add_view_to_samples(view_header)

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
            v = self._ui.tabWidgetSamples.widget(i)
            v.add_view(view)

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


def _is_annotation_map_data(data):
    first = True
    for row in data:
        if first:
            if len(row) == 2 and row[0] == "Term ID" and row[1] == "Group name":
                first = False
            else:
                return False
        elif len(row) != 2:
            return False

    return True
