from PySide2.QtWidgets import QApplication, QInputDialog, QListWidget, QVBoxLayout, QDialog, QPushButton
import os
import pymel.core as pm
import maya.cmds as cmds
import maya.mel as mel
from Renamer import data

class DeleteFunctions():
	def deleteNodes(self, settings):
		selectedNodes = pm.ls(sl=True)

		if len(selectedNodes) > 0:
			#----settings----#
			self.delStartAmount = 0
			self.delText = ""
			self.delEndAmount = 0
			self.delType = ""
			self.includeHierarchy = False
			self.hierarchyType = ""
			self.excludeSelection = False
			self.includeShapes = False

			self.populateSettings(settings)

			toDeletels = []

			if self.excludeSelection == False:
				toDeletels = selectedNodes

			# Rename the hierarchy
			if self.includeHierarchy:
				for node in selectedNodes:
					if self.hierarchyType == data.typeList[0]:
						node_hierarchy_ls = pm.listRelatives(node, ad=True)
					else:
						node_hierarchy_ls = pm.listRelatives(node, ad=True, type=self.hierarchyType)

					for node in node_hierarchy_ls:
						if node not in toDeletels:
							toDeletels.append(node)
			
			self.deleteName(toDeletels)
		else:
			pm.error("No Nodes Selected.")

	def populateSettings(self, settings):
		self.delStartAmount = settings.get('delStart', self.delStartAmount)
		self.delText = settings.get('delText', self.delText)
		self.delEndAmount = settings.get('delEnd', self.delEndAmount)
		self.delType = settings.get('deleteType', self.delType)
		self.includeHierarchy = settings.get('includeHierarchy', self.includeHierarchy)
		self.hierarchyType = settings.get('hierarchyType', self.hierarchyType)
		self.excludeSelection = settings.get('excludeSelection', self.excludeSelection)
		self.includeShapes = settings.get('includeShapes', self.includeShapes)

	def deleteName(self, nodeList):
		print("------STARTING---------")
		try:
			pm.undoInfo(openChunk=True)

			for node in nodeList:
				print("---------------------")
				nodeName = node.name()

				if "|" in nodeName:
					splitName = nodeName.split("|")
					nodeName = splitName[-1]

				textRemoved = self.removeText(nodeName)

				preRemoved = self.removePre(textRemoved)

				suffRemoved = self.removeSuff(preRemoved)

				if len(suffRemoved)>0:
					node.rename(suffRemoved, ignoreShape=not self.includeShapes)
				else:
					node.rename("null", ignoreShape=not self.includeShapes)
				
		finally:
			pm.undoInfo(closeChunk=True)

	def removeText(self, nodeName):
		newName = nodeName.replace(self.delText, '')
		print("removeText: " + newName)
		return newName


	def removePre(self, nodeName):
		self.delStartValue = self.delStartAmount
		if self.delStartValue > len(nodeName):
			self.delStartValue = len(nodeName)

		newName = nodeName[self.delStartValue:len(nodeName)]
		print("removePre: " + newName)
		return newName

	def removeSuff(self, nodeName):
		self.delEndValue = self.delEndAmount
		if self.delEndValue > len(nodeName):
			self.delEndValue = len(nodeName)
		elif self.delEndValue == 0:
			self.delEndValue = len(nodeName)
		else:
			self.delEndValue = self.delEndValue*-1

		newName = nodeName[0:self.delEndValue]
		print("value: " + str(self.delEndValue))
		print("removeSuff: " + newName)
		return newName


	def deleteAllNamespaces(self):
		allNamespaces = cmds.namespaceInfo(lon=True, recurse=True)

		namespacesToDelete = [ns for ns in allNamespaces if ns not in (':', 'UI')]

		for ns in namespacesToDelete:
			try:
				cmds.namespace(moveNamespace=(ns, ':'), force=True)
				cmds.namespace(removeNamespace=ns)
				pm.warning("Namespace '{}' deleted.".format(ns))
			except Exception as e:
				print("Error deleting namespace '{}': {}".format(ns, e))

	def deleteUnconnected(self):
		mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes")')