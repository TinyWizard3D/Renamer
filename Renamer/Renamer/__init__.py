import pymel.core as pm

def createRenamerMenu():
    menuVar = 'RenamerMenu'
    menuName = 'Renamer Toolkit'

    if pm.menu(menuVar, q=True, exists=True):
        try:
            pm.deleteUI(menuVar, control=True)
        except Exception as e:
            pm.warning(f"Failed to delete menu '{menuVar}': {e}")

    mainWindow = pm.language.melGlobals['gMainWindow']

    pm.menu(menuVar, label=menuName, parent=mainWindow, tearOff=True)

    pm.menuItem(label='Open Renamer', command=lambda *args: __import__('Renamer.renamer_01', fromlist=['']).show_renamer())

    print("Imported Renamer Toolkit successfully")

createRenamerMenu()