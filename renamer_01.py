import sys
import imp
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QStackedWidget
from PySide2.QtGui import QPalette, QColor
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
#--------Tools--------#
import renameUI
import findUI

#-------Reload Tool Scripts------#
imp.reload(renameUI)
imp.reload(findUI)

#--------Code Starts Here--------#
widgetInstance = None
toolsList = ["Rename", "Find"]

def getMayaMainWindow():
		main_window_pointer = omui.MQtUtil.mainWindow()
		return wrapInstance(long(main_window_pointer), QWidget)

class Renamer(MayaQWidgetDockableMixin, QWidget):
	def __init__(self, parent=getMayaMainWindow()):

		#-----Setup-----#
		super(Renamer, self).__init__(parent)

		#-----Variables-----#
		self.initUI()

		self.setFixedHeight(28)

	def initUI(self):
		self.setWindowTitle('')  # Optional: Set an empty title

		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(3, 3, 0, 0)

		# Dropdown list to change layouts
		self.toolsDropdown = QComboBox(self)
		self.toolsDropdown.addItems(toolsList)
		self.toolsDropdown.currentIndexChanged.connect(self.changeCategory)
		self.layout.addWidget(self.toolsDropdown)

		# Stacked Widget
		self.stackedWidget = QStackedWidget(self)
		self.layout.addWidget(self.stackedWidget)

		self.rename_UI = renameUI.RenameUI()
		self.find_UI = findUI.FindUI()

		self.stackedWidget.addWidget(self.rename_UI)
		self.stackedWidget.addWidget(self.find_UI)

		#-----Finalization-----#
		self.setLayout(self.layout)
		self.changeCategory()

	def changeCategory(self):
		index = self.toolsDropdown.currentIndex()
		self.stackedWidget.setCurrentIndex(index)

def show_renamer():
	global widgetInstance

	# Close the existing instance if it exists
	if widgetInstance is not None:
		try:
			print("Closing existing instance")
			widgetInstance.close()
		except Exception as e:
			print("Error closing instance: {}".format(e))

	# Create and show a new instance
	try:
		widgetInstance = Renamer()
		widgetInstance.setObjectName('renamerWindow')

		# Delete existing workspace control if it exists
		if cmds.workspaceControl('renamerWorkspaceControl', q=True, exists=True):
			cmds.deleteUI('renamerWorkspaceControl', control=True)

		# Create and dock the control with proper layout
		cmds.workspaceControl(
			'renamerWorkspaceControl',
			label='Renamer',
			retain=False,
			floating=False,
			dockToMainWindow=("top", 1))
		controlLayout = omui.MQtUtil.findControl('renamerWorkspaceControl')
		controlPtr = wrapInstance(long(controlLayout), QWidget)
		controlPtr.layout().addWidget(widgetInstance)
	except Exception as e:
		print("Error showing instance: {}".format(e))