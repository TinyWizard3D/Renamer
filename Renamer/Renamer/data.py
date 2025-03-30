#----Lists----#
typeList = ["all", "transform", "shape", "mesh", "joint", "locator", "nurbsCurve", "nurbsSurface", "ikHandle", "light", "camera"]
toolsList = ["Rename", "Find", "Delete", "Group"]
shapeTypes = ["mesh", "nurbsCurve", "nurbsSurface", "subdiv", "particle", "fluidShape"]

#----Tooltips----#
preTltpTitle = "Add Prefix"
preTltp = "Write, or select from a list, a prefix for selected object/s. If left empty, no prefix will be added"

renameTltpTitle = "Rename/Replace"
renameTltp = "Writing text here will rename selected object/s to your input. If there's also input text in the Replace textbox, it will instead replace input in this textbox with the input in the Replace textbox for all selected objects."

replaceTltpTitle = "Replace with"
replaceTltp = "Writing text here will replace the input in 'Rename/Replace' with the one in this textbox for all selected objects. If 'Rename/Replace' is empty, it will instead rename all selected objects to your text input."

suffTltpTitle = "Add Suffix"
suffTltp = "Write, or select from a list, a suffix for selected object/s. If left empty, no suffix will be added"

renameBtnTltpTitle= "Rename Selection"
renameBtnTltp = "Click to rename all selected objects according to your chosen preferences"

paddingTltpTitle = "Number Padding"
paddingTltp = "Choose how many zeros should be added to all selected objects, example: 1, 01, 001, etc."

startTltpTitle = "Starting Number"
startTltp = "Choose at which number the list of selects objects should start. Example: 1: start at 1: obj_01, obj_02, etc. Example-2: start at 46: obj_46, obj_47, etc..."

stepTltpTitle = "Skip By Number"
stepTltp = "Choose the amount of steps the list of selected objects should skip. Example: 1: skip set to 1: obj_1, obj_2, etc. Example-2: skip set to 3: obj_1, obj_4, etc..."

defaultTltpTitle = "Default Decoration"
defaultTltp = "Renamed text will be unchanged from the way it was originally written"

uppercaseTltpTitle = "Uppercase (AAA)"
uppercaseTltp = "Check to make the names of selected object/s 'UPPERCASE'"

lowercaseTltpTitle = "Lowercase (aaa)"
lowercaseTltp = "Check to make the names of selected object/s 'lowercase'"

capitalizeTltpTitle = "Capitalize (Aaa)"
capitalizeTltp = "Check to make the names of selected object/s 'Capitalized'"

hierarchyTltpTitle = "Include Hierarchy"
hierarchyTltp = "Check to rename all children and grandchildren under selected object/s"

typeTltpHierarchyTitle = "Type to Include"
typeTltpHierarchy = "Specify which node type you would like to rename in the hierarchy."

shapesTltpTitle = "(RECOMMENDED) Include Shapes"
shapesTltp = "Check to also rename all shape nodes under selected object/s"

excludeTltpTitle = "Exclude Selection"
excludeTltp = "Excludes current selection from being renamed"

autoSuffixTltpTitle = "Add Suffix To Selection"
autoSuffixTltp = "Automatically adds suffix to each selected object by its type"

duplicateTltpTitle = "Find Duplicates"
duplicateTltp = "Click this button to select all duplicate nodes"

printTltpTitle = "Save Selected"
printTltp = "Click this button to print and save selected nodes"

saveSelectionTltpTitle = "Save Selection"
saveSelectionTltp = "Click this button to save selection to allow for later quick selection"

savedTltpTitle = "Open Load Selection Window"
savedTltp = "Click this button to open the Load Selection window and select a previously saved selection"

boundJointsTltpTitle = "Select Bound Joints"
boundJointsTltp = "Click this button to select all joints that bind the selected geometry.<br><br><i>Requires a skinCluster on the mesh.</i>"

fiveVertsTltpTitle = "Select Vertices by Influence Count"
fiveVertsTltp = """Select all vertices in the active mesh that have X or more influences.<br>
    This may take time for high-density meshes.<br><br>
    <i>Requires a skinCluster on the mesh.</i>"""

influenceTltpTitle = "Influence Count Threshold"
influenceTltp = "Set the minimum number of influences a vertex must have to be selected using the button on the left."

typeTltpTitle = "Type to Select"
typeTltp = "Specify which node type you would like to select"

findBoxTltpTitle = "Select Objects Containing This Text"
findBoxTltp = """Write text here to select objects that have this text in their name.<br><br>
    <b>TIP:</b><br>
    • *text →  will select all objects ending with 'text'.<br>
    • text* →  will select all objects starting with 'text'.<br>
    • *text* →  will select all objects containing the word 'text'"""

selectBtnTltpTitle = "Select Objects"
selectBtnTltp = "Click this button to select all objects that correspond to your preferences on the left"

delStartTltpTitle = "Delete Characters from Start"
delStartTltp = "Enter the number of characters to remove from the beginning of selected object names."

delEndTltpTitle = "Delete Characters From End"
delEndTltp = "Enter the number of characters to remove from the end of selected object names."

delTltpTitle = "Delete Specific Text from Names"
delTltp = """Enter text to remove it from selected object names.<br><br>
    <b>Tip:</b><br>
    • *text → Removes text only if it appears at the end.<br>
    • text* → Removes text only if it appears at the start.<br>
    • *text* → Removes all occurrences of 'text' anywhere in the name."""

delBtnTltpTitle = "Delete Text In Selected"
delBtnTltp = "Click this button to delete text in selected objects according to your preferences on the left"

unconnectedTltpTitle = "Delete Unused Nodes"
unconnectedTltp = "Click this button to delete all nodes that aren't connected to other nodes."

deleteNamespacesTltpTitle = "Delete All Namespaces"
deleteNamespacesTltp = "Click this button to delete all namespaces."

hierarchyTltpTitle = "Include Hierarchy"
hierarchyTltp = "Check to rename all children and grandchildren under selected object/s"

shapesTltpTitle = "(RECOMMENDED) Include Shapes"
shapesTltp = "Check to also rename all shape nodes under selected object/s"

excludeTltpTitle = "Exclude Selection"
excludeTltp = "Excludes current selection from being renamed"

groupNameBoxTltpTitle = "Name of Group"
groupNameBoxTltp = "Enter the name of the selected objects' group."

groupBtnTltpTitle = "Group Selected Objects"
groupBtnTltp = "Click this button to group selected objects and set their name according to the text box on the left."

npoTltpTitle = "Create NPO"
npoTltp = "Neutral POse - Creates a transform group above the selected object and transfers all values to the group, zeroing out the object's values."

ascendingTltpTitle = "Ascending Order"
ascendingTltp = "Orders all selected objects in ascending order"

descendingTltpTitle = "Descending Order"
descendingTltp = "Orders all selected objects in descending order"

helpTltpTitle = "Help"
helpTltp = "Opens the help menu"


#----Stylesheets----#
mainColor = "#5285a6"
hoverColor = "#62a0c7"

mainBtnStylesheet = f"""
        QPushButton {{
            background-color: {mainColor}; 
            width: 100px; 
            height: 15px; 
            padding-bottom: 2px;
            padding-left: 5px;
            padding-right: 5px;
        }}
        QPushButton:checked {{
            background-color: {mainColor};
            color: white;
        }}
        QPushButton:pressed {{
            background-color: {mainColor};
            color: white;
        }}
    """

iconStylesheet = f"""
        QPushButton {{
            background-color: transparent;
            color: white;
            border: none; 
            width: 17px; 
            height: 17px;
            padding: 5px;
        }}
        QPushButton:hover {{
            background-color: {hoverColor};
            color: white;
        }}
        QPushButton:checked {{
            background-color: {mainColor};
            color: white;
        }}
        QPushButton:pressed {{
            background-color: {mainColor};
            color: white;
        }}
    """


tooltipStylesheet = """
    #customTooltip QToolTip {
        font-family: SegoeUI;
        background-color: #ffffdc;
        color: black;
        border: 1px solid #000;
        padding: 4px 3px;
        border-radius: 0px;
        font-size: 11px;
        min-width: 322px;
        min-height: 95px;
    }"""