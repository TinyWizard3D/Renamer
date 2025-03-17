from PySide2.QtWidgets import QApplication, QInputDialog, QListWidget, QVBoxLayout, QDialog, QPushButton
import os
import pymel.core as pm
import maya.cmds as cmds
import data

class FindFunctions():
	def __init__(self):
		self.file_path = None

	def selectNodes(self, settings):
		#----settings----#
		self.findText = ""
		self.selectType = ""

		self.populateSettings(settings)

		try:
			matchingObjects = pm.ls(self.findText)

			if self.findText and self.selectType != data.typeList[0]:
				objTypeLs = [obj for obj in matchingObjects if pm.nodeType(obj) == self.selectType]
			else:
				pm.select(matchingObjects)

			if objTypeLs:
				pm.select(objTypeLs)
			else:
				pm.warning("Couldn't find any matching objects.")
		except Exception as e:
			pm.error("An error occurred: {}".format(e))


	def populateSettings(self, settings):
		self.findText = settings.get('findText', self.findText)
		self.selectType = settings.get('selectType', self.selectType)

	def findDuplicates(self):
		allObjs = pm.ls(dag=True)
		seenObjects = set()
		duplicateObjects = set()

		for obj in allObjs:
			objName = obj.nodeName()
			if objName in seenObjects:
				duplicateObjects.add(objName)
			else:
				seenObjects.add(objName)

		if duplicateObjects:
			duplicateLs = pm.ls(list(duplicateObjects))
			pm.select(duplicateLs)
		else:
			pm.warning("No duplicate nodes found.")

	def printSave(self):
		selected_nodes = pm.ls(sl=True)
		if not selected_nodes:
			pm.warning("No nodes selected.")
			return

		try:
			current_scene_path = cmds.file(query=True, sceneName=True)
			if not current_scene_path:
				raise RuntimeError("Please save your scene.")
			self.file_path = os.path.join(os.path.dirname(current_scene_path), 'selections.txt')

			if not os.path.exists(self.file_path):
				with open(self.file_path, 'w') as file:
					file.write("")

		except Exception as e:
			pm.warning("Please save your scene.")
			self.file_path = None
			return

		group_name, ok = QInputDialog.getText(None, "Save Selection", "Enter group name:")
		if ok and group_name:
			# Read existing selections
			groups = self.get_saved_groups()
			group_lines = {}
			current_group = None

			with open(self.file_path, 'r') as file:
				lines = file.readlines()
				for line in lines:
					if line.startswith("Group:"):
						current_group = line.split(":")[1].strip()
						group_lines[current_group] = []
					if current_group is not None:
						group_lines[current_group].append(line)
					if line.startswith("EndGroup"):
						current_group = None

			# Overwrite or add the new group
			group_lines[group_name] = ["Group: {}\n".format(group_name)] + [node.name() + '\n' for node in selected_nodes] + ["EndGroup\n"]

			# Write back all groups
			with open(self.file_path, 'w') as file:
				for group in group_lines.values():
					file.writelines(group)

			pm.warning("Selection group '{}' saved to {}".format(group_name, self.file_path))

			selectedObjs = "[" + ", ".join('"' + str(obj) + '"' for obj in selected_nodes) + "]"

			print(selectedObjs)

	def selectSaved(self):
		try:
			current_scene_path = cmds.file(query=True, sceneName=True)
			if not current_scene_path:
				raise RuntimeError("Please save your scene.")
			self.file_path = os.path.join(os.path.dirname(current_scene_path), 'selections.txt')

		except Exception as e:
			pm.error("Please save your scene.")
			self.file_path = None

		if not os.path.exists(self.file_path):
			pm.warning("No saved selections found.")
			return

		groups = self.get_saved_groups()
		if not groups:
			pm.warning("No selection groups found.")
			return

		dialog = QDialog()
		dialog.setWindowTitle("Load Selection")
		layout = QVBoxLayout()
		list_widget = QListWidget()
		for group in groups:
			list_widget.addItem(group)

		load_button = QPushButton("Load")
		load_button.clicked.connect(lambda: self.select_group(list_widget.currentItem().text(), dialog))
		layout.addWidget(list_widget)
		layout.addWidget(load_button)
		dialog.setLayout(layout)
		dialog.exec_()

	def get_saved_groups(self):
		group_lines = {}
		current_group = None

		if os.path.exists(self.file_path):
			with open(self.file_path, 'r') as file:
				lines = file.readlines()
				for line in lines:
					if line.startswith("Group:"):
						current_group = line.split(":")[1].strip()
						group_lines[current_group] = []
					if current_group is not None:
						group_lines[current_group].append(line)
					if line.startswith("EndGroup"):
						current_group = None
		return group_lines

	def select_group(self, group_name, dialog):
		try:
			with open(self.file_path, 'r') as file:
				lines = file.readlines()
			in_group = False
			nodes_to_select = []
			for line in lines:
				if line.startswith("Group: {}".format(group_name)):
					in_group = True
					continue
				if line.startswith("EndGroup"):
					in_group = False
				if in_group and not line.startswith("Group:"):
					nodes_to_select.append(line.strip())
			pm.select(nodes_to_select)
			print("Selection group '{}' loaded.".format(group_name))
			dialog.accept()
		except Exception as e:
			pm.warning("An error occurred: {}".format(e))


	def selectBoundJoints(self):
		selected = cmds.ls(sl=True)

		if selected:
			history = cmds.listHistory(selected[0])
			skinClusters = cmds.ls(history, type='skinCluster')

			if skinClusters:
				joints = cmds.skinCluster(skinClusters[0], query=True, influence=True)
				cmds.select(joints, replace=True)
			else:
				pm.warning("No skinClusters on object.")
		else:
			pm.warning("No nodes selected.")


	def selectMultipleInfluence(self, max_influences):
		selected_objects = cmds.ls(sl=True)

		if not selected_objects:
			pm.warning("No nodes selected.")
			return

		obj = selected_objects[0]
		res = []

		if obj:
			history = cmds.listHistory(obj)
			skin_clusters = cmds.ls(history, type="skinCluster")
			for skin in skin_clusters:
				for mesh in cmds.skinCluster(skin, q=True, geometry=True):
					res += self.checkMesh(max_influences, skin, mesh)

			if res:
				cmds.select(clear=True)
				cmds.select(res)
			else:
				pm.warning("No vertices found with influences greater than {}".format(max_influences))
		else:
			pm.warning("No valid object selected.")

	def checkMesh(self, max_influences, skin, mesh):
		vertices = cmds.polyListComponentConversion(mesh, toVertex=True)
		vertices = cmds.filterExpand(vertices, selectionMask=31)  # polygon vertex

		res = []
		for vert in vertices:
			joints = cmds.skinPercent(
				skin, vert, query=True, ignoreBelow=0.000001, transform=None)

			print("max influences: " + str(max_influences))
			print("Vertex: {}, Influences: {}".format(vert, len(joints)))

			if max_influences == 0 and len(joints) == 0:
				res.append(vert)
			elif len(joints) == max_influences:
				res.append(vert)

		return res