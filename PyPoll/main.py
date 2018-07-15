import os
import csv

PyPoll = os.path.join('C:/Users/Jes/Desktop/boot_camp/python-challenge/election_data.csv')

total_votes = 0
candidates_withvotes = []
Khan = 0
Correy = 0
Li = 0
O_Tooley = 0

with open (PyPoll, 'r') as f:
    csvreader = csv.reader(f)
    csv_header = next(csvreader)
    for row in csvreader:
        # print(row)
        total_votes +=1
        candidate = row[2]

        if candidate not in candidates_withvotes:
            candidates_withvotes.append(row[2])
    
        if candidate == 'Khan':
             Khan +=1
        elif candidate == 'Correy':
            Correy +=1
        elif candidate == 'Li':
            Li +=1
        else:
            O_Tooley +=1

# print(Khan)
Khan_percent = '{percent: .3%}'.format(percent = Khan/total_votes)

# print(Correy)
Correy_percent = '{percent: .3%}'.format(percent = Correy/total_votes)

# print(Li)
Li_percent = '{percent: .3%}'.format(percent = Li/total_votes)

# print(Li_percent)
# print(O_Tooley)
O_Tooley_percent = '{percent: .3%}'.format(percent = O_Tooley/total_votes)

# print(candidates_withvotes)        

# print(total_votes)
    
print('''Election Results

------------------------------------------
''')

print(f'''Total Votes: {total_votes}

-------------------------------------------

''' )
print(f'Khan: {Khan_percent} ( {Khan})')
print(f'Correy: {Correy_percent} ( {Correy})')
print(f'Li: {Li_percent} ( {Li})')
print(f'''O'Tooley: {O_Tooley_percent} ( {O_Tooley})
-------------------------------------------
''')

candidate_and_votes = {'Khan': Khan, 'Corry': Correy, 'Li':Li, 'O_Tooley': O_Tooley}

for winner, vote in candidate_and_votes.items():
    if vote == max(Khan, Correy, Li, O_Tooley):
        print('Winner: ' + winner)

# in Bash: run python main.py > PyPoll_output.txt
