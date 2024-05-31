# -*- coding: utf-8 -*-
import imp
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QRadioButton, QButtonGroup, QFrame, QSpacerItem, QSizePolicy, QSplitter, QToolBar, QAction, QMainWindow
#--------Tools--------#
import renameFunctions as rf
import data

#-------Reload Tool Scripts------#
imp.reload(rf)

class RenameUI(QWidget):
	def __init__(self, parent=None):
		super(RenameUI, self).__init__(parent)

		#----Setup----#
		self.initUI()

	def initUI(self):
		#-----variables-----#
		preList = ["C_", "L_", "R_"]
		suffList = ["_grp", "_geo", "_crv", "_ctl", "_jnt", "_R", "_L"]

		typeList = ["transform", "shape", "mesh", "joint", "locator", "nurbsCurve", "nurbsSurface", "ikHandle", "light", "camera"]

		# Tooltips
		preTltp = "PREFIX - Write, or select from a list, a prefix for selected object/s. If left empty, no prefix will be added"
		renameTltp = "RENAME/REPLACE - Writing text here will rename selected object/s to your input. If there's also input text in the Replace textbox, it will instead replace input in this textbox with the input in the Replace textbox for all selected objects."
		replaceTltp = "REPLACE-WITH - Writing text here will replace the input in 'Rename/Replace' with the one in this textbox for all selected objects. If 'Rename/Replace' is empty, it will instead rename all selected objects to your text input."
		suffTltp = "SUFFIX - Write, or select from a list, a suffix for selected object/s. If left empty, no suffix will be added"
		renameBtnTltp = "Click to rename all selected objects according to your chosen preferences"
		paddingTltp = "Choose how many zeros should be added to the all selected objects, example: 1, 01, 001, etc."
		startTltp = "Choose at which number the list of selects objects should start. Example-1: start at 1: obj_01, obj_02, etc. Example-2: start at 46: obj_46, obj_47, etc..."
		stepTltp = "Choose the amount of steps the list of selected objects should skip. Example-1: skip set to 1: obj_1, obj_2, etc. Example-2: skip set to 3: obj_1, obj_4, etc..."
		defaultTltp = "DEFAULT DECORATION - Renamed text will be unchanged from the way it was originally written"
		uppercaseTltp = "UPPERCASE - Check to make all copy of selected object/s 'UPPERCASE'"
		lowercaseTltp = "lowercase - Check to make all copy of selected object/s 'lowercase'"
		capitalizeTltp = "Capitalize - Check to make all copy of selected object/s 'Capitalize'"
		hierarchyTltp = "INCLUDE HIERARCHY - Check to rename all children and grandchildren under selected object/s"
		typeTltp = "TYPE TO INCLUDE - Specify which node type you would like to rename in the hierarchy."
		shapesTltp = "(RECOMMENDED) INCLUDE SHAPES - Check to also rename all shape nodes under selected object/s"
		excludeTltp = "EXCLUDE SELECTION - Excludes current selection from being renamed"
		autoSuffixTltp = ""


		# Layout section
		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)


		# Prefix dropdown
		self.preDropdown = QComboBox(self)
		self.preDropdown.setEditable(True)
		self.preDropdown.addItems(preList)
		self.preDropdown.setCurrentText("")
		self.preDropdown.lineEdit().setPlaceholderText("Prefix")
		self.preDropdown.setToolTip(preTltp)
		self.preDropdown.setStyleSheet("width: 30px")
		self.layout.addWidget(self.preDropdown)

		# Rename textbox
		self.renameText = QLineEdit(self)
		self.renameText.setPlaceholderText("Rename/Replace")
		self.renameText.setToolTip(renameTltp)
		self.layout.addWidget(self.renameText)

		# Replace textbox
		self.replaceText = QLineEdit(self)
		self.replaceText.setPlaceholderText("Replace With...")
		self.replaceText.setToolTip(replaceTltp)
		self.layout.addWidget(self.replaceText)

		# Suffix dropdown
		self.suffDropdown = QComboBox(self)
		self.suffDropdown.setEditable(True)
		self.suffDropdown.addItems(suffList)
		self.suffDropdown.setCurrentText("")
		self.suffDropdown.lineEdit().setPlaceholderText("Suffix")
		self.suffDropdown.setToolTip(suffTltp)
		self.suffDropdown.setStyleSheet("width: 30px")
		self.layout.addWidget(self.suffDropdown)


		#------------------
		self.addSeparator()
		#------------------


		#------Padding------#
		# Padding Label
		paddingLabel = QLabel("Padding:")
		paddingLabel.setToolTip(paddingTltp)
		self.layout.addWidget(paddingLabel)

		# Amount of Padding
		self.paddingAmount = QSpinBox(self)
		self.paddingAmount.setRange(0, 999999)
		self.paddingAmount.setValue(0)
		self.paddingAmount.setToolTip(paddingTltp)
		self.layout.addWidget(self.paddingAmount)

		# Start Label
		startLabel = QLabel("Start:")
		startLabel.setToolTip(startTltp)
		self.layout.addWidget(startLabel)

		# Start of Padding
		self.paddingStart = QSpinBox(self)
		self.paddingStart.setRange(0, 999999)
		self.paddingStart.setValue(0)
		self.paddingStart.setToolTip(startTltp)
		self.layout.addWidget(self.paddingStart)

		# Step Label
		stepLabel = QLabel("Step:")
		stepLabel.setToolTip(stepTltp)
		self.layout.addWidget(stepLabel)

		# Step of Padding
		self.stepAmount = QSpinBox(self)
		self.stepAmount.setRange(1, 999999)
		self.stepAmount.setValue(1)
		self.stepAmount.setToolTip(stepTltp)
		self.layout.addWidget(self.stepAmount)


		#------------------
		self.addSeparator()
		#------------------


		#-----Text Capitalization-----#
		self.capGroup = QButtonGroup(self)
		self.capGroup.setExclusive(True)

		# Default button
		self.defaultBtn = QPushButton("Def")
		self.defaultBtn.setCheckable(True)
		self.capGroup.addButton(self.defaultBtn)
		self.defaultBtn.setToolTip(defaultTltp)
		self.layout.addWidget(self.defaultBtn)

		# Uppercase button
		self.uppercaseBtn = QPushButton("UP")
		self.uppercaseBtn.setCheckable(True)
		self.capGroup.addButton(self.uppercaseBtn)
		self.uppercaseBtn.setToolTip(uppercaseTltp)
		self.layout.addWidget(self.uppercaseBtn)

		# Lowercase button
		self.lowercaseBtn = QPushButton("lo")
		self.lowercaseBtn.setCheckable(True)
		self.capGroup.addButton(self.lowercaseBtn)
		self.lowercaseBtn.setToolTip(lowercaseTltp)
		self.layout.addWidget(self.lowercaseBtn)

		# Capitalize button
		self.capitalizeBtn = QPushButton("Cap")
		self.capitalizeBtn.setCheckable(True)
		self.capGroup.addButton(self.capitalizeBtn)
		self.capitalizeBtn.setToolTip(capitalizeTltp)
		self.layout.addWidget(self.capitalizeBtn)

		# Default selection for button group
		self.defaultBtn.setChecked(True)


		#------------------
		self.addSeparator()
		#------------------


		#-----Additions-----#
		# Include hierarchy button
		self.hierarchyBtn = QPushButton("H")
		self.hierarchyBtn.setCheckable(True)
		self.hierarchyBtn.setToolTip(hierarchyTltp)
		self.layout.addWidget(self.hierarchyBtn)

		# Prefix dropdown
		self.typeDropdown = QComboBox(self)
		self.typeDropdown.addItems(data.typeList)
		self.typeDropdown.setToolTip(typeTltp)
		self.layout.addWidget(self.typeDropdown)


		#------------------
		self.addSeparator()
		#------------------


		# exclude selected button
		self.excludeBtn = QPushButton("E")
		self.excludeBtn.setCheckable(True)
		self.excludeBtn.setToolTip(excludeTltp)
		self.excludeBtn.setStyleSheet("width:10px")
		self.layout.addWidget(self.excludeBtn)


		# Include shapes button
		self.shapesBtn = QPushButton("S")
		self.shapesBtn.setCheckable(True)
		self.shapesBtn.setToolTip(shapesTltp)
		self.shapesBtn.setStyleSheet("width:10px")
		self.layout.addWidget(self.shapesBtn)

		self.shapesBtn.setChecked(True)


		#------------------
		self.addSeparator()
		#------------------


		# Button that changes name of object according to the selected settings above
		renameBtn = QPushButton("Rename", self)
		renameBtn.setToolTip(renameBtnTltp)
		renameBtn.clicked.connect(self.renameClicked)
		renameBtn.setStyleSheet("background-color: teal; width: 70px; height: 15px; padding-bottom: 2px;")
		self.layout.addWidget(renameBtn)


		#------------------
		self.addSeparator()
		#------------------


		# Adds to all selected object a suffix according to type of object
		self.autoSuffixBtn = QPushButton("Auto Suffix")
		self.autoSuffixBtn.setToolTip(autoSuffixTltp)
		self.autoSuffixBtn.clicked.connect(self.autoSuffix)
		self.layout.addWidget(self.autoSuffixBtn)


		#-----Finalization-----#
		self.setLayout(self.layout)
		#self.layout.addWidget(self.leftMenu)


	def addSeparator(self):
		separator = QFrame()
		separator.setFrameShape(QFrame.VLine)
		separator.setFrameShadow(QFrame.Sunken)

		self.layout.addWidget(separator)


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