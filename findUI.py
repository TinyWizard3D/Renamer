from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QLineEdit, QComboBox, QFrame
import imp
import data

#--------Tools--------#
import findFunctions as ff

#-------Reload Tool Scripts------#
imp.reload(ff)

class FindUI(QWidget):
	def __init__(self, parent=None):
		super(FindUI, self).__init__(parent)
		self.initUI()

	def initUI(self):
		# Tooltips
		duplicateTltp = "FIND DUPLICATES - Click this button to select all duplicate nodes"
		printTltp = "SAVE SELECTED - Click this button to print and save selected nodes"
		savedTltp = "SELECT SAVED LIST - Click this button to select previously saved list"
		boundJointsTltp = "SELECT BOUND JOINTS - Click this button to select all joints that bind the selected geometry"
		influenceTltp = ""
		fiveVertsTltp = "Selects all vertices in a mesh with 5 or more influences (may take a few minutes in high density meshes)"
		typeTltp = "TYPE TO SELECT - Specify which node type you would like to select"

		# Layout section
		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)

		# Label to change
		self.findBox = QLineEdit(self)
		self.findBox.setPlaceholderText("Search & Select")
		self.layout.addWidget(self.findBox)

		# Padding Label
		typeLabel = QLabel("Type:")
		self.layout.addWidget(typeLabel)

		# Prefix dropdown
		self.typeDropdown = QComboBox(self)
		self.typeDropdown.addItems(data.typeList)
		self.typeDropdown.setToolTip(typeTltp)
		self.typeDropdown.setStyleSheet("width: 100px")
		self.layout.addWidget(self.typeDropdown)

		# Button that changes label
		selectButton = QPushButton("Select", self)
		selectButton.setStyleSheet("background-color: teal; width: 70px; height: 15px; padding-bottom: 2px;")
		selectButton.clicked.connect(self.selectClicked)
		self.layout.addWidget(selectButton)


		#------------------
		self.addSeparator()
		#------------------


		# Find Duplicates button
		self.duplicateBtn = QPushButton("Select Duplicates")
		self.duplicateBtn.setToolTip(duplicateTltp)
		self.duplicateBtn.clicked.connect(self.findDuplicates)
		self.layout.addWidget(self.duplicateBtn)


		#------------------
		self.addSeparator()
		#------------------


		# Print and save button
		self.printBtn = QPushButton("Save Selected")
		self.printBtn.setToolTip(duplicateTltp)
		self.printBtn.clicked.connect(self.printSave)
		self.layout.addWidget(self.printBtn)

		# Select saved button
		self.savedBtn = QPushButton("Select Saved")
		self.savedBtn.setToolTip(savedTltp)
		self.savedBtn.clicked.connect(self.selectSaved)
		self.layout.addWidget(self.savedBtn)


		#------------------
		self.addSeparator()
		#------------------


		# Select bound joints button
		self.boundJointsBtn = QPushButton("Select Bound Joints")
		self.boundJointsBtn.setToolTip(boundJointsTltp)
		self.boundJointsBtn.clicked.connect(self.selectBoundJoints)
		self.layout.addWidget(self.boundJointsBtn)


		#------------------
		self.addSeparator()
		#------------------


		# Select 5 vert influeces button
		self.fiveVertsBtn = QPushButton("Select Influnced Vertices")
		self.fiveVertsBtn.setToolTip(fiveVertsTltp)
		self.fiveVertsBtn.clicked.connect(self.selectMultipleInfluence)
		self.layout.addWidget(self.fiveVertsBtn)

		# Joint Influence Label
		typeLabel = QLabel("Joints Influencing:")
		self.layout.addWidget(typeLabel)

		# Amount of Influences
		self.influenceAmount = QSpinBox(self)
		self.influenceAmount.setRange(0, 999999)
		self.influenceAmount.setValue(0)
		self.influenceAmount.setToolTip(influenceTltp)
		self.layout.addWidget(self.influenceAmount)

		self.setLayout(self.layout)

	def addSeparator(self):
		separator = QFrame()
		separator.setFrameShape(QFrame.VLine)
		separator.setFrameShadow(QFrame.Sunken)

		self.layout.addWidget(separator)

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
