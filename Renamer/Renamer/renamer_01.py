# -*- coding: utf-8 -*-
import sys
import imp
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QStackedWidget, QFrame, QSpacerItem, QSizePolicy, QLayout, QToolTip
from PySide2.QtGui import QPalette, QColor, QFont
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import webbrowser
import maya.cmds as cmds
import pymel.core as pm
import re

#--------Tools--------#
from Renamer import renameUI, findUI, deleteUI, groupUI, data
from Renamer import generalFunctions as gef

#-------Reload Tool Scripts------#
imp.reload(renameUI)
imp.reload(findUI)
imp.reload(deleteUI)
imp.reload(groupUI)
imp.reload(data)
imp.reload(gef)

#--------Code Starts Here--------#
widgetInstance = None

QApplication.instance().setStyleSheet(data.tooltipStylesheet)

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

		genf = gef.GeneralFunction()

		self.layout = QHBoxLayout(self)

		self.layout.setContentsMargins(10, 0, 10, 0)

		self.rightMenu = QWidget()
		self.rightLayout = QHBoxLayout()
		self.rightLayout.setContentsMargins(0, 0, 0, 0)
		self.rightMenu.setLayout(self.rightLayout)
		#self.rightLayout.setSizeConstraint(QLayout.SetMinimumSize)

		self.leftMenu = QWidget()
		self.leftLayout = QHBoxLayout()
		self.leftLayout.setContentsMargins(0, 0, 0, 0)
		self.leftMenu.setLayout(self.leftLayout)
		#self.leftLayout.setSizeConstraint(QLayout.SetMinimumSize)

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
		self.descendingBtn = QPushButton("▼")
		genf.setButton(self.descendingBtn, self.rightLayout, text="▼", tooltipTitle=data.descendingTltpTitle, tooltip=data.descendingTltp)
		self.descendingBtn.clicked.connect(self.sortList)
		self.descendingBtn.setStyleSheet("width:20px")

		# Order ascending button
		self.ascendingBtn = QPushButton("▲")
		genf.setButton(self.ascendingBtn, self.rightLayout, text="▲", tooltipTitle=data.ascendingTltpTitle, tooltip=data.ascendingTltp)
		self.ascendingBtn.clicked.connect(self.reverseSortList)
		self.ascendingBtn.setStyleSheet("width:20px")

		#-----Help Button-----#
		self.helpBtn = QPushButton("?")
		genf.setButton(self.helpBtn, self.rightLayout, text="?", tooltipTitle=data.helpTltpTitle, tooltip=data.helpTltp)
		self.helpBtn.clicked.connect(lambda: webbrowser.open("https://slavbruner.vercel.app/tools/renamer"))
		self.helpBtn.setStyleSheet("width: 10px")

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

	dock_name = "renamerWorkspaceControl"

	# Restore if it already exists
	if cmds.workspaceControl(dock_name, q=True, exists=True):
		cmds.workspaceControl(dock_name, e=True, restore=True)
		return

	# Close existing instance properly
	if widgetInstance is not None:
		try:
			widgetInstance.close()
		except Exception as e:
			print(f"Error closing instance: {e}")

	try:
		widgetInstance = Renamer()
		widgetInstance.setObjectName("renamerWindow")  # Ensure unique object name

		# Create workspace control (DO NOT delete UI first)
		cmds.workspaceControl(dock_name, label="Renamer", retain=False, floating=False, dockToMainWindow=("top", 1))

		# Get control layout and attach the widget
		controlLayout = omui.MQtUtil.findControl(dock_name)
		controlPtr = wrapInstance(int(controlLayout), QWidget)
		controlPtr.layout().addWidget(widgetInstance)
	except Exception as e:
		print(f"Error showing instance: {e}")