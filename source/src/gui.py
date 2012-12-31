#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import settings
from PyQt4 import QtGui, QtCore, QtWebKit

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
    
        webView = QtWebKit.QWebView()
        
        html = open(settings.HTML).read()
        webView.setHtml(html)
        webView.page().mainFrame().evaluateJavaScript('createDiv("%s")' % ("<b>charles garrocho</b> (19 minutos atras)<br> Primeira Mensagem do bot... <a href='http://www.google.com'>ReTwittar</a>",))
        webView.page().mainFrame().evaluateJavaScript('createDiv("%s")' % ("<b>arthur assuncao</b> (23 minutos atras)<br> A Garantia do Twitter Nao e Boa... <a href='http://www.google.com'>ReTwittar</a>",))
        webView.page().mainFrame().evaluateJavaScript('createDiv("%s")' % ("<b>alemao</b> (28 minutos atras)<br> Temos Muito no Que Trabalhar... <a href='http://www.google.com'>ReTwittar</a>",))
        
        self.setCentralWidget(webView)

        self.iniciarBot = QtGui.QAction(QtGui.QIcon(settings.INICIAR), 'Iniciar', self)
        self.iniciarBot.setShortcut('Ctrl+I')
        self.iniciarBot.setStatusTip('Iniciar o Bot - Ctrl+I')
        self.iniciarBot.triggered.connect(self.close)
        
        self.pararBot = QtGui.QAction(QtGui.QIcon(settings.PARAR), 'Parar', self)
        self.pararBot.setShortcut('Ctrl+P')
        self.pararBot.setStatusTip('Parar o Bot - Ctrl+P')
        self.pararBot.triggered.connect(self.close)
        
        self.confBot = QtGui.QAction(QtGui.QIcon(settings.CONFIGURAR), 'Configurar', self)
        self.confBot.setShortcut('Ctrl+C')
        self.confBot.setStatusTip('Configurar o Bot - Ctrl+C')
        self.confBot.triggered.connect(self.close)
        
        self.atuaBot = QtGui.QAction(QtGui.QIcon(settings.ATUALIZAR), 'Atualizar', self)
        self.atuaBot.setShortcut('Ctrl+A')
        self.atuaBot.setStatusTip('Atualizar Twitter - Ctrl+A')
        self.atuaBot.triggered.connect(self.close)
        
        self.keysBot = QtGui.QAction(QtGui.QIcon(settings.CHAVES), 'Chaves', self)
        self.keysBot.setShortcut('Ctrl+K')
        self.keysBot.setStatusTip('Chaves do Bot - Ctrl+K')
        self.keysBot.triggered.connect(self.close)
        
        self.ajuda = QtGui.QAction(QtGui.QIcon(settings.AJUDA), 'Ajuda', self)
        self.ajuda.setShortcut('Ctrl+H')
        self.ajuda.setStatusTip('Ajuda do Bot - Ctrl+H')
        self.ajuda.triggered.connect(self.close)
        
        self.sair = QtGui.QAction(QtGui.QIcon(settings.SAIR), 'Sair', self)
        self.sair.setShortcut('Ctrl+Q')
        self.sair.setStatusTip('Sair da Aplicacao - Ctrl+Q')
        self.sair.triggered.connect(self.close)

        self.statusBar()
        
        toolBar = self.addToolBar('Sair')
        toolBar.setMovable(False)
        toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        toolBar.addAction(self.iniciarBot)
        toolBar.addAction(self.pararBot)
        toolBar.addAction(self.atuaBot)
        toolBar.addSeparator()
        toolBar.addAction(self.keysBot)
        toolBar.addAction(self.confBot)
        toolBar.addSeparator()
        toolBar.addAction(self.ajuda)
        toolBar.addSeparator()
        toolBar.addAction(self.sair)
        
        self.setGeometry(600, 600, 650, 550)
        self.setWindowTitle('BOTWIPY - Bot em Python Para Twitter')
        self.setWindowIcon(QtGui.QIcon(settings.LOGO))
        self.center()
        self.show()
    
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
  
             
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()