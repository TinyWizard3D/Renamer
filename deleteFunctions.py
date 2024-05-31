from PySide2.QtWidgets import QApplication, QInputDialog, QListWidget, QVBoxLayout, QDialog, QPushButton
import os
import pymel.core as pm
import maya.cmds as cmds

class DeleteFunctions():
	def __init__(self):
		self.file_path = None

	def deleteNodes(self, settings):
		#----settings----#
		self.findText = ""
		self.selectType = ""

		self.populateSettings(settings)

	def populateSettings(self, settings):
		self.findText = settings.get('findText', self.findText)
		self.selectType = settings.get('selectType', self.selectType)

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