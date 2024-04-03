"""
Hey there! I'm Sameer, and I'm excited to introduce you to my latest project: "Browsy.net" a Custom Browser Interface that Mimics Google Chrome's functionality.
1. Powered by PyQt5 and PyQtWebEngine
2. Navigation Controls: Includes options for back, forward, reload, and home page.
3. URL Search: Conduct searches directly using URLs.
4. User-Friendly Experience: Enjoy a familiar interface for efficient browsing.

"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar= QToolBar()
        self.addToolBar(navbar)
        # homebutton code
        home_btn=QAction('🏠',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        # backbutton code
        back_btn=QAction('👈🏻',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        # forwardbutton code
        forward_btn=QAction('👉🏻',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        # reloadbutton code
        reload_btn=QAction('🔄',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.Url_bar=QLineEdit()
        self.Url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.Url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))
    def navigate_to_url(self):
        url=self.Url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self,q):
        self.Url_bar.setText(q.toString())

app=QApplication(sys.argv)
QApplication.setApplicationName('Browsy.net')
window=MainWindow()
app.exec_()