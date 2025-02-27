from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.mozilla.org"))
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    app = QApplication([])
    window = Browser()
    window.show()
    app.exec_()
