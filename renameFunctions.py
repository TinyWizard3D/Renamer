import maya.cmds as cmds
import pymel.core as pm

class RenameFunctions():
	def renameObjects(self, settings):
		print("##################################")
		print("---------Starting Renamer---------")
		print("##################################")

		selectedNodes = pm.ls(sl=True)
		self.shapeTypes = ["mesh", "nurbsCurve", "nurbsSurface", "subdiv", "particle", "fluidShape"]

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
					node_hierarchy_ls = pm.listRelatives(node, ad=True, type=self.hierarchyType)

					for node in node_hierarchy_ls:
						if node not in toRename_ls:
							toRename_ls.append(node)
	
			self.assembleName(toRename_ls, settings)
		else:
			pm.error("No Objects Selected.")


	def assembleName(self, nodeList, settings):
		try:
			pm.undoInfo(openChunk=True)

			for node in nodeList:
				print("--------------------")
				nodeName = node.name()
				print("Old Name: " + nodeName)

				# Decide if to rename or replace part of name
				renamedNode = self.renameOrReplace(nodeName)

				# Text Decor
				decorName = self.handleDecor(renamedNode, settings)

				# Assemble name
				assembledStrName = "{}{}".format(self.prefixText, decorName)
				
				# Add padding
				numberedName = self.handlePadding()

				# Add Prefix
				assembledName = "{}{}{}".format(assembledStrName, numberedName, self.suffixText)

				# Add "Shape" as suffix if node is of type Shape
				if node.nodeType() in self.shapeTypes:
					assembledName += "Shape"

				node.rename(assembledName, ignoreShape=not self.includeShapes)
				print("New Name: " + assembledName)
				print("--------------------")

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
			print("calling rename from rename")
			newName = self.rename(nameTxt)
			return newName
		elif len(repTxt) > 0 and len(nameTxt) > 0:
			if nameTxt in objName:
				print("calling replace")
				newName = self.replace(objName, nameTxt, repTxt)
				return newName
			else:
				pm.error("'" + nameTxt + "' is not part of selected objects name: '" + objName + "'")
		elif len(repTxt) > 0 and len(nameTxt) <= 0:
			print("calling rename from replace")
			newName = self.rename(repTxt)
			return newName
		elif len(repTxt) <= 0 and len(nameTxt) <= 0:
			print("passing")
			return objName
		else:
			pm.warning("Can't rename objects.")


	def rename(self, newName):
		print("rename: " + newName)
		return newName


	def replace(self, objName, nameTxt, repTxt):		
		print("replace: " + nameTxt + ", with: " + repTxt + ", in: " + objName)
		newName = objName.replace(nameTxt, repTxt)
		return newName


	def handlePadding(self):
		numberedName = ""

		numPadding = "{{:0{}d}}".format(self.paddingAmount)

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


	# Sorting lists
	def sortList(self):
		try:
			pm.undoInfo(openChunk=True)
			
			print("Sorting list")
			selectedNodes = pm.ls(sl=True)

			# Capture the original parent and positions within their parent groups
			original_positions = {node: (node.getParent(), node.index()) for node in selectedNodes}

			# Sort the nodes by name
			sortedNodes = sorted(selectedNodes, key=lambda x: x.name())

			# Reorder within their parent groups based on original positions
			for parent, positions in original_positions.items():
				parent, original_index = positions
				siblings = pm.listRelatives(parent, children=True)
				# Find the new indices for the sorted nodes
				new_indices = {node: siblings.index(node) for node in sortedNodes if node.getParent() == parent}

				for node in sortedNodes:
					if node.getParent() == parent:
						# Reorder node within its parent group
						pm.reorder(node, new_indices[node])

		finally:
			pm.undoInfo(closeChunk=True)

	def reverseSortList(self):
		try:
			pm.undoInfo(openChunk=True)

			print("reversing list")
			selectedNodes = pm.ls(sl=True)

			originalPositions = {node: node.getParent() for node in selectedNodes}

			sortedNodes = sorted(selectedNodes, key=lambda x: x.name())
			sortedNodes.reverse()

			for parent in set(originalPositions.values()):
				children = [node for node in sortedNodes if originalPositions[node] == parent]
				for node in children:
					pm.reorder(node, front=True)


		finally:
			pm.undoInfo(closeChunk=True)

