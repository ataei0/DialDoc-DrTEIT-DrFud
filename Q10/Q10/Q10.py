import csv

with open('data_replaced.csv', 'w') as temp:
   with open('data.csv', 'r') as f:
      reader = csv.reader(f)
      writer = csv.writer(temp)
      for line in reader:
        line[0] = ''
        #print(line)
        writer.writerow(line)

#opening the new file for checking the results:
with open('data_replaced.csv') as f:
  reader = csv.reader(f)
  for line in reader:
    print(line)
