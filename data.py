import generalFunctions as gf

typeList = ["all", "transform", "shape", "mesh", "joint", "locator", "nurbsCurve", "nurbsSurface", "ikHandle", "light", "camera"]
toolsList = ["Rename", "Find", "Delete", "Group"]
shapeTypes = ["mesh", "nurbsCurve", "nurbsSurface", "subdiv", "particle", "fluidShape"]

# Tooltips
preTltpTitle = "Prefix"
preTltp = "Write, or select from a list, a prefix for selected object/s. If left empty, no prefix will be added"

renameTltpTitle = "Rename/Replace"
renameTltp = "Writing text here will rename selected object/s to your input. If there's also input text in the Replace textbox, it will instead replace input in this textbox with the input in the Replace textbox for all selected objects."

replaceTltpTitle = "Replace with"
replaceTltp = "Writing text here will replace the input in 'Rename/Replace' with the one in this textbox for all selected objects. If 'Rename/Replace' is empty, it will instead rename all selected objects to your text input."

suffTltpTitle = "Suffix"
suffTltp = "Write, or select from a list, a suffix for selected object/s. If left empty, no suffix will be added"

renameBtnTltp = "Click to rename all selected objects according to your chosen preferences"

paddingTltpTitle = ""
paddingTltp = "Choose how many zeros should be added to the all selected objects, example: 1, 01, 001, etc."

startTltpTitle = ""
startTltp = "Choose at which number the list of selects objects should start. Example-1: start at 1: obj_01, obj_02, etc. Example-2: start at 46: obj_46, obj_47, etc..."

stepTltpTitle = ""
stepTltp = "Choose the amount of steps the list of selected objects should skip. Example-1: skip set to 1: obj_1, obj_2, etc. Example-2: skip set to 3: obj_1, obj_4, etc..."

defaultTltpTitle = "Default Decoration"
defaultTltp = "Renamed text will be unchanged from the way it was originally written"

uppercaseTltpTitle = "Uppercase (AAA)"
uppercaseTltp = "Check to make all copy of selected object/s 'UPPERCASE'"

lowercaseTltpTitle = "lowercase (aaa)"
lowercaseTltp = "Check to make all copy of selected object/s 'lowercase'"

capitalizeTltpTitle = "Capitalize (Aaa)"
capitalizeTltp = "Check to make all copy of selected object/s 'Capitalize'"

hierarchyTltpTitle = "Include Hierarchy"
hierarchyTltp = "Check to rename all children and grandchildren under selected object/s"

typeTltpTitle = "Type to Include"
typeTltp = "Specify which node type you would like to rename in the hierarchy."

shapesTltpTitle = "(RECOMMENDED) Include Shapes"
shapesTltp = "Check to also rename all shape nodes under selected object/s"

excludeTltpTitle = "Exclude Selection"
excludeTltp = "Excludes current selection from being renamed"

autoSuffixTltpTitle = ""
autoSuffixTltp = ""

duplicateTltpTitle = "Find Duplicates"
duplicateTltp = "Click this button to select all duplicate nodes"

printTltpTitle = "Save Selected"
printTltp = "Click this button to print and save selected nodes"

savedTltpTitle = "Select Saved List"
savedTltp = "Click this button to select previously saved list"

boundJointsTltpTitle = "Select Bound Joints"
boundJointsTltp = "Click this button to select all joints that bind the selected geometry"

influenceTltpTitle = ""
influenceTltp = ""

fiveVertsTltpTitle = ""
fiveVertsTltp = "Selects all vertices in a mesh with 5 or more influences (may take a few minutes in high density meshes)"

typeTltpTitle = "Type to Select"
typeTltp = "Specify which node type you would like to select"

delStartTltpTitle = ""
delStartTltp = ""

typeTltpTitle = ""
typeTltp = ""

delEndTltpTitle = ""
delEndTltp = ""

delTltpTitle = ""
delTltp = ""

unconnectedTltpTitle = ""
unconnectedTltp = ""

deleteNamespacesTltpTitle = ""
deleteNamespacesTltp = ""

hierarchyTltpTitle = "Include Hierarchy"
hierarchyTltp = "Check to rename all children and grandchildren under selected object/s"

shapesTltpTitle = "(RECOMMENDED) Include Shapes"
shapesTltp = "Check to also rename all shape nodes under selected object/s"

excludeTltpTitle = "Exclude Selection"
excludeTltp = "Excludes current selection from being renamed"

#mainColor = teal
#hoverColor = #009a9a

mainColor = "#5285a6"
hoverColor = "#62a0c7"

#----Stylesheets----#
mainBtnStylesheet = """
        QPushButton {{
            background-color: {}; 
            width: 80px; 
            height: 15px; 
            padding-bottom: 2px;
            padding-left: 5px;
            padding-right: 5px;
        }}
        QPushButton:checked {{
            background-color: {};
            color: white;
        }}
        QPushButton:pressed {{
            background-color: {};
            color: white;
        }}
    """.format(mainColor, mainColor, mainColor)

iconStylesheet = """
        QPushButton {{
            background-color: transparent;
            color: white;
            border: none; 
            width: 17px; 
            height: 17px;
            padding: 5px;
        }}
        QPushButton:hover {{
            background-color: {};
            color: white;
        }}
        QPushButton:checked {{
            background-color: {};
            color: white;
        }}
        QPushButton:pressed {{
            background-color: {};
            color: white;
        }}
    """.format(hoverColor, mainColor, mainColor)