import resources
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class TestPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        # self.action = QAction("Run", self.iface.mainWindow())
        # QObject.connect(self.action, SIGNAL("triggered()"),
        # self.onRun)
        # self.iface.addPluginToMenu("Test Plugin", self.action)
        icon = QIcon(":/plugins/testPlugin/icon.png")
        self.action = QAction(icon, "Run", self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("triggered()"),
        self.onRun)
        self.iface.addPluginToMenu("Test Plugin", self.action)
        self.iface.addToolbarIcon(self.action)

    def unload(self):
        self.iface.removePluginMenu("Test Plugin", self.action)
        self.iface.removeToolBarIcon(self.action)

    def onRun(self):
        QMessageBox.information(self.iface.mainWindow(), "debug",
        "Running")
