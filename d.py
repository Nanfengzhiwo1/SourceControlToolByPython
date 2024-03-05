import sys
from random import randint
import git
from PySide6.QtWidgets import *


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self,pulltitle):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel(pulltitle)
        self.progressbar=QProgressBar()
        self.progressbar.move(25, 50)
        self.progressbar.resize(250, 20)
        self.progressbar.setRange(0,100)

        self.btn_start = QPushButton("begin")
        self.btn_start.move(125, 100)
        if pulltitle=="Pull Engine":
            self.btn_start.clicked.connect(self.pull_engine)
        layout.addWidget(self.label)
        layout.addWidget(self.progressbar)
        layout.addWidget(self.btn_start)
        self.setLayout(layout)


    def pull_engine(self):
        git.Repo.clone_from(url='https://github.com/Nanfengzhiwo1/EditorPluginExplore.git',to_path='D:/one',progress=Progress(self))   

    def pull_p4(self):
        pass

class Progress(git.remote.RemoteProgress):
    def __init__(self, delegate: "AnotherWindow"):
        super().__init__()
        self.delegate = delegate 

    def update(self, op_code, cur_count, max_count=None, message=''):

        progress=int(cur_count/max_count*100)
        self.delegate.progressbar.setValue(progress)  
        print(self._cur_line)

