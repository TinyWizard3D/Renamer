import os
import data
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QFrame

class GeneralFunction():
	def __init__(self):		
		currentDir = os.path.dirname(os.path.abspath(__file__))
		self.iconsPath = os.path.join(currentDir, "imgs")

	def setButton(self, btn, layout, text="", checked=False, checkable=False, tooltipTitle="", tooltip="", isIcon=False, isMainBtn=False, iconName=""):
		btn.setText(text)
		btn.setCheckable(checkable)
		self.setStyledTooltip(btn, tooltipTitle, tooltip)
		if isIcon:
			self.addIcon(iconName, btn, isIcon)
			btn.setStyleSheet(data.iconStylesheet)
		if isMainBtn:
			self.addIcon(iconName, btn, isIcon)
			btn.setStyleSheet(data.mainBtnStylesheet)
		layout.addWidget(btn)
		btn.setChecked(checked)

	def addIcon(self, imgName, buttonName, isIcon):
		if not os.path.exists(self.iconsPath):
			pm.warning("Icon file does not exist:", self.iconsPath)
		else:	
			iconPath = os.path.join(self.iconsPath, imgName + ".svg")
			icon = QtGui.QIcon(iconPath)
			buttonName.setIcon(icon)
			if isIcon:
				buttonName.setIconSize(QtCore.QSize(18, 18))
			else:
				buttonName.setIconSize(QtCore.QSize(15, 15))

	def addSeparator(self, layout):
		separator = QFrame()
		separator.setFrameShape(QFrame.VLine)
		separator.setFrameShadow(QFrame.Sunken)

		layout.addWidget(separator)

	def setStyledTooltip(self, element, title, description):
		element.setToolTip(f"<b>{title}</b><br><br>{description}")