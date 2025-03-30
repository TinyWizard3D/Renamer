import pymel.core as pm
import maya.cmds as cmds
from Renamer import data


class RenameFunctions():
	def renameObjects(self, settings):
		selectedNodes = pm.ls(sl=True)

		if len(selectedNodes) > 0:
			#----settings----#
			self.prefixText = ""
			self.renameText = ""
			self.replaceText = ""
			self.suffixText = ""
			self.paddingAmount = 0
			self.paddingStart = 0
			self.paddingStep = 0
			self.defaultState = True
			self.uppercaseState = False
			self.lowercaseState = False
			self.capitalizeState = False
			self.includeHierarchy = False
			self.hierarchyType = ""
			self.excludeSelection = False
			self.includeShapes = False

			self.populateSettings(settings)

			#----initialize variables----#
			self.paddingCount = 0

			# Rename selection
			toRename_ls = []

			if self.excludeSelection == False:
				toRename_ls = selectedNodes

			# Rename the hierarchy
			if self.includeHierarchy:
				for node in selectedNodes:
					if self.hierarchyType == data.typeList[0]:
						node_hierarchy_ls = pm.listRelatives(node, ad=True)
					else:
						node_hierarchy_ls = pm.listRelatives(node, ad=True, type=self.hierarchyType)

					for node in node_hierarchy_ls:
						if node not in toRename_ls:
							toRename_ls.append(node)
	
			self.assembleName(toRename_ls, settings)
		else:
			pm.error("No Nodes Selected.")


	def assembleName(self, nodeList, settings):
		try:
			pm.undoInfo(openChunk=True)

			for node in nodeList:
				nodeName = node.name()

				# Decide if to rename or replace part of name
				renamedNode = self.renameOrReplace(nodeName)

				# Text Decor
				decorName = self.handleDecor(renamedNode, settings)

				# Assemble name
				assembledStrName = f"{self.prefixText}{decorName}"
				
				# Add padding
				numberedName = self.handlePadding()

				# Add Prefix
				assembledName = f"{assembledStrName}{numberedName}{self.suffixText}"

				# Add "Shape" as suffix if node is of type Shape
				if node.nodeType() in data.shapeTypes:
					assembledName += "Shape"

				node.rename(assembledName, ignoreShape=not self.includeShapes)

		finally:
			pm.undoInfo(closeChunk=True)


	def populateSettings(self, settings):
		self.prefixText = settings.get('prefixText', self.prefixText)
		self.renameText = settings.get('renameText', self.renameText)
		self.replaceText = settings.get('replaceText', self.replaceText)
		self.suffixText = settings.get('suffixText', self.suffixText)
		self.paddingAmount = settings.get('paddingAmount', self.paddingAmount)
		self.paddingStart = settings.get('paddingStart', self.paddingStart)
		self.paddingStep = settings.get('paddingStep', self.paddingStep)
		self.defaultState = settings.get('defaultState', self.defaultState)
		self.uppercaseState = settings.get('uppercaseState', self.uppercaseState)
		self.lowercaseState = settings.get('lowercaseState', self.lowercaseState)
		self.capitalizeState = settings.get('capitalizeState', self.capitalizeState)
		self.includeHierarchy = settings.get('includeHierarchy', self.includeHierarchy)
		self.hierarchyType = settings.get('hierarchyType', self.hierarchyType)
		self.excludeSelection = settings.get('excludeSelection', self.excludeSelection)
		self.includeShapes = settings.get('includeShapes', self.includeShapes)


	def renameOrReplace(self, objName):
		nameTxt = self.renameText
		repTxt = self.replaceText

		if (len(repTxt) <= 0 or repTxt == None) and len(nameTxt) > 0:
			newName = self.rename(nameTxt)
			return newName
		elif len(repTxt) > 0 and len(nameTxt) > 0:
			if nameTxt in objName:
				newName = self.replace(objName, nameTxt, repTxt)
				return newName
		elif len(repTxt) > 0 and len(nameTxt) <= 0:
			newName = self.rename(repTxt)
			return newName
		elif len(repTxt) <= 0 and len(nameTxt) <= 0:
			return objName
		
		return objName


	def rename(self, newName):
		return newName


	def replace(self, objName, nameTxt, repTxt):		
		newName = objName.replace(nameTxt, repTxt)
		return newName


	def handlePadding(self):
		numberedName = ""

		numPadding = f"{{:0{self.paddingAmount}d}}"

		if self.paddingAmount > 0:
			number = self.paddingStart + self.paddingCount * self.paddingStep
			numberedName = "_" + numPadding.format(number)
			self.paddingCount += 1

		return numberedName


	def handleDecor(self, objName, settings):
		decorators = {
			"defaultState": lambda x: x,
			"uppercaseState": str.upper,
			"lowercaseState": str.lower,
			"capitalizeState": str.capitalize
		}
		
		for state, func in decorators.items():
			if settings.get(state):
				return func(str(objName))

		return objName


	def autoSuffix(self):
		selectedNodes = pm.ls(sl=True)

		if selectedNodes:
			try:
				pm.undoInfo(openChunk=True)
				
				for node in selectedNodes:
					nodeName = node.name()
					curveChildren = pm.listRelatives(node, children=True, type="nurbsCurve")
					locatorChildren = pm.listRelatives(node, children=True, type="locator")
					if node.nodeType() == "joint":
						pm.rename(node, nodeName + "_jnt")
					elif curveChildren:
						pm.rename(node, nodeName + "_ctl")
					elif locatorChildren:
						pm.rename(node, nodeName + "_loc")
					elif node.nodeType() == "transform":
						pm.rename(node, nodeName + "_geo")
			finally:
				pm.undoInfo(closeChunk=True)
		else:
			pm.warning("No nodes selected.")
