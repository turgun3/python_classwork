id,username,email,ip_address
1,root,root@example.com,192.168.0.1
2,admin,admin@example.com,192.168.0.2
3,test_user,test_user@example.com,192.168.0.3
4,second_user,second_user@example.com,192.168.0.4”


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

path = "output.csv"
csv_writer(data, path)
