import os
import csv

PyBank = os.path.join('C:/Users/Jes/Desktop/boot_camp/python-challenge/budget_data.csv')

num_months = 0
profit_loss = 0
PL = []
PL_change = []
total_change = 0
date = []

print('''Financial Analysis: 

-----------------------------------
''')

with open(PyBank, 'r') as f: 
    csvreader = csv.reader(f)
    csv_header = next(csvreader)
    for row in csvreader:
        num_months +=1
        profit_loss += int(row[1])
        # print(row)
        # print(row[1])
        PL.append(int(row[1]))
        date.append(row[0])
    print(f'Total Months: {num_months}')
    print(f'Total:${profit_loss}')
    

for i in range(1,len(PL)):
    PL_change.append(int(PL[i])-int(PL[i-1]))
    total_change += int(PL_change[i-1])

# print(PL_change)
# print(total_change)
avg_change = '{: .2f}'.format(total_change/(num_months-1))
print(f'Average Change: ${avg_change}')

max_change = max(PL_change)
max_index = PL_change.index(max_change)
# print(max_index)
max_date = date[max_index+1]
print(f'Greatest Increase in Profits: {max_date} (${max_change})')

min_change = min(PL_change)
min_index = PL_change.index(min_change)
# print(min_index)
min_date = date[min_index+1]
print(f'Greatest Decrease in Profits: {min_date} (${min_change})')

# in Bash, run python main.py > PyBank_output.txt






















