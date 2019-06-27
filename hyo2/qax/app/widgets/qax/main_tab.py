from PySide2 import QtCore, QtGui, QtWidgets

import os
import logging
logger = logging.getLogger(__name__)

from hyo2.abc.lib.helper import Helper

from hyo2.qax.app.gui_settings import GuiSettings
# Use NSURL as a workaround to pyside/Qt4 behaviour for dragging and dropping on OSx
if Helper.is_darwin():
    # noinspection PyUnresolvedReferences
    from Foundation import NSURL


class MainTab(QtWidgets.QMainWindow):

    here = os.path.abspath(os.path.dirname(__file__))

    def __init__(self, parent_win, prj):
        QtWidgets.QMainWindow.__init__(self)

        # store a project reference
        self.prj = prj
        self.parent_win = parent_win
        self.media = self.parent_win.media

        # ui
        self.panel = QtWidgets.QFrame()
        self.setCentralWidget(self.panel)
        self.vbox = QtWidgets.QVBoxLayout()
        self.panel.setLayout(self.vbox)

    #     self.loadData = QtWidgets.QGroupBox("Data inputs  [drap-and-drop to add, right click to drop files]")
    #     self.loadData.setStyleSheet("QGroupBox::title { color: rgb(155, 155, 155); }")
    #     self.vbox.addWidget(self.loadData)
    #
    #     vbox = QtWidgets.QVBoxLayout()
    #     self.loadData.setLayout(vbox)
    #
    #     vbox.addStretch()
    # #
    #     # add main window
    #     hbox = QtWidgets.QHBoxLayout()
    #     vbox.addLayout(hbox)
        # text_add_ss = QtWidgets.QLabel("Survey Soundings:")
        # hbox.addWidget(text_add_ss)
        # text_add_ss.setFixedHeight(GuiSettings.single_line_height())
        # text_add_ss.setMinimumWidth(90)
        # self.input_ss = QtWidgets.QListWidget()
        # hbox.addWidget(self.input_ss)
        # self.input_ss.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        # self.input_ss.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # # noinspection PyUnresolvedReferences
        # self.input_ss.customContextMenuRequested.connect(self.make_ss_context_menu)
        # self.input_ss.setAlternatingRowColors(True)
        # self.input_ss.setMaximumHeight(100)
        # # Enable dropping onto the input ss list
        # self.input_ss.setAcceptDrops(True)
        # self.input_ss.installEventFilter(self)
        # button_add_ss = QtWidgets.QPushButton()
        # hbox.addWidget(button_add_ss)
        # button_add_ss.setFixedHeight(GuiSettings.single_line_height())
        # button_add_ss.setFixedWidth(GuiSettings.single_line_height())
        # button_add_ss.setText(" + ")
        # button_add_ss.setToolTip('Add (or drag-and-drop) the survey soundings as S57 file (.000)')
        # # noinspection PyUnresolvedReferences
        # button_add_ss.clicked.connect(self.click_add_ss)

    #     # add dtm
    #     hbox = QtWidgets.QHBoxLayout()
    #     vbox.addLayout(hbox)
    #     text_add_dtm = QtWidgets.QLabel("Survey DTMs:")
    #     hbox.addWidget(text_add_dtm)
    #     text_add_dtm.setFixedHeight(GuiSettings.single_line_height())
    #     text_add_dtm.setMinimumWidth(90)
    #     self.input_dtm = QtWidgets.QListWidget()
    #     hbox.addWidget(self.input_dtm)
    #     self.input_dtm.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
    #     self.input_dtm.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    #     # noinspection PyUnresolvedReferences
    #     self.input_dtm.customContextMenuRequested.connect(self.make_dtm_context_menu)
    #     self.input_dtm.setAlternatingRowColors(True)
    #     self.input_dtm.setMaximumHeight(100)
    #     # Enable dropping onto the input ss list
    #     self.input_dtm.setAcceptDrops(True)
    #     self.input_dtm.installEventFilter(self)
    #     button_add_dtm = QtWidgets.QPushButton()
    #     hbox.addWidget(button_add_dtm)
    #     button_add_dtm.setFixedHeight(GuiSettings.single_line_height())
    #     button_add_dtm.setFixedWidth(GuiSettings.single_line_height())
    #     button_add_dtm.setText(" + ")
    #     button_add_dtm.setToolTip('Add (or drag-and-drop) the survey DTMs as geotiff or BAG files')
    #     # noinspection PyUnresolvedReferences
    #     button_add_dtm.clicked.connect(self.click_add_dtm)
    #
    #     vbox.addSpacing(10)
    #
    #     # add ENC
    #     hbox = QtWidgets.QHBoxLayout()
    #     vbox.addLayout(hbox)
    #     text_add_enc = QtWidgets.QLabel("Current ENCs:")
    #     hbox.addWidget(text_add_enc)
    #     text_add_enc.setFixedHeight(GuiSettings.single_line_height())
    #     text_add_enc.setMinimumWidth(90)
    #     self.input_enc = QtWidgets.QListWidget()
    #     hbox.addWidget(self.input_enc)
    #     self.input_enc.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
    #     self.input_enc.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    #     # noinspection PyUnresolvedReferences
    #     self.input_enc.customContextMenuRequested.connect(self.make_enc_context_menu)
    #     self.input_enc.setAlternatingRowColors(True)
    #     self.input_enc.setMaximumHeight(100)
    #     # Enable dropping onto the input s57 list
    #     self.input_enc.setAcceptDrops(True)
    #     self.input_enc.installEventFilter(self)
    #     button_add_enc = QtWidgets.QPushButton()
    #     hbox.addWidget(button_add_enc)
    #     button_add_enc.setFixedHeight(GuiSettings.single_line_height())
    #     button_add_enc.setFixedWidth(GuiSettings.single_line_height())
    #     button_add_enc.setText(" + ")
    #     button_add_enc.setToolTip('Add (or drag-and-drop) the current ENC as S57 file (.000)')
    #     # noinspection PyUnresolvedReferences
    #     button_add_enc.clicked.connect(self.click_add_enc)
    #
    #     vbox.addStretch()
    #
    #     # clear data
    #     hbox = QtWidgets.QHBoxLayout()
    #     vbox.addLayout(hbox)
    #     hbox.addStretch()
    #     button_clear_data = QtWidgets.QPushButton()
    #     hbox.addWidget(button_clear_data)
    #     button_clear_data.setFixedHeight(GuiSettings.single_line_height())
    #     # button_clear_data.setFixedWidth(GuiSettings.single_line_height())
    #     button_clear_data.setText("Clear data")
    #     button_clear_data.setToolTip('Clear all data loaded')
    #     # noinspection PyUnresolvedReferences
    #     button_clear_data.clicked.connect(self.click_clear_data)
    #     # info
    #     button = QtWidgets.QPushButton()
    #     hbox.addWidget(button)
    #     button.setFixedHeight(GuiSettings.single_line_height())
    #     button.setFixedWidth(GuiSettings.single_line_height())
    #     icon_info = QtCore.QFileInfo(os.path.join(self.media, 'small_info.png'))
    #     button.setIcon(QtGui.QIcon(icon_info.absoluteFilePath()))
    #     button.setToolTip('Open the manual page')
    #     button.setStyleSheet("QPushButton { background-color: rgba(255, 255, 255, 0); }\n"
    #                          "QPushButton:hover { background-color: rgba(230, 230, 230, 100); }\n")
    #     # noinspection PyUnresolvedReferences
    #     button.clicked.connect(self.click_open_manual)
    #     hbox.addStretch()
    #
    #     self.vbox.addStretch()
    #     self.vbox.addStretch()
    #
    #     # data outputs
    #     self.savedData = QtWidgets.QGroupBox("Data outputs [drap-and-drop the desired output folder]")
    #     self.savedData.setStyleSheet("QGroupBox::title { color: rgb(155, 155, 155); }")
    #     self.savedData.setMaximumHeight(GuiSettings.single_line_height() * 8)
    #     self.vbox.addWidget(self.savedData)
    #
    #     vbox = QtWidgets.QVBoxLayout()
    #     self.savedData.setLayout(vbox)
    #
    #     # set optional formats
    #     hbox = QtWidgets.QHBoxLayout()
    #     vbox.addLayout(hbox)
    #     text_set_formats = QtWidgets.QLabel("Formats:")
    #     hbox.addWidget(text_set_formats)
    #     text_set_formats.setFixedHeight(GuiSettings.single_line_height())
    #     text_set_formats.setMinimumWidth(64)
    #     self.output_pdf = QtWidgets.QCheckBox("PDF")
    #     self.output_pdf.setChecked(True)
    #     self.output_pdf.setDisabled(True)
    #     hbox.addWidget(self.output_pdf)
    #     self.output_s57 = QtWidgets.QCheckBox("S57")
    #     self.output_s57.setChecked(True)
    #     self.output_s57.setDisabled(True)
    #     hbox.addWidget(self.output_s57)
    #     self.output_shp = QtWidgets.QCheckBox("Shapefile")
    #     self.output_shp.setToolTip('Activate/deactivate the creation of Shapefiles in output')
    #     self.output_shp.setChecked(self.prj.output_shp)
    #     # noinspection PyUnresolvedReferences
    #     self.output_shp.clicked.connect(self.click_output_shp)
    #     hbox.addWidget(self.output_shp)
    #     self.output_kml = QtWidgets.QCheckBox("KML")
    #     self.output_kml.setToolTip('Activate/deactivate the creation of KML files in output')
    #     self.output_kml.setChecked(self.prj.output_kml)
    #     # noinspection PyUnresolvedReferences
    #     self.output_kml.clicked.connect(self.click_output_kml)
    #     hbox.addWidget(self.output_kml)
    #
    #     hbox.addSpacing(36)
    #
    #     text_set_prj_folder = QtWidgets.QLabel("Create project folder: ")
    #     hbox.addWidget(text_set_prj_folder)
    #     text_set_prj_folder.setFixedHeight(GuiSettings.single_line_height())
    #     self.output_prj_folder = QtWidgets.QCheckBox("")
    #     self.output_prj_folder.setToolTip('Create a sub-folder with project name')
    #     self.output_prj_folder.setChecked(self.prj.output_project_folder)
    #     # noinspection PyUnresolvedReferences
    #     self.output_prj_folder.clicked.connect(self.click_output_project_folder)
    #     hbox.addWidget(self.output_prj_folder)
    #
    #     text_set_subfolders = QtWidgets.QLabel("Per-tool sub-folders: ")
    #     hbox.addWidget(text_set_subfolders)
    #     text_set_subfolders.setFixedHeight(GuiSettings.single_line_height())
    #     self.output_subfolders = QtWidgets.QCheckBox("")
    #     self.output_subfolders.setToolTip('Create a sub-folder for each tool')
    #     self.output_subfolders.setChecked(self.prj.output_subfolders)
    #     # noinspection PyUnresolvedReferences
    #     self.output_subfolders.clicked.connect(self.click_output_subfolders)
    #     hbox.addWidget(self.output_subfolders)
    #
    #     hbox.addStretch()
    #
    #     # add folder
    #     hbox = QtWidgets.QHBoxLayout()
    #     vbox.addLayout(hbox)
    #     text_add_folder = QtWidgets.QLabel("Folder:")
    #     hbox.addWidget(text_add_folder)
    #     text_add_folder.setMinimumWidth(64)
    #     self.output_folder = QtWidgets.QListWidget()
    #     hbox.addWidget(self.output_folder)
    #     self.output_folder.setMinimumHeight(GuiSettings.single_line_height())
    #     self.output_folder.setMaximumHeight(GuiSettings.single_line_height() * 2)
    #     self.output_folder.clear()
    #     new_item = QtWidgets.QListWidgetItem()
    #     new_item.setIcon(QtGui.QIcon(os.path.join(self.parent_win.media, 'folder.png')))
    #     new_item.setText("%s" % self.prj.output_folder)
    #     new_item.setFont(GuiSettings.console_font())
    #     new_item.setForeground(GuiSettings.console_fg_color())
    #     self.output_folder.addItem(new_item)
    #     # Enable dropping onto the input ss list
    #     self.output_folder.setAcceptDrops(True)
    #     self.output_folder.installEventFilter(self)
    #     button_add_folder = QtWidgets.QPushButton()
    #     hbox.addWidget(button_add_folder)
    #     button_add_folder.setFixedHeight(GuiSettings.single_line_height())
    #     button_add_folder.setFixedWidth(GuiSettings.single_line_height())
    #     button_add_folder.setText(" .. ")
    #     button_add_folder.setToolTip('Add (or drag-and-drop) output folder')
    #     # noinspection PyUnresolvedReferences
    #     button_add_folder.clicked.connect(self.click_add_folder)
    #
    #     # open folder
    #     hbox = QtWidgets.QHBoxLayout()
    #     vbox.addLayout(hbox)
    #     hbox.addStretch()
    #
    #     button_default_output = QtWidgets.QPushButton()
    #     hbox.addWidget(button_default_output)
    #     button_default_output.setFixedHeight(GuiSettings.single_line_height())
    #     # button_open_output.setFixedWidth(GuiSettings.single_line_height())
    #     button_default_output.setText("Use default")
    #     button_default_output.setToolTip('Use the default output folder')
    #     # noinspection PyUnresolvedReferences
    #     button_default_output.clicked.connect(self.click_default_output)
    #
    #     button_open_output = QtWidgets.QPushButton()
    #     hbox.addWidget(button_open_output)
    #     button_open_output.setFixedHeight(GuiSettings.single_line_height())
    #     # button_open_output.setFixedWidth(GuiSettings.single_line_height())
    #     button_open_output.setText("Open folder")
    #     button_open_output.setToolTip('Open the output folder')
    #     # noinspection PyUnresolvedReferences
    #     button_open_output.clicked.connect(self.click_open_output)
    #
    #     hbox.addStretch()
    #
        # self.installEventFilter(self)
    #
    # def eventFilter(self, obj, e):
    #
    #     # drag events
    #     if (e.type() == QtCore.QEvent.DragEnter) or (e.type() == QtCore.QEvent.DragMove):
    #
    #         if obj in (self.input_dtm, ):
    #
    #             if e.mimeData().hasUrls:
    #
    #                 for url in e.mimeData().urls():
    #
    #                     if Helper.is_darwin():
    #                         dropping_file = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
    #
    #                     else:
    #                         dropping_file = str(url.toLocalFile())
    #
    #                     if os.path.splitext(dropping_file)[-1].lower() in (".bag", ".tiff", ".tif"):
    #                         e.accept()
    #                         return True
    #
    #         elif obj in (self.input_enc, self.input_ss):
    #
    #             if e.mimeData().hasUrls:
    #
    #                 for url in e.mimeData().urls():
    #
    #                     if Helper.is_darwin():
    #                         dropping_file = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
    #
    #                     else:
    #                         dropping_file = str(url.toLocalFile())
    #
    #                     if os.path.splitext(dropping_file)[-1].lower() in (".000", ):
    #                         e.accept()
    #                         return True
    #
    #         elif obj in (self.output_folder,):
    #
    #             if e.mimeData().hasUrls:
    #
    #                 for url in e.mimeData().urls():
    #
    #                     if Helper.is_darwin():
    #                         dropped_path = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
    #
    #                     else:
    #                         dropped_path = str(url.toLocalFile())
    #
    #                     dropped_path = os.path.abspath(dropped_path)
    #
    #                     if os.path.isdir(dropped_path):
    #                         e.accept()
    #                         return True
    #
    #         e.ignore()
    #         return True
    #
    #     # drop events
    #     if e.type() == QtCore.QEvent.Drop:
    #
    #         # print('drop', obj)
    #         if obj is self.input_dtm:
    #
    #             if e.mimeData().hasUrls():
    #
    #                 e.setDropAction(QtCore.Qt.CopyAction)
    #                 e.accept()
    #                 # Workaround for OSx dragging and dropping
    #                 for url in e.mimeData().urls():
    #                     if Helper.is_darwin():
    #                         dropped_file = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
    #                     else:
    #                         dropped_file = str(url.toLocalFile())
    #
    #                     logger.debug("dropped file: %s" % dropped_file)
    #                     if os.path.splitext(dropped_file)[-1] in (".bag", ".tiff", ".tif"):
    #
    #                         self._add_dtm(selection=dropped_file)
    #
    #                     else:
    #                         msg = 'Drag-and-drop is only possible with the following file extensions:\n' \
    #                               '- BAG files: .bag\n\n' \
    #                               '- GeoTIff files: .tif, .tiff\n\n' \
    #                               'Dropped file:\n' \
    #                               '%s' % dropped_file
    #                         # noinspection PyCallByClass,PyArgumentList
    #                         QtWidgets.QMessageBox.critical(self, "Drag-and-drop Error", msg, QtWidgets.QMessageBox.Ok)
    #                 return True
    #
    #         elif obj is self.input_enc:
    #
    #             if e.mimeData().hasUrls():
    #
    #                 e.setDropAction(QtCore.Qt.CopyAction)
    #                 e.accept()
    #                 # Workaround for OSx dragging and dropping
    #                 for url in e.mimeData().urls():
    #                     if Helper.is_darwin():
    #                         dropped_file = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
    #                     else:
    #                         dropped_file = str(url.toLocalFile())
    #
    #                     logger.debug("dropped file: %s" % dropped_file)
    #                     if os.path.splitext(dropped_file)[-1] in (".000",):
    #
    #                         self._add_enc(selection=dropped_file)
    #
    #                     else:
    #                         msg = 'Drag-and-drop is only possible with the following file extensions:\n' \
    #                               '- ENC S57 files: .000\n\n' \
    #                               'Dropped file:\n' \
    #                               '%s' % dropped_file
    #                         # noinspection PyCallByClass,PyArgumentList
    #                         QtWidgets.QMessageBox.critical(self, "Drag-and-drop Error", msg, QtWidgets.QMessageBox.Ok)
    #                 return True
    #
    #         elif obj is self.input_ss:
    #
    #             if e.mimeData().hasUrls():
    #
    #                 e.setDropAction(QtCore.Qt.CopyAction)
    #                 e.accept()
    #                 # Workaround for OSx dragging and dropping
    #                 for url in e.mimeData().urls():
    #                     if Helper.is_darwin():
    #                         dropped_file = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
    #                     else:
    #                         dropped_file = str(url.toLocalFile())
    #
    #                     logger.debug("dropped file: %s" % dropped_file)
    #                     if os.path.splitext(dropped_file)[-1] in (".000",):
    #                         self._add_ss(selection=dropped_file)
    #                     else:
    #                         msg = 'Drag-and-drop is only possible with the following file extensions:\n' \
    #                               '- Survey Soundings S57 files: .000\n\n' \
    #                               'Dropped file:\n' \
    #                               '%s' % dropped_file
    #                         # noinspection PyCallByClass,PyArgumentList
    #                         QtWidgets.QMessageBox.critical(self, "Drag-and-drop Error", msg, QtWidgets.QMessageBox.Ok)
    #                 return True
    #
    #         elif obj is self.output_folder:
    #
    #             if e.mimeData().hasUrls():
    #
    #                 e.setDropAction(QtCore.Qt.CopyAction)
    #                 e.accept()
    #                 # Workaround for OSx dragging and dropping
    #                 for url in e.mimeData().urls():
    #
    #                     if Helper.is_darwin():
    #                         dropped_path = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
    #
    #                     else:
    #                         dropped_path = str(url.toLocalFile())
    #
    #                     dropped_path = os.path.abspath(dropped_path)
    #
    #                     logger.debug("dropped file: %s" % dropped_path)
    #                     if os.path.isdir(dropped_path):
    #                         self._add_folder(selection=dropped_path)
    #
    #                     else:
    #                         msg = 'Drag-and-drop is only possible with a single folder\n'
    #                         # noinspection PyCallByClass,PyArgumentList
    #                         QtWidgets.QMessageBox.critical(self, "Drag-and-drop Error", msg, QtWidgets.QMessageBox.Ok)
    #
    #                 return True
    #
    #         e.ignore()
    #         return True
    #
    #     return QtWidgets.QMainWindow.eventFilter(self, obj, e)
    #
    # # DTM METHODS
    #
    # def click_add_dtm(self):
    #     """ Read the DTM files provided by the user"""
    #     logger.debug('adding DTM ...')
    #
    #     # ask the file path to the user
    #     # noinspection PyCallByClass
    #     selections, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Add DTM file",
    #                                                            QtCore.QSettings().value("dtm_import_folder"),
    #                                                            "Supported formats (*.bag *.tif *.tiff);; "
    #                                                            "BAG file (*.bag);;GeoTiff file (*.tif *.tiff);;"
    #                                                            "All files (*.*)")
    #     if len(selections) == 0:
    #         logger.debug('adding dtm: aborted')
    #         return
    #     last_open_folder = os.path.dirname(selections[0])
    #     if os.path.exists(last_open_folder):
    #         QtCore.QSettings().setValue("dtm_import_folder", last_open_folder)
    #
    #     for selection in selections:
    #         selection = os.path.abspath(selection).replace("\\", "/")
    #         self._add_dtm(selection=selection)
    #
    # def _add_dtm(self, selection):
    #
    #     # attempt to read the data
    #     try:
    #         self.prj.add_input_dtm_path(selection)
    #
    #     except Exception as e:  # more general case that catches all the exceptions
    #         msg = '<b>Error setting \"%s\".</b>' % selection
    #         msg += '<br><br><font color=\"red\">%s</font>' % e
    #         # noinspection PyCallByClass,PyArgumentList
    #         QtWidgets.QMessageBox.critical(self, "Data Setting Error", msg, QtWidgets.QMessageBox.Ok)
    #         logger.error('DTM file NOT added: %s' % selection)
    #         return
    #
    #     self._update_input_dtm_list()
    #     self.parent_win.dtm_loaded()
    #
    # def _update_input_dtm_list(self):
    #     self.input_dtm.clear()
    #     for input_dtm_path in self.prj.input_dtm_paths:
    #         new_item = QtWidgets.QListWidgetItem()
    #         if os.path.splitext(input_dtm_path)[-1] == ".bag":
    #             new_item.setIcon(QtGui.QIcon(os.path.join(self.parent_win.media, 'bag.png')))
    #         elif os.path.splitext(input_dtm_path)[-1] in [".tif", ".tiff"]:
    #             new_item.setIcon(QtGui.QIcon(os.path.join(self.parent_win.media, 'tif.png')))
    #         new_item.setText(input_dtm_path)
    #         new_item.setFont(GuiSettings.console_font())
    #         new_item.setForeground(GuiSettings.console_fg_color())
    #         self.input_dtm.addItem(new_item)
    #
    # def make_dtm_context_menu(self, pos):
    #     logger.debug('context menu')
    #
    #     # # check if any selection
    #     # sel = self.input_ss.selectedItems()
    #     # # noinspection PyArgumentList
    #     # if len(sel) == 0:
    #     #     # noinspection PyCallByClass,PyArgumentList
    #     #     QtWidgets.QMessageBox.information(self, "SS list", "You need to first add and select one or more files!")
    #     #     return
    #
    #     remove_act = QtWidgets.QAction("Remove files", self, statusTip="Remove DTM files",
    #                                    triggered=self.remove_dtm_files)
    #
    #     menu = QtWidgets.QMenu(parent=self)
    #     # noinspection PyArgumentList
    #     menu.addAction(remove_act)
    #     # noinspection PyArgumentList
    #     menu.exec_(self.input_dtm.mapToGlobal(pos))
    #
    # def remove_dtm_files(self):
    #     logger.debug("user want to remove DTM files")
    #
    #     self.prj.clear_input_dtm_paths()
    #     self._update_input_dtm_list()
    #     self.parent_win.dtm_unloaded()
    #
    # # SS METHODS
    #
    # def click_add_ss(self):
    #     """ Read the SS files provided by the user"""
    #     logger.debug('adding SS features from file ...')
    #
    #     # ask the file path to the user
    #     # noinspection PyCallByClass
    #     selections, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Add SS file",
    #                                                            QtCore.QSettings().value("ss_import_folder"),
    #                                                            "S57 file (*.000);;All files (*.*)")
    #     if len(selections) == 0:
    #         logger.debug('adding ss: aborted')
    #         return
    #     last_open_folder = os.path.dirname(selections[0])
    #     if os.path.exists(last_open_folder):
    #         QtCore.QSettings().setValue("ss_import_folder", last_open_folder)
    #
    #     for selection in selections:
    #         selection = os.path.abspath(selection).replace("\\", "/")
    #         self._add_ss(selection=selection)
    #
    # def _add_ss(self, selection):
    #
    #     # attempt to read the data
    #     try:
    #         self.prj.add_input_ss_path(selection)
    #
    #     except Exception as e:  # more general case that catches all the exceptions
    #         msg = '<b>Error setting \"%s\".</b>' % selection
    #         msg += '<br><br><font color=\"red\">%s</font>' % e
    #         # noinspection PyCallByClass,PyArgumentList
    #         QtWidgets.QMessageBox.critical(self, "Data Setting Error", msg, QtWidgets.QMessageBox.Ok)
    #         logger.error('S57 file NOT added: %s' % selection)
    #         return
    #
    #     self._update_input_ss_list()
    #     self.parent_win.ss_loaded()
    #
    # def _update_input_ss_list(self):
    #     self.input_ss.clear()
    #     for input_ss_path in self.prj.input_ss_paths:
    #         new_item = QtWidgets.QListWidgetItem()
    #         if os.path.splitext(input_ss_path)[-1] == ".000":
    #             new_item.setIcon(QtGui.QIcon(os.path.join(self.parent_win.media, 's57.png')))
    #         new_item.setText(input_ss_path)
    #         new_item.setFont(GuiSettings.console_font())
    #         new_item.setForeground(GuiSettings.console_fg_color())
    #         self.input_ss.addItem(new_item)
    #
    # def make_ss_context_menu(self, pos):
    #     logger.debug('context menu')
    #
    #     # # check if any selection
    #     # sel = self.input_ss.selectedItems()
    #     # # noinspection PyArgumentList
    #     # if len(sel) == 0:
    #     #     # noinspection PyCallByClass,PyArgumentList
    #     #     QtWidgets.QMessageBox.information(self, "SS list", "You need to first add and select one or more files!")
    #     #     return
    #
    #     remove_act = QtWidgets.QAction("Remove files", self, statusTip="Remove SS files",
    #                                    triggered=self.remove_ss_files)
    #
    #     menu = QtWidgets.QMenu(parent=self)
    #     # noinspection PyArgumentList
    #     menu.addAction(remove_act)
    #     # noinspection PyArgumentList
    #     menu.exec_(self.input_ss.mapToGlobal(pos))
    #
    # def remove_ss_files(self):
    #     logger.debug("user want to remove SS files")
    #
    #     self.prj.clear_input_ss_paths()
    #     self._update_input_ss_list()
    #     self.parent_win.ss_unloaded()
    #
    # # ENC methods
    #
    # def click_add_enc(self):
    #     """ Read the S57 files provided by the user"""
    #     logger.debug('adding ENC features from file ...')
    #
    #     # ask the file path to the user
    #     # noinspection PyCallByClass
    #     selections, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Add ENC features",
    #                                                            QtCore.QSettings().value("enc_import_folder"),
    #                                                            "S57 file (*.000);;All files (*.*)")
    #     if len(selections) == 0:
    #         logger.debug('adding s57: aborted')
    #         return
    #     last_open_folder = os.path.dirname(selections[0])
    #     if os.path.exists(last_open_folder):
    #         QtCore.QSettings().setValue("enc_import_folder", last_open_folder)
    #
    #     for selection in selections:
    #         selection = os.path.abspath(selection).replace("\\", "/")
    #         self._add_enc(selection=selection)
    #
    # def _add_enc(self, selection):
    #
    #     # attempt to read the data
    #     try:
    #         self.parent_win.prj.add_input_enc_path(selection)
    #
    #     except Exception as e:  # more general case that catches all the exceptions
    #         msg = '<b>Error setting \"%s\".</b>' % selection
    #         msg += '<br><br><font color=\"red\">%s</font>' % e
    #         # noinspection PyCallByClass,PyArgumentList
    #         QtWidgets.QMessageBox.critical(self, "Data Setting Error", msg, QtWidgets.QMessageBox.Ok)
    #         logger.error('ENC file NOT added: %s' % selection)
    #         return
    #
    #     self._update_input_enc_list()
    #     self.parent_win.enc_loaded()
    #
    # def _update_input_enc_list(self):
    #     """ update the ENC list widget """
    #     self.input_enc.clear()
    #     for input_enc_path in self.prj.input_enc_paths:
    #         new_item = QtWidgets.QListWidgetItem()
    #         if os.path.splitext(input_enc_path)[-1] == ".000":
    #             new_item.setIcon(QtGui.QIcon(os.path.join(self.parent_win.media, 's57.png')))
    #         new_item.setText(input_enc_path)
    #         new_item.setFont(GuiSettings.console_font())
    #         new_item.setForeground(GuiSettings.console_fg_color())
    #         self.input_enc.addItem(new_item)
    #
    # def make_enc_context_menu(self, pos):
    #     logger.debug('ENC context menu')
    #
    #     # # check if any selection
    #     # sel = self.input_enc.selectedItems()
    #     # if len(sel) == 0:
    #     #     # noinspection PyCallByClass,PyArgumentList
    #     #     QtWidgets.QMessageBox.information(self, "ENC list", "You need to first add and select one or more files!")
    #     #     return
    #
    #     remove_act = QtWidgets.QAction("Remove files", self, statusTip="Remove the ENC files",
    #                                    triggered=self.remove_enc_files)
    #
    #     menu = QtWidgets.QMenu(parent=self)
    #     # noinspection PyArgumentList
    #     menu.addAction(remove_act)
    #     # noinspection PyArgumentList
    #     menu.exec_(self.input_enc.mapToGlobal(pos))
    #
    # def remove_enc_files(self):
    #     logger.debug("user want to remove ENC files")
    #
    #     self.prj.clear_input_enc_paths()
    #     self.parent_win.enc_unloaded()
    #     self._update_input_enc_list()
    #
    # # AUX METHODS
    #
    # def click_clear_data(self):
    #     """ Clear all the read data"""
    #     logger.debug('clear data')
    #     self.parent_win.prj.clear_data()
    #
    #     self.input_enc.clear()
    #     self.parent_win.enc_unloaded()
    #
    #     self.input_dtm.clear()
    #     self.parent_win.dtm_unloaded()
    #
    #     self.input_ss.clear()
    #     self.parent_win.ss_unloaded()
    #
    # def click_output_kml(self):
    #     """ Set the KML output"""
    #     self.prj.output_kml = self.output_kml.isChecked()
    #     QtCore.QSettings().setValue("enc_export_kml", self.prj.output_kml)
    #
    # def click_output_shp(self):
    #     """ Set the Shapefile output"""
    #     self.prj.output_shp = self.output_shp.isChecked()
    #     QtCore.QSettings().setValue("enc_export_shp", self.prj.output_shp)
    #
    # def click_output_project_folder(self):
    #     """ Set the output project folder"""
    #     self.prj.output_project_folder = self.output_prj_folder.isChecked()
    #     QtCore.QSettings().setValue("enc_export_project_folder", self.prj.output_project_folder)
    #
    # def click_output_subfolders(self):
    #     """ Set the output in sub-folders"""
    #     self.prj.output_subfolders = self.output_subfolders.isChecked()
    #     QtCore.QSettings().setValue("enc_export_subfolders", self.prj.output_subfolders)
    #
    # def click_add_folder(self):
    #     """ Read the grids provided by the user"""
    #     logger.debug('set output folder ...')
    #
    #     # ask the output folder
    #     # noinspection PyCallByClass
    #     selection = QtWidgets.QFileDialog.getExistingDirectory(self, "Set output folder",
    #                                                            QtCore.QSettings().value("enc_export_folder"),)
    #     if selection == "":
    #         logger.debug('setting output folder: aborted')
    #         return
    #     logger.debug("selected path: %s" % selection)
    #
    #     self._add_folder(selection)
    #
    # def _add_folder(self, selection):
    #
    #     path_len = len(selection)
    #     logger.debug("folder path length: %d" % path_len)
    #     if path_len > 140:
    #
    #         msg = 'The selected path is %d characters long. ' \
    #               'This may trigger the filename truncation of generated outputs (max allowed path length: 260).\n\n' \
    #               'Do you really want to use: %s?' % (path_len, selection)
    #         msg_box = QtWidgets.QMessageBox(self)
    #         msg_box.setWindowTitle("Output folder")
    #         msg_box.setText(msg)
    #         msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    #         msg_box.setDefaultButton(QtWidgets.QMessageBox.No)
    #         reply = msg_box.exec_()
    #
    #         if reply == QtWidgets.QMessageBox.No:
    #             return
    #
    #     try:
    #         self.prj.output_folder = os.path.abspath(selection).replace("\\", "/")
    #
    #     except Exception as e:  # more general case that catches all the exceptions
    #         msg = '<b>Error setting the output folder to \"%s\".</b>' % selection
    #         msg += '<br><br><font color=\"red\">%s</font>' % e
    #         # noinspection PyCallByClass,PyArgumentList
    #         QtWidgets.QMessageBox.critical(self, "Output Folder Error", msg, QtWidgets.QMessageBox.Ok)
    #         logger.debug('output folder NOT set: %s' % selection)
    #         return
    #
    #     self.output_folder.clear()
    #     new_item = QtWidgets.QListWidgetItem()
    #     new_item.setIcon(QtGui.QIcon(os.path.join(self.parent_win.media, 'folder.png')))
    #     new_item.setText("%s" % self.prj.output_folder)
    #     new_item.setFont(GuiSettings.console_font())
    #     new_item.setForeground(GuiSettings.console_fg_color())
    #     self.output_folder.addItem(new_item)
    #
    #     QtCore.QSettings().setValue("enc_export_folder", self.prj.output_folder)
    #
    #     logger.debug("new output folder: %s" % self.prj.output_folder)
    #
    # def click_default_output(self):
    #     """ Set default output data folder """
    #     self._add_folder(selection=self.prj.default_output_folder())
    #
    # def click_open_output(self):
    #     """ Open output data folder """
    #     logger.debug('open output folder: %s' % self.prj.output_folder)
    #     self.prj.open_output_folder()
    #
    # # common
    # @classmethod
    # def click_open_manual(cls):
    #     logger.debug("open manual")
    #     Helper.explore_folder("https://www.hydroffice.org/manuals/catools/user_manual_enc_data_inputs.html")
