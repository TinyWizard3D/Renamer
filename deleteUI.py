from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QSpinBox, QLineEdit, QComboBox, QFrame
import imp
import data
import generalFunctions as gef

#--------Tools--------#
import deleteFunctions as df

#-------Reload Tool Scripts------#
imp.reload(df)
imp.reload(gef)

class DeleteUI(QWidget):
	def __init__(self, parent=None):
		super(DeleteUI, self).__init__(parent)
		self.initUI()

	def initUI(self):
		genf = gef.GeneralFunction()

		# Layout section
		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)

		
		# Type Label
		startLabel = QLabel("from Start:")
		self.layout.addWidget(startLabel)

		# Amount of Influences
		self.delStartAmount = QSpinBox(self)
		self.delStartAmount.setRange(0, 999999)
		self.delStartAmount.setValue(0)
		self.delStartAmount.setToolTip(data.delStartTltp)
		self.layout.addWidget(self.delStartAmount)

		# Label to change
		self.delBox = QLineEdit(self)
		self.delBox.setPlaceholderText("Objects to delete")
		self.delBox.setToolTip(data.delTltp)
		self.layout.addWidget(self.delBox)

		# Type Label
		endLabel = QLabel("from End:")
		self.layout.addWidget(endLabel)

		# Amount of Influences
		self.delEndAmount = QSpinBox(self)
		self.delEndAmount.setRange(0, 999999)
		self.delEndAmount.setValue(0)
		self.delEndAmount.setToolTip(data.delEndTltp)
		self.layout.addWidget(self.delEndAmount)

		# Type Label
		typeLabel = QLabel("Type:")
		self.layout.addWidget(typeLabel)

		# Prefix dropdown
		self.typeDropdown = QComboBox(self)
		self.typeDropdown.addItems(data.typeList)
		self.typeDropdown.setToolTip(data.typeTltp)
		self.layout.addWidget(self.typeDropdown)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		#-----Additions-----#
		self.hierarchyBtn = QPushButton(self)
		genf.setButton(self.hierarchyBtn, self.layout, checkable=True, tooltip=data.hierarchyTltp, isIcon=True, iconName="hierarchyIcon")

		# Prefix dropdown
		self.hierarchyTypeDropdown = QComboBox(self)
		self.hierarchyTypeDropdown.addItems(data.typeList)
		self.hierarchyTypeDropdown.setToolTip(data.typeTltp)
		self.layout.addWidget(self.hierarchyTypeDropdown)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# exclude selected button
		self.excludeBtn = QPushButton(self)
		genf.setButton(self.excludeBtn, self.layout, checkable=True, tooltip=data.excludeTltp, isIcon=True, iconName="excludeSelectionIcon")


		# Include shapes button
		self.shapesBtn = QPushButton(self)
		genf.setButton(self.shapesBtn, self.layout, checked=True, checkable=True, tooltip=data.shapesTltp, isIcon=True, iconName="shapeIcon")


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# Button that changes label
		deleteButton = QPushButton("Delete", self)
		genf.setButton(deleteButton, self.layout, text="Delete", isMainBtn=True, iconName="deleteIcon")
		deleteButton.clicked.connect(self.deleteClicked)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# Find Duplicates button
		self.delUnconnectedBtn = QPushButton(self)
		genf.setButton(self.delUnconnectedBtn, self.layout, tooltip=data.unconnectedTltp, isIcon=True, iconName="unconnectedIcon")
		self.delUnconnectedBtn.clicked.connect(self.delUnconnected)


		#------------------
		genf.addSeparator(self.layout)
		#------------------


		# Deletes all namespaces in the scene
		self.deleteNamespacesBtn = QPushButton(self)
		genf.setButton(self.deleteNamespacesBtn, self.layout, tooltip=data.deleteNamespacesTltp, isIcon=True, iconName="renameIcon")
		self.deleteNamespacesBtn.clicked.connect(self.deleteNamespaces)

		self.setLayout(self.layout)

	def collectSettings(self):
		self.del_start = self.delStartAmount.value()
		self.del_text = self.delBox.text()
		self.del_end = self.delEndAmount.value()
		self.type_Dropdown = self.typeDropdown.currentText()
		self.hierarchy_Btn = self.hierarchyBtn.isChecked()
		self.hierarchy_type_Dropdown = self.hierarchyTypeDropdown.currentText()
		self.exclude_Btn = self.excludeBtn.isChecked()
		self.shapes_Btn = self.shapesBtn.isChecked()
		
		return {
			"delStart": self.del_start,
			"delText": self.del_text,
			"delEnd": self.del_end,
			"deleteType": self.type_Dropdown,
			"includeHierarchy": self.hierarchy_Btn,
			"hierarchyType": self.hierarchy_type_Dropdown,
			"excludeSelection": self.exclude_Btn,
			"includeShapes": self.shapes_Btn
		}

	def validateSettings(self, settings):
		#WRITE AND DECIDE ON PROPER VALIDATION FOR SETTINGS
		return True

	def deleteClicked(self):
		settings = self.collectSettings()
		if self.validateSettings(settings):
			df.DeleteFunctions().deleteNodes(settings)

	def deleteNamespaces(self):
		df.DeleteFunctions().deleteAllNamespaces()

	def delUnconnected(self):
		df.DeleteFunctions().deleteUnconnected()