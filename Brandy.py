import csv
with open('ContributionsList-BrandyBrooks-2021Dec2.csv', newline='') as csvfile:
   line = csv.reader(csvfile, delimiter=',', quotechar='|')
   for row in line:
      print(', '.join(row))
