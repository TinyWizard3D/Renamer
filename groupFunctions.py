from PySide2.QtWidgets import QApplication, QInputDialog, QListWidget, QVBoxLayout, QDialog, QPushButton
import os
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
import data

class GroupFunctions():
	def groupNodes(self, settings):
		selectedNodes = pm.ls(sl=True)

		if len(selectedNodes) > 0:
			#----settings----#
			try:
				pm.undoInfo(openChunk=True)

				self.groupName = ""

				self.populateSettings(settings)

				pm.group(selectedNodes, name=self.groupName)
			finally:
				pm.undoInfo(closeChunk=True)
		else:
			pm.error("No Nodes Selected.")

	def populateSettings(self, settings):
		self.groupName = settings.get('groupText', self.groupName)

	def createNPO(self):
		selectedNodes = pm.ls(sl=True)

		if len(selectedNodes) > 0:
			try:
				pm.undoInfo(openChunk=True)
				for node in selectedNodes:
					npo = pm.createNode('transform')
					parentNode = pm.listRelatives(node, parent=True)

					pm.parent(npo, parentNode)
					pm.delete(pm.parentConstraint(node, npo))

					pm.parent(node, npo)

					npo.rename(node + "_npo")

			finally:
				pm.undoInfo(closeChunk=True)
		else:
			pm.error("No Nodes Selected.")