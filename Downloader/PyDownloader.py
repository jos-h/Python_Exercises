from PySide.QtGui import *
from PySide.QtCore import *

import sys
import urllib.request
import time
import requests

class PyDownloader(QWidget):

	def __init__(self):

		super(PyDownloader,self).__init__()

		self.initUI()

	def initUI(self):

		self.setFixedSize(350,200)

		layout = QVBoxLayout()

		self.url_edit = QLineEdit()
		self.url_edit.setPlaceholderText("URL")

		self.file_save_location = QLineEdit()
		self.file_save_location.setPlaceholderText("file location")
		
		self.progress_bar = QProgressBar()
		self.progress_bar.setValue(0)
		self.progress_bar.setAlignment(Qt.AlignHCenter)

		download_btn = QPushButton("Download")
		browse_btn = QPushButton("Browse")

		layout.addWidget(self.url_edit)

		layout.addWidget(self.file_save_location)
		layout.addWidget(browse_btn)

		layout.addWidget(self.progress_bar)

		layout.addWidget(download_btn)

		self.setLayout(layout)
		self.setFocus()
		self.setWindowTitle("PyDownloader GUI")

		browse_btn.clicked.connect(self.browse_files)
		download_btn.clicked.connect(self.download)
	
	def browse_files(self):

		save_file = QFileDialog.getSaveFileName(self, caption="Save As...", filter="all files (*.*)",directory=".")
		self.file_save_location.setText(QDir.toNativeSeparators(save_file[0]))

	def download(self):
		url = self.url_edit.text()
		save_loca = self.file_save_location.text()
		print(save_loca)
		try:
			start = time.time()
			urllib.request.urlretrieve(url, save_loca, self.report)
			# response = requests.get(url, stream=True)
			# handle = open(save_loca, "wb")
			# for chunks in response.iter_content(chunk_size = 512):
			# 	if chunks:
			# 		handle.write(chunks)
			end = time.time()
		except Exception as e:
			print(e)
			QMessageBox.warning(self, "information", "failed!!!!!")
			return
		QMessageBox.information(self, "Information", "Download is complete")
		QMessageBox.information(self,"time required",str(int(abs(start - end))))
		self.progress_bar.setValue(0)
		self.url_edit.setText("")
		self.file_save_location.setText("")
	
	def report(self, blocknum, blocksize, totalsize):

		read_so_far = blocknum * blocksize

		if totalsize > 0:
			percent = (read_so_far * 100)/ totalsize
			self.progress_bar.setValue(int(percent))

def main():

	app = QApplication(sys.argv)

	downloader = PyDownloader()
	downloader.show()

	app.exec_()

if __name__ == '__main__':
	main()