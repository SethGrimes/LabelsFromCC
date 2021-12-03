import csv
with open('ContributionsList-BrandyBrooks-2021Dec2.csv', newline='') as csvfile:
   line = csv.reader(csvfile, delimiter=',', quotechar='|')
   i = 0
   for row in line:
      i += 1
      if i >1:
         rawname = row[7]
         rawaddr = r[9]
         print(', '.join((rawnamme,rawaddr))
