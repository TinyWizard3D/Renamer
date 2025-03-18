# -*- coding: utf-8 -*-
import os
import imp
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QLayout, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QRadioButton, QButtonGroup, QFrame, QSpacerItem, QSizePolicy, QSplitter, QToolBar, QAction, QMainWindow

#--------Tools--------#
import renameFunctions as rf
import data
import generalFunctions as gef

#-------Reload Tool Scripts------#
imp.reload(rf)
imp.reload(gef)

class RenameUI(QWidget):
	def __init__(self, parent=None):
		super(RenameUI, self).__init__(parent)

		#----Setup----#
		self.initUI()

	def initUI(self):
		#-----variables-----#
		genf = gef.GeneralFunction()

		preList = ["C_", "L_", "R_"]
		suffList = ["_grp", "_geo", "_crv", "_ctl", "_jnt", "_R", "_L"]

		# Layout section
		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)


		# Prefix dropdown
		self.preDropdown = QComboBox(self)
		self.preDropdown.setEditable(True)
		self.preDropdown.addItems(preList)
		self.preDropdown.setCurrentText("")
		self.preDropdown.lineEdit().setPlaceholderText("Prefix")
		genf.setStyledTooltip(self.preDropdown, data.preTltpTitle, data.preTltp)
		self.preDropdown.setStyleSheet("width: 30px")
		self.layout.addWidget(self.preDropdown)

		# Rename textbox
		self.renameText = QLineEdit(self)
		self.renameText.setPlaceholderText("Rename/Replace")
		genf.setStyledTooltip(self.renameText, data.renameTltpTitle, data.renameTltp)
		self.layout.addWidget(self.renameText)

		# Replace textbox
		self.replaceText = QLineEdit(self)
		self.replaceText.setPlaceholderText("Replace With...")
		genf.setStyledTooltip(self.replaceText, data.replaceTltpTitle, data.replaceTltp)
		self.layout.addWidget(self.replaceText)

		# Suffix dropdown
		self.suffDropdown = QComboBox(self)
		self.suffDropdown.setEditable(True)
		self.suffDropdown.addItems(suffList)
		self.suffDropdown.setCurrentText("")
		self.suffDropdown.lineEdit().setPlaceholderText("Suffix")
		genf.setStyledTooltip(self.suffDropdown, data.suffTltpTitle, data.suffTltp)
		self.suffDropdown.setStyleSheet("width: 30px")
		self.layout.addWidget(self.suffDropdown)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		#------Padding------#
		# Padding Label
		paddingLabel = QLabel("Padding:")
		genf.setStyledTooltip(paddingLabel, data.paddingTltpTitle, data.paddingTltp)
		self.layout.addWidget(paddingLabel)

		# Amount of Padding
		self.paddingAmount = QSpinBox(self)
		self.paddingAmount.setRange(0, 999999)
		self.paddingAmount.setValue(0)
		genf.setStyledTooltip(self.paddingAmount, data.paddingTltpTitle, data.paddingTltp)
		self.layout.addWidget(self.paddingAmount)

		# Start Label
		startLabel = QLabel("Start:")
		genf.setStyledTooltip(startLabel, data.startTltpTitle, data.startTltp)
		self.layout.addWidget(startLabel)

		# Start of Padding
		self.paddingStart = QSpinBox(self)
		self.paddingStart.setRange(0, 999999)
		self.paddingStart.setValue(0)
		genf.setStyledTooltip(self.paddingStart, data.startTltpTitle, data.startTltp)
		self.layout.addWidget(self.paddingStart)

		# Step Label
		stepLabel = QLabel("Step:")
		genf.setStyledTooltip(stepLabel, data.stepTltpTitle, data.stepTltp)
		self.layout.addWidget(stepLabel)

		# Step of Padding
		self.stepAmount = QSpinBox(self)
		self.stepAmount.setRange(1, 999999)
		self.stepAmount.setValue(1)
		genf.setStyledTooltip(self.stepAmount, data.stepTltpTitle, data.stepTltp)
		self.layout.addWidget(self.stepAmount)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		#-----Text Capitalization-----#
		self.capGroup = QButtonGroup(self)
		self.capGroup.setExclusive(True)

		# Default button
		self.defaultBtn = QPushButton(self)
		genf.setButton(self.defaultBtn, self.layout, checked=True, checkable=True, tooltipTitle=data.defaultTltpTitle, tooltip=data.defaultTltp, isIcon=True, iconName="defaultIcon")
		self.capGroup.addButton(self.defaultBtn)

		# Uppercase button
		self.uppercaseBtn = QPushButton(self)
		genf.setButton(self.uppercaseBtn, self.layout, checkable=True, tooltipTitle=data.uppercaseTltpTitle, tooltip=data.uppercaseTltp, isIcon=True, iconName="upperIcon")
		self.capGroup.addButton(self.uppercaseBtn)

		# Lowercase button
		self.lowercaseBtn = QPushButton(self)
		genf.setButton(self.lowercaseBtn, self.layout, checkable=True, tooltipTitle=data.lowercaseTltpTitle, tooltip=data.lowercaseTltp, isIcon=True, iconName="lowerIcon")
		self.capGroup.addButton(self.lowercaseBtn)

		# Capitalize button
		self.capitalizeBtn = QPushButton(self)
		genf.setButton(self.capitalizeBtn, self.layout, checkable=True, tooltipTitle=data.capitalizeTltpTitle, tooltip=data.capitalizeTltp, isIcon=True, iconName="capitalIcon")
		self.capGroup.addButton(self.capitalizeBtn)

		# Default selection for button group
		#self.defaultBtn.setChecked(True)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		#-----Additions-----#
		# Include hierarchy button
		self.hierarchyBtn = QPushButton(self)
		genf.setButton(self.hierarchyBtn, self.layout, checkable=True, tooltipTitle=data.hierarchyTltpTitle, tooltip=data.hierarchyTltp, isIcon=True, iconName="hierarchyIcon")

		# Prefix dropdown
		self.typeDropdown = QComboBox(self)
		self.typeDropdown.addItems(data.typeList)
		genf.setStyledTooltip(self.typeDropdown, data.typeTltpHierarchyTitle, data.typeTltpHierarchy)
		self.layout.addWidget(self.typeDropdown)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# exclude selected button
		self.excludeBtn = QPushButton("")
		genf.setButton(self.excludeBtn, self.layout, checkable=True, tooltipTitle=data.excludeTltpTitle, tooltip=data.excludeTltp, isIcon=True, iconName="excludeSelectionIcon")


		# Include shapes button
		self.shapesBtn = QPushButton("")
		genf.setButton(self.shapesBtn, self.layout, checked=True, checkable=True, tooltipTitle=data.shapesTltpTitle, tooltip=data.shapesTltp, isIcon=True, iconName="shapeIcon")


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# Button that changes name of object according to the selected settings above
		renameBtn = QPushButton("Rename", self)
		genf.setButton(renameBtn, self.layout, text="Rename", tooltipTitle=data.renameBtnTltpTitle, tooltip=data.renameBtnTltp, isMainBtn=True, iconName="renameIcon")
		renameBtn.clicked.connect(self.renameClicked)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# Adds to all selected object a suffix according to type of object
		self.autoSuffixBtn = QPushButton("Auto Suffix")
		genf.setStyledTooltip(self.autoSuffixBtn, data.autoSuffixTltpTitle, data.autoSuffixTltp)
		self.autoSuffixBtn.clicked.connect(self.autoSuffix)
		self.layout.addWidget(self.autoSuffixBtn)


		#-----Finalization-----#
		self.setLayout(self.layout)

	def collectSettings(self):
		self.pre_Dropdown = self.preDropdown.currentText()
		self.rename_Text = self.renameText.text()
		self.replace_Text = self.replaceText.text()
		self.suff_Dropdown = self.suffDropdown.currentText()
		self.padding_Amount = self.paddingAmount.value()
		self.padding_Start = self.paddingStart.value()
		self.step_Amount = self.stepAmount.value()
		self.default_Btn = self.defaultBtn.isChecked()
		self.uppercase_Btn = self.uppercaseBtn.isChecked()
		self.lowercase_Btn = self.lowercaseBtn.isChecked()
		self.capitalize_Btn = self.capitalizeBtn.isChecked()
		self.hierarchy_Btn = self.hierarchyBtn.isChecked()
		self.type_Dropdown = self.typeDropdown.currentText()
		self.exclude_Btn = self.excludeBtn.isChecked()
		self.shapes_Btn = self.shapesBtn.isChecked()
		
		return {
			"prefixText": self.pre_Dropdown,
			"renameText": self.rename_Text,
			"replaceText": self.replace_Text,
			"suffixText": self.suff_Dropdown,
			"paddingAmount": self.padding_Amount,
			"paddingStart": self.padding_Start,
			"paddingStep": self.step_Amount,
			"defaultState": self.default_Btn,
			"uppercaseState": self.uppercase_Btn,
			"lowercaseState": self.lowercase_Btn,
			"capitalizeState": self.capitalize_Btn,
			"includeHierarchy": self.hierarchy_Btn,
			"hierarchyType": self.type_Dropdown,
			"excludeSelection": self.exclude_Btn,
			"includeShapes": self.shapes_Btn
		}

	def validateSettings(self, settings):
		#WRITE AND DECIDE ON PROPER VALIDATION FOR SETTINGS
		return True

	def renameClicked(self):
		settings = self.collectSettings()
		if self.validateSettings(settings):
			rf.RenameFunctions().renameObjects(settings)

	def autoSuffix(self):
		rf.RenameFunctions().autoSuffix()