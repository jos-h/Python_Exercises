from PySide.QtCore import *
from PySide.QtGui import *
import sys
import webbrowser

class Automate(QDialog):

	def __init__(self):
		super(Automate, self).__init__()
		
		self.initUI()

	def initUI(self):

		#self.setGeometry(300, 300, 250, 250)
		'''
			Disables resizing option 
		'''
		self.setFixedSize(315,275)

		self.setWindowTitle("Open links")
		layout = QGridLayout()
		label = QLabel("Start Automate")
		start = QPushButton("Begin")
		#textedit = QTextEdit()
		# scroll = QScrollArea()
		# scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
		# scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		#layout.addWidget(textedit)
		layout.addWidget(label,0,0)
		layout.addWidget(start,0,1)
		
		# textedit.verticalScrollBar().setValue(textedit.verticalScrollBar().minimum()) 
		self.setLayout(layout)
		start.clicked.connect(self.start_appli)

	def start_appli(self):

		try:
			#url = "www.google.com"
			ffpath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(ffpath),1)
			browser = webbrowser.get('chrome')
			#browser.open_new(url)
			#browser.open_new_tab('email.zensar.com')
			url_tabs = ['www.google.com','email.zensar.com',
					'https://mail.google.com/mail/','zenloungeplus.zensar.com',
					'https://github.com/jos-h/Python_Exercises',
					'https://app.pluralsight.com/id',
					'http://www.diveintopython3.net/']
			for url_new_tabs in url_tabs:
				browser.open_new_tab(url_new_tabs)
		except Exception as e:
			print(e)

		else:
			return True


def main():
	app = QApplication(sys.argv)
	dialog = Automate()
	dialog.show()
	app.exec_()

if __name__ == '__main__':
	main()