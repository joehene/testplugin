# This is the package initialization file
def classFactory(iface):
    from testPlugin import TestPlugin
    return TestPlugin(iface)
        