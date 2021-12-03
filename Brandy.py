import csv
with open('ContributionsList-BrandyBrooks-2021Dec2.csv', newline='') as csvfile:
   line = csv.reader(csvfile, delimiter=',', quotechar='|')
   i = 0
   for row in line:
      i += 1
      if i >1 and i<11:
         rawname = row[4]
         rawaddr = row[5]
         print(', '.join((rawname,rawaddr)))
