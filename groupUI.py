from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QLineEdit, QComboBox, QFrame
import imp
import data
import generalFunctions as gef

#--------Tools--------#
import groupFunctions as gf

#-------Reload Tool Scripts------#
imp.reload(gf)
imp.reload(gef)

class GroupUI(QWidget):
	def __init__(self, parent=None):
		super(GroupUI, self).__init__(parent)
		self.initUI()

	def initUI(self):
		genf = gef.GeneralFunction()

		# Layout section
		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)

		# Label to change
		self.groupNameBox = QLineEdit(self)
		self.groupNameBox.setPlaceholderText("Group name")
		self.layout.addWidget(self.groupNameBox)

		# Find Duplicates button
		self.groupBtn = QPushButton(self)
		genf.setButton(self.groupBtn, self.layout, text="Group Selected", isMainBtn=True, iconName="npoIcon")
		self.groupBtn.clicked.connect(self.groupSelected)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# Select bound joints button
		self.NPOCreateBtn = QPushButton(self)
		genf.setButton(self.NPOCreateBtn, self.layout, isIcon=True, iconName="npoIcon")
		self.NPOCreateBtn.clicked.connect(self.createNPO)

		self.setLayout(self.layout)

	def collectSettings(self):
		self.group_name_box = self.groupNameBox.text()
		
		return {
			"groupText": self.group_name_box,
		}

	def validateSettings(self, settings):
		#WRITE AND DECIDE ON PROPER VALIDATION FOR SETTINGS
		return True

	def groupSelected(self):
		settings = self.collectSettings()
		if self.validateSettings(settings):
			gf.GroupFunctions().groupNodes(settings)

	def createNPO(self):
		gf.GroupFunctions().createNPO()