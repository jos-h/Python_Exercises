from tkinter import *
from tkinter import ttk
import os
from os import *

class SearchApplication():
	
	__search_filenames_list = list()
	__listbox = ''
	__search_string = ''
	__primary_frame = ''
	__label_search = ''
	__entry_text_field = ''
	__search_quit_button_frame = ''

	__search_button = ''
	__quit_button = ''

	__progrss_bar_frame = ''
	__progressbar = ''
	__scrollbar = ''

	def __init__(self,root):
		super(SearchApplication, self).__init__()
		#root.minsize(550,450)
		root.maxsize(750,500)
		#self.create_search_widget(root)
		
	def create_search_widget(self, root):
		
		self.__primary_frame = ttk.Frame(root,height=200,width=200)
		self.__primary_frame.pack()
		#label
		self.__label_search = Label(self.__primary_frame)
		self.__label_search['text'] = 'Search Field'
		self.__label_search.pack(side=LEFT)
		#hi_there.grid(row=0, column=0,sticky=W)

		#text field using entry
		self.__search_string = StringVar()
		self.__entry_text_field = Entry(self.__primary_frame,textvariable=self.__search_string)
		self.__search_string.set("Search")
		self.__entry_text_field.pack(side=LEFT,padx=10,pady=10)

		#frame for search and quit button
		self.__search_quit_button_frame = ttk.Frame(root,height=300,width=100)
		self.__search_quit_button_frame.pack()

		#search button
		self.__search_button = Button(self.__search_quit_button_frame, text='Search',cursor = "hand1", 
								command=self.search_files)
		self.__search_button.pack(side=LEFT,padx=10,pady=10)
		self.__search_button.bind('<ButtonPress>',lambda e: self.__progressbar.start())

		#quit button
		self.__quit_button = Button(self.__search_quit_button_frame, text='Quit!!', fg='red',cursor = "X_cursor", command=root.destroy)
		self.__quit_button.pack(side=LEFT,padx=10,pady=10)
		self.__quit_button.bind('<ButtonPress>',lambda e: exit())

		#progress bar
		self.__progrss_bar_frame = ttk.Frame(root,height=20,width=35)
		self.__progrss_bar_frame.pack()
		self.__progressbar = ttk.Progressbar(self.__progrss_bar_frame, orient = HORIZONTAL, length = 200, mode = 'indeterminate')
		self.__progressbar.pack(padx=10,pady=10)

		#ScrollBar
		self.__scrollbar = Scrollbar(root)
		self.__scrollbar.pack(side=RIGHT,fill=Y)

		#listbox to display found result
		self.__listbox = Listbox(root,width=100,height=50)
		self.__listbox.pack(side=BOTTOM)

		'''
			configure scrollbar with listbox
		'''
		self.__listbox.config(yscrollcommand=self.__scrollbar.set)
		self.__scrollbar.config(command=self.__listbox.yview)

	def search_files(self):
		
		string_search = self.__search_string.get()
		for root_dir, dirs, filenames in os.walk("D://"):
			for files in filenames:
				if files.endswith(".py"):
					if string_search in files:
						self.__search_filenames_list.append(os.path.join(root_dir,files))
					else:
						break;
		self.__progressbar.stop()
		self.insert_Listbox(self.__listbox,self.__search_filenames_list)
	
	def getSearchList(self):
		return self.__search_filenames_list
	
	def insert_Listbox(self,listbox,search_filenames_list):
		print("in listbox function")

		for search_result in search_filenames_list:
			listbox.insert(END, search_result)


def main():
	root = Tk()
	app = SearchApplication(root)
	app.create_search_widget(root)
	root.mainloop()


if __name__ == '__main__':
	main()
