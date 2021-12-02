import csv
with open('', newline='') as csvfile:
   line = csv.reader(csvfile, delimiter=',', quotechar='|')
   for row in line:
      print(', '.join(row))
