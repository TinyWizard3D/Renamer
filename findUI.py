from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox

class FindUI(QWidget):
	def __init__(self, parent=None):
		super(FindUI, self).__init__(parent)
		self.initUI()

		self.setFixedSize(self.sizeHint())

	def initUI(self):
		# Layout section
		self.layout = QHBoxLayout(self)
		self.layout.setContentsMargins(0, 0, 0, 0)

		# Label to change
		self.findBox = QLineEdit(self)
		self.findBox.setPlaceholderText("Search & Select")
		self.layout.addWidget(self.findBox)

		# Button that changes label
		btn = QPushButton("Select", self)
		self.layout.addWidget(btn)

		self.setLayout(self.layout)