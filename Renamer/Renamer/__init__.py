import pymel.core as pm

print("---------------------------------hihi---------------------------")

def createRenamerMenu():
    menuVar = 'RenamerMenu'
    menuName = 'Renamer Toolkit'

    if pm.menu(menuVar, q=True, exists=True):
        try:
            pm.deleteUI(menuVar, control=True)
        except Exception as e:
            pm.warning("Failed to delete menu '{}': {}".format(menuVar, e))

    mainWindow = pm.language.melGlobals['gMainWindow']

    pm.menu(menuVar, label=menuName, parent=mainWindow, tearOff=True)

    pm.menuItem(label='Open Renamer', command=lambda *args: __import__('Renamer.renamer_01', fromlist=['']).show_renamer())

    print("---------------------------------Done with hihi---------------------------")

createRenamerMenu()