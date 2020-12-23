
import csv

def csv_writer(data, path):
	with open(path, "w") as csv_file:
		writer = csv.writer(csv_file, delimiter=',')
		for line in data:
			writer.writerow(line)

data = ["username,email".split(","),
		"root,root@example.com,".split(","),
		"admin,admin@example.com,".split(","),
		"test_user,test_user@example.com,.split(","),
		"second_user,second_user@example.com".split(",")
		]

path = "data.csv"
csv_writer(data, path)
