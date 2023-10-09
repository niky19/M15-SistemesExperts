#ETL from csv
import csv

with open('II/basket_players.csv') as csv_file:
	csv_reader = csv.DictReader('II/basket_players.csv')
	dict_from_csv = dict(list(csv_reader)[5])
	list_of_column_names = list(dict_from_csv)
	print(list_of_column_names)


