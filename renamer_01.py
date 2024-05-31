# -*- coding: utf-8 -*-
import sys
import imp
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QStackedWidget, QFrame, QSpacerItem, QSizePolicy
from PySide2.QtGui import QPalette, QColor
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import maya.cmds as cmds

#--------Tools--------#
import renameUI
import findUI
import deleteUI
import groupUI
import data

#-------Reload Tool Scripts------#
imp.reload(renameUI)
imp.reload(findUI)
imp.reload(deleteUI)
imp.reload(groupUI)
imp.reload(data)

#--------Code Starts Here--------#
widgetInstance = None

def getMayaMainWindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QWidget)

class Renamer(MayaQWidgetDockableMixin, QWidget):

	def __init__(self, parent=getMayaMainWindow()):

		#-----Setup-----#
		super(Renamer, self).__init__(parent)

		#-----Variables-----#
		self.initUI()

		self.setFixedHeight(23)

	def initUI(self):
		self.setWindowTitle('')

		# Tooltips
		ascendingTltp = "ASCENDING - Orders all selected objects in ascending order"
		descendingTltp = "DESCENDING - Orders all selected objects in descending order"
		helpTltp = "HELP - Opens the help menu"

		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(10, 0, 10, 0)

		self.rightMenu = QWidget()
		self.rightLayout = QHBoxLayout()
		self.rightLayout.setContentsMargins(0, 0, 0, 0)
		self.rightMenu.setLayout(self.rightLayout)

		self.leftMenu = QWidget()
		self.leftLayout = QHBoxLayout()
		self.leftLayout.setContentsMargins(0, 0, 0, 0)
		self.leftMenu.setLayout(self.leftLayout)

		# Dropdown list to change layouts
		self.toolsDropdown = QComboBox(self)
		self.toolsDropdown.addItems(data.toolsList)
		self.toolsDropdown.currentIndexChanged.connect(self.changeCategory)
		self.toolsDropdown.setStyleSheet("width: 54px")
		self.layout.addWidget(self.toolsDropdown)


		#------------------
		self.addSeparator()
		#------------------


		#-----Reordering Lists-----#
		# Order ascending button
		self.ascendingBtn = QPushButton("▼")
		self.ascendingBtn.setToolTip(ascendingTltp)
		self.ascendingBtn.clicked.connect(self.sortList)
		self.ascendingBtn.setStyleSheet("width:20px")
		self.rightLayout.addWidget(self.ascendingBtn)

		# Order ascending button
		self.descendingBtn = QPushButton("▲")
		self.descendingBtn.setToolTip(descendingTltp)
		self.descendingBtn.clicked.connect(self.reverseSortList)
		self.descendingBtn.setStyleSheet("width:20px")
		self.rightLayout.addWidget(self.descendingBtn)

		#-----Help Button-----#
		self.helpBtn = QPushButton("?")
		self.helpBtn.setToolTip(helpTltp)
		self.helpBtn.setStyleSheet("width: 10px")
		self.rightLayout.addWidget(self.helpBtn)

		# Stacked Widget
		self.stackedWidget = QStackedWidget(self)
		self.layout.addWidget(self.stackedWidget)

		self.rename_UI = renameUI.RenameUI()
		self.find_UI = findUI.FindUI()
		self.delete_UI = deleteUI.DeleteUI()
		self.group_UI = groupUI.GroupUI()

		self.stackedWidget.addWidget(self.rename_UI)
		self.stackedWidget.addWidget(self.find_UI)
		self.stackedWidget.addWidget(self.delete_UI)
		self.stackedWidget.addWidget(self.group_UI)

		#-----Finalization-----#
		self.setLayout(self.layout)
		spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
		self.layout.addItem(spacer)
		self.layout.addWidget(self.rightMenu)
		self.changeCategory()

	def changeCategory(self):
		index = self.toolsDropdown.currentIndex()
		self.stackedWidget.setCurrentIndex(index)

	def addSeparator(self):
		separator = QFrame()
		separator.setFrameShape(QFrame.VLine)
		separator.setFrameShadow(QFrame.Sunken)

		self.layout.addWidget(separator)

	# Sorting lists
	def sortList(self):
		try:
			pm.undoInfo(openChunk=True)
			
			selectedNodes = pm.ls(sl=True)

			sortedNodes = sorted(selectedNodes, key=self.natural_sort_key)

			start_index = self.findFirstIndex(selectedNodes)

			for node in sortedNodes:
				current_index = self.getNodeIndex(node)
				sorted_index = sortedNodes.index(node)
				if current_index is not None and sorted_index is not None:
					relative_move = sorted_index - current_index + start_index

					if relative_move != 0:
						pm.reorder(node, r=relative_move)

		finally:
			pm.undoInfo(closeChunk=True)


	def reverseSortList(self):
		try:
			pm.undoInfo(openChunk=True)
			
			selectedNodes = pm.ls(sl=True)

			sortedNodes = sorted(selectedNodes, key=self.natural_sort_key)
			sortedNodes.reverse()

			start_index = self.findFirstIndex(selectedNodes)

			for node in sortedNodes:
				current_index = self.getNodeIndex(node)
				sorted_index = sortedNodes.index(node)
				if current_index is not None and sorted_index is not None:
					relative_move = sorted_index - current_index + start_index

					if relative_move != 0:
						pm.reorder(node, r=relative_move)

		finally:
			pm.undoInfo(closeChunk=True)


	def getNodeIndex(self, node):
		parent = node.getParent()
		if parent:
			siblings = parent.listRelatives(children=True)
			return siblings.index(node)
		else:
			all_nodes = pm.ls(assemblies=True)
			return all_nodes.index(node)

	def natural_sort_key(self, s):
	    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s.name())]


	def findFirstIndex(self, nodeList):
		firstIndex = 0

		if (nodeList is not None):
			firstIndex = self.getNodeIndex(nodeList[0])
			for node in nodeList:
				nodeIndex = self.getNodeIndex(node)
				if nodeIndex < firstIndex:
					firstIndex = nodeIndex
		else:
			pm.error("No selected nodes.")
		
		return firstIndex

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
		controlPtr = wrapInstance(int(controlLayout), QWidget)
		controlPtr.layout().addWidget(widgetInstance)
	except Exception as e:
		print("Error showing instance: {}".format(e))