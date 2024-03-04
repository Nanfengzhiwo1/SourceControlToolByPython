
import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        #TabWidget
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        # for n, color in enumerate(["white", "white", "white", "white"]):
        tabs.addTab(Color("white"), "Menu")
        tabs.addTab(Color("blue"), "Branch")
        tabs.addTab(Color("green"), "Tag")
        tabs.addTab(Color("black"), "SubModule")
        tabs.addTab(Color("grey"), "Search")
        self.setCentralWidget(tabs)

        #ToolBar
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #Action_Refresh
        refresh_action = QAction(QIcon("./icon/Refresh.png"), "Refresh", self)
        refresh_action.setStatusTip("Refresh all (F5)")
        refresh_action.triggered.connect(self.onMyToolBarButtonClick)
        refresh_action.setCheckable(True)
        refresh_action.setShortcut(QKeySequence("F5"))        
        toolbar.addAction(refresh_action)
        toolbar.addSeparator()

        #Action_Checkout
        checkout_action = QAction(QIcon("./icon/Checkout.png"), "Checkout", self)
        checkout_action.setStatusTip("Check out (Ctrl+E)")
        checkout_action.triggered.connect(self.onMyToolBarButtonClick)
        checkout_action.setCheckable(True)
        checkout_action.setShortcut(QKeySequence("Ctrl+E"))   
        toolbar.addAction(checkout_action)
        toolbar.addSeparator()

        #Action_Add
        add_action = QAction(QIcon("./icon/Add.png"), "Add", self)
        add_action.setStatusTip("Mark for add")
        add_action.triggered.connect(self.onMyToolBarButtonClick)
        add_action.setCheckable(True)
        add_action.setShortcut(QKeySequence())   
        toolbar.addAction(add_action)
        toolbar.addSeparator()

        #Action_Delete
        delete_action = QAction(QIcon("./icon/Delete.png"), "Delete", self)
        delete_action.setStatusTip("Mark for delete")
        delete_action.triggered.connect(self.onMyToolBarButtonClick)
        delete_action.setCheckable(True)
        delete_action.setShortcut(QKeySequence())   
        toolbar.addAction(delete_action)
        toolbar.addSeparator()

        #Action_Pull
        pull_action = QAction(QIcon("./icon/Pull.png"), "Pull", self)
        pull_action.setStatusTip("Pull")
        pull_action.triggered.connect(self.onMyToolBarButtonClick)
        pull_action.setCheckable(True)
        pull_action.setShortcut(QKeySequence())   
        toolbar.addAction(pull_action)
        toolbar.addSeparator()

        #Action_Push
        push_action = QAction(QIcon("./icon/Push.png"), "Push", self)
        push_action.setStatusTip("Push")
        push_action.triggered.connect(self.onMyToolBarButtonClick)
        push_action.setCheckable(True)
        push_action.setShortcut(QKeySequence())   
        toolbar.addAction(push_action)
        toolbar.addSeparator()

        #Action_Bug
        bug_action = QAction(QIcon("./icon/Bug.png"), "DeBug", self)
        bug_action.setStatusTip("Report Bugs")
        bug_action.triggered.connect(self.onMyToolBarButtonClick)
        bug_action.setCheckable(True)
        bug_action.setShortcut(QKeySequence())   
        toolbar.addAction(bug_action)
        toolbar.addSeparator()

        self.setStatusBar(QStatusBar(self))
        
        #MenuBar
        menu = self.menuBar()

        #File
        file_menu = menu.addMenu("&File")
        file_menu.addAction(pull_action)
        file_menu.addSeparator()
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(pull_action)

        #Checkout
        Checkout_menu = menu.addMenu("&Checkout")
        Checkout_menu.addAction(pull_action)
        Checkout_menu.addSeparator()
        Checkout_submenu = Checkout_menu.addMenu("Submenu")
        Checkout_submenu.addAction(pull_action)

        #View
        view_menu = menu.addMenu("&View")
        view_menu.addAction(pull_action)
        view_menu.addSeparator()
        view_submenu = view_menu.addMenu("Submenu")
        view_submenu.addAction(pull_action)

        #Help
        help_menu = menu.addMenu("&Help")
        help_menu.addAction(pull_action)
        help_menu.addSeparator()
        help_submenu = help_menu.addMenu("Submenu")
        help_submenu.addAction(pull_action)

    def onMyToolBarButtonClick(self, s):
        print("click", s)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
