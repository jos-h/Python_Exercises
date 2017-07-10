import csv
import xlsxwriter
from xlsxwriter.workbook import Workbook
import os

def csv_excel(csv_file):

	dest_excel_file_path = "D://macrocodesrequired//"

	'''
		create workbook using 
		Workboot method from xlsx.workbook
	'''
	workbook = xlsxwriter.Workbook(dest_excel_file_path + "sample_excel.xlsx",
									{'strings_to_numbers':True})

	'''
		create a worksheet
		by default the name of sheet
		is Sheet 1 . we can pass arguments if we 
		want to change the name of the sheet
	'''
	worksheet = workbook.add_worksheet("sheet_1")

	csv_separator = ','

	csv.register_dialect('comma', delimiter = ',')

	'''
		iterate through csv file

	'''

	with open(csv_file, 'r') as csv_reader:

		reader = csv.reader(csv_reader, dialect='comma')

		for row_index , rows in enumerate(reader):
			for column_index, columns in enumerate(rows):
				worksheet.write(row_index,column_index,columns)
	workbook.close()


def main():
	csv_excel("D://macrocodesrequired//SampleCSVFile_119kb.csv")


if __name__ == '__main__':
	main()