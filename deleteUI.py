from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QLineEdit, QComboBox, QFrame
import imp
import data

#--------Tools--------#
import deleteFunctions as df

#-------Reload Tool Scripts------#
imp.reload(df)

class DeleteUI(QWidget):
	def __init__(self, parent=None):
		super(DeleteUI, self).__init__(parent)
		self.initUI()

	def initUI(self):
		# Tooltips
		delStartTltp = ""
		typeTltp = ""
		delEndTltp = ""
		delTltp = ""
		unconnectedTltp = ""
		deleteNamespacesTltp = ""

		# Layout section
		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)

		
		# Amount of Influences
		self.delStartAmount = QSpinBox(self)
		self.delStartAmount.setRange(0, 999999)
		self.delStartAmount.setValue(0)
		self.delStartAmount.setToolTip(delStartTltp)
		self.layout.addWidget(self.delStartAmount)

		# Label to change
		self.delBox = QLineEdit(self)
		self.delBox.setPlaceholderText("Objects to delete")
		self.delBox.setToolTip(delTltp)
		self.layout.addWidget(self.delBox)

		# Amount of Influences
		self.delEndAmount = QSpinBox(self)
		self.delEndAmount.setRange(0, 999999)
		self.delEndAmount.setValue(0)
		self.delEndAmount.setToolTip(delEndTltp)
		self.layout.addWidget(self.delEndAmount)

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
		deleteButton = QPushButton("Delete", self)
		deleteButton.setStyleSheet("background-color: teal; width: 70px; height: 15px;")
		deleteButton.clicked.connect(self.deleteClicked)
		self.layout.addWidget(deleteButton)


		#------------------
		self.addSeparator()
		#------------------


		# Find Duplicates button
		self.delUnconnectedBtn = QPushButton("Delete Unconnected Nodes")
		self.delUnconnectedBtn.setToolTip(unconnectedTltp)
		self.delUnconnectedBtn.clicked.connect(self.delUnconnected)
		self.layout.addWidget(self.delUnconnectedBtn)


		#------------------
		self.addSeparator()
		#------------------


		# Deletes all namespaces in the scene
		self.deleteNamespacesBtn = QPushButton("Delete Namespaces")
		self.deleteNamespacesBtn.setToolTip(deleteNamespacesTltp)
		self.deleteNamespacesBtn.clicked.connect(self.deleteNamespaces)
		self.layout.addWidget(self.deleteNamespacesBtn)

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

	def deleteClicked(self):
		settings = self.collectSettings()
		if self.validateSettings(settings):
			df.DeleteFunctions().deleteNodes(settings)

	def deleteNamespaces(self):
		rf.DeleteFunctions().deleteAllNamespaces()

	def delUnconnected(self):
		return True