import maya.cmds as cmds
import pymel.core as pm

class RenameFunctions():
	def renameObjects(self, settings):
		selectedObjects = pm.ls(sl=True)

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
		self.includeShapes = False

		self.populateSettings(settings)

		self.paddingCount = 0

		if len(selectedObjects) > 0:
			for obj in selectedObjects:
				print("--------------------")
				objName = obj.name()
				hierarchyList = []
				print("Old Name: " + objName)

				if self.includeHierarchy:
				    children_ls = pm.listRelatives(obj, ad=True, type=self.hierarchyType)
				    for obj in new_ls:
				        if obj not in hierarchy_ls:
				            hierarchy_ls.append(obj)

				# Decide if to rename or replace part of name
				renamedObj = self.renameOrReplace(objName)

				# Text Decor
				decorName = self.handleDecor(renamedObj, settings)

				# Assemble name
				assembledStrName = "{}{}".format(self.prefixText, decorName)
				
				# Add padding
				numberedName = self.handlePadding()

				# Add Prefix
				assembledName = "{}{}{}".format(assembledStrName, numberedName, self.suffixText)

				print("New Name: " + assembledName)
				print("--------------------")
		else:
			pm.warning("No Objects Selected.")


	def assembleName(self, list):
		hierarchy_ls = []

		for obj in sel_ls:
		    new_ls = pm.listRelatives(obj, ad=True, type=self.hierarchyType)
		    for obj in new_ls:
		        if obj not in hierarchy_ls:
		            hierarchy_ls.append(obj)


	def populateSettings(self, settings):
		self.prefixText = settings["prefixText"]
		self.renameText = settings["renameText"]
		self.replaceText = settings["replaceText"]
		self.suffixText = settings["suffixText"]
		self.paddingAmount = settings["paddingAmount"]
		self.paddingStart = settings["paddingStart"]
		self.paddingStep = settings["paddingStep"]
		self.defaultState = settings["defaultState"]
		self.uppercaseState = settings["uppercaseState"]
		self.lowercaseState = settings["lowercaseState"]
		self.capitalizeState = settings["capitalizeState"]
		self.includeHierarchy = settings["includeHierarchy"]
		self.hierarchyType = settings["hierarchyType"]
		self.includeShapes = settings["includeShapes"]


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