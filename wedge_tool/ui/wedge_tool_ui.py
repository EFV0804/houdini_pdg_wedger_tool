from Qt import QtWidgets, QtCompat, QtCore
import wedge_tool
class OpenFileWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(OpenFileWindow, self).__init__()
        self.wedger = wedge_tool.Wedger()
        self.data = wedger.user_settings