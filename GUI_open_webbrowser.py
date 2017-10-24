<<<<<<< HEAD
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
			ffpath = r'/usr/bin/google-chrome'
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(ffpath),1)
			browser = webbrowser.get('chrome')
			#browser.open_new(url)
			#browser.open_new_tab('email.zensar.com')
			url_tabs = ['www.google.com',
					'https://mail.google.com/mail/','www.youtube.com',
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
=======
from PySide.QtCore import *
from PySide.QtGui import *
import sys
import webbrowser
import requests
#from robobrowser import RoboBrowser


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
		time = QTimer()
		time.singleShot(10000, self.close)

	def start_appli(self):

		try:
			ffpath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
			webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(ffpath),1)
			browser = webbrowser.get('chrome')
			url_tabs = ['www.google.com','email.zensar.com',
					'https://mail.google.com/mail/','zenloungeplus.zensar.com',
					'https://github.com/jos-h/Python_Exercises',
					'https://app.pluralsight.com/id',
					'http://www.diveintopython3.net/']
			for url_new_tabs in url_tabs:
				browser.open_new_tab(url_new_tabs)

			#self.login(url)
		except Exception as e:
			print("====",e)

		else:
			return True

	# def login(self, url):

	# 	values = {"inusername":"<UserName>",
	# 			"inpassword":"<password>"}
	# 	session_request = requests.Session()

	# 	#r = session_request.get(url)

	# 	result = session_request.post(url, data = values)

	# 	print(result)

def main():
	app = QApplication(sys.argv)
	dialog = Automate()
	dialog.show()
	app.exec_()

if __name__ == '__main__':
	main()
>>>>>>> 56ec4a980455644465e575f966e444f30ea77e0d
