from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QLineEdit, QComboBox, QFrame
import imp
import data
import generalFunctions as gef

#--------Tools--------#
import findFunctions as ff

#-------Reload Tool Scripts------#
imp.reload(ff)
imp.reload(gef)

class FindUI(QWidget):
	def __init__(self, parent=None):
		super(FindUI, self).__init__(parent)
		self.initUI()

	def initUI(self):
		genf = gef.GeneralFunction()

		# Layout section
		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)

		# Label to change
		self.findBox = QLineEdit(self)
		self.findBox.setPlaceholderText("Search & Select")
		self.layout.addWidget(self.findBox)

		# Prefix dropdown
		self.typeDropdown = QComboBox(self)
		self.typeDropdown.addItems(data.typeList)
		genf.setStyledTooltip(self.typeDropdown, data.typeTltpTitle, data.typeTltp)
		#self.typeDropdown.setToolTip(data.typeTltp)
		self.typeDropdown.setStyleSheet("width: 100px")
		self.layout.addWidget(self.typeDropdown)

		# Button that changes label
		selectButton = QPushButton("Select", self)
		genf.setButton(selectButton, self.layout, text="Select", isMainBtn=True, iconName="selectIcon")
		selectButton.clicked.connect(self.selectClicked)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# Find Duplicates button
		self.duplicateBtn = QPushButton(self)
		genf.setButton(self.duplicateBtn, self.layout, tooltip=data.duplicateTltp, isIcon=True, iconName="duplicatesIcon")
		self.duplicateBtn.clicked.connect(self.findDuplicates)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# Print and save button
		self.printBtn = QPushButton("Save Selected")
		genf.setStyledTooltip(self.printBtn, data.duplicateTltpTitle, data.duplicateTltp)
		#self.printBtn.setToolTip(data.duplicateTltp)
		self.printBtn.clicked.connect(self.printSave)
		self.layout.addWidget(self.printBtn)

		# Select saved button
		self.savedBtn = QPushButton("Load Selection")
		genf.setStyledTooltip(self.savedBtn, data.savedTltpTitle, data.savedTltp)
		#self.savedBtn.setToolTip(data.savedTltp)
		self.savedBtn.clicked.connect(self.selectSaved)
		self.layout.addWidget(self.savedBtn)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# Select bound joints button
		self.boundJointsBtn = QPushButton(self)
		genf.setButton(self.boundJointsBtn, self.layout, tooltip=data.boundJointsTltp, isIcon=True, iconName="boundJointsIcon")
		self.boundJointsBtn.clicked.connect(self.selectBoundJoints)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# Select 5 vert influeces button
		self.fiveVertsBtn = QPushButton(self)
		genf.setButton(self.fiveVertsBtn, self.layout, tooltip=data.fiveVertsTltp, isIcon=True, iconName="selectVerticesIcon")
		self.fiveVertsBtn.clicked.connect(self.selectMultipleInfluence)

		# Joint Influence Label
		typeLabel = QLabel("Influence:")
		self.layout.addWidget(typeLabel)

		# Amount of Influences
		self.influenceAmount = QSpinBox(self)
		self.influenceAmount.setRange(0, 999999)
		self.influenceAmount.setValue(0)
		genf.setStyledTooltip(self.influenceAmount, data.influenceTltpTitle, data.influenceTltp)
		#self.influenceAmount.setToolTip(data.influenceTltp)
		self.layout.addWidget(self.influenceAmount)

		self.setLayout(self.layout)

	def collectSettings(self):
		self.find_Box = self.findBox.text()
		self.type_Dropdown = self.typeDropdown.currentText()
		
		return {
			"findText": self.find_Box,
			"selectType": self.type_Dropdown,
		}

	def validateSettings(self, settings):
		#WRITE AND DECIDE ON PROPER VALIDATION FOR SETTINGS
		return True

	def selectClicked(self):
		settings = self.collectSettings()
		if self.validateSettings(settings):
			ff.FindFunctions().selectNodes(settings)

	def findDuplicates(self):
		ff.FindFunctions().findDuplicates()

	def printSave(self):
		ff.FindFunctions().printSave()

	def selectSaved(self):
		ff.FindFunctions().selectSaved()

	def selectBoundJoints(self):
		ff.FindFunctions().selectBoundJoints()

	def selectMultipleInfluence(self):
		ff.FindFunctions().selectMultipleInfluence(self.influenceAmount.value())
