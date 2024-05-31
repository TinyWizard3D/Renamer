from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QLineEdit, QComboBox

class GroupUI(QWidget):
	def __init__(self, parent=None):
		super(GroupUI, self).__init__(parent)
		self.initUI()

	def initUI(self):
		typeList = ["transform", "shape", "mesh", "joint", "locator", "nurbsCurve", "nurbsSurface", "ikHandle", "light", "camera"]

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
		self.findBox.setPlaceholderText("group")
		self.layout.addWidget(self.findBox)

		# Padding Label
		typeLabel = QLabel("Type:")
		self.layout.addWidget(typeLabel)

		# Prefix dropdown
		self.typeDropdown = QComboBox(self)
		self.typeDropdown.setEditable(True)
		self.typeDropdown.addItems(typeList)
		self.typeDropdown.setCurrentText("")
		self.typeDropdown.lineEdit().setPlaceholderText("Select node type")
		self.typeDropdown.setToolTip(typeTltp)
		self.typeDropdown.setStyleSheet("width: 100px")
		self.layout.addWidget(self.typeDropdown)

		# Button that changes label
		btn = QPushButton("Select", self)
		self.layout.addWidget(btn)

		# Find Duplicates button
		self.duplicateBtn = QPushButton("Find Duplicates")
		self.duplicateBtn.setCheckable(True)
		self.duplicateBtn.setToolTip(duplicateTltp)
		self.layout.addWidget(self.duplicateBtn)

		# Print and save button
		self.printBtn = QPushButton("Save Selected")
		self.printBtn.setCheckable(True)
		self.printBtn.setToolTip(duplicateTltp)
		self.layout.addWidget(self.printBtn)

		# Select saved button
		self.savedBtn = QPushButton("Select Saved")
		self.savedBtn.setCheckable(True)
		self.savedBtn.setToolTip(savedTltp)
		self.layout.addWidget(self.savedBtn)

		# Select bound joints button
		self.boundJointsBtn = QPushButton("Select Bound Joints")
		self.boundJointsBtn.setCheckable(True)
		self.boundJointsBtn.setToolTip(boundJointsTltp)
		self.layout.addWidget(self.boundJointsBtn)

		# Select 5 vert influeces button
		self.fiveVertsBtn = QPushButton("Select Influnced Vertices")
		self.fiveVertsBtn.setCheckable(True)
		self.fiveVertsBtn.setToolTip(fiveVertsTltp)
		self.layout.addWidget(self.fiveVertsBtn)

		# Amount of Padding
		self.influenceAmount = QSpinBox(self)
		self.influenceAmount.setRange(0, 999999)
		self.influenceAmount.setValue(0)
		self.influenceAmount.setToolTip(influenceTltp)
		self.layout.addWidget(self.influenceAmount)

		self.setLayout(self.layout)