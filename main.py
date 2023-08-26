import csv
import sys
# Function to read and print the contents of the CSV file
def search_qb_stats(file_path): 
    labels =  ["Team:", "Completions:", "Attempts:", "Yards:", "Touchdowns:", "Interceptions", "Sacked:", "Sacked Yards:", "Longest Pass:", "Passer Rating: ", "Rushing Attempts:", "Rushing Yards:", "Rushing TD's:", "Longest Rush:"]    
    qb_name = input("Enter the name of the Quarterback:\n")
    found = False
    with open(file_path, newline='') as csvfile:
         csvreader = csv.reader(csvfile)
         for row in csvreader:
             name = row[0].strip()
             if name == qb_name:
                 stats = row[1:15]
                 print(f"2021 Stats for {name}: ")
                 for index, stat in enumerate(stats):
                    label = labels[index]
                    print(f"{label} {stat}")
                 found = True
                 print('')
                 break
         if not found:
            print("Error finding QB: Please enter a valid name:\n")

def get_max_stat(file_path, column_index):
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        column_data = [col[column_index] for col in csvreader]
        stats = []
        for stat in column_data:
            try:
                stats.append(float(stat))
            except ValueError:
                stats.append(0)
        max_stat = max(stats)
        max_qb_index = stats.index(max_stat)
        csvfile.seek(0)

        for i, col in enumerate(csvreader):
             if i == max_qb_index:
                name = col[0]
                print(name + ':', col[column_index], end ='')

csv_file_path = 'nfl_offense_data_2021.csv'

def common_qb_questions():
    while True:
        try:
            option = int(input("Please enter an option (1-5):\n1) Which QB had the most touchdowns in 2021\n2) Which QB had the most passing yards in 2021\n3) Which QB had the most completions in 2021\n4) Which QB had the highest passer rating in 2021\n5) Quit\n"))
        except ValueError:
            print("INVALID INPUT\n")
            continue
        if option < 1 and option > 4:
            print("Invalid Input\n")
        if option == 1:
            get_max_stat(csv_file_path, 5); print(" Touchdowns")     
            break
        if option == 2:            
            get_max_stat(csv_file_path, 4); print(" Yards")
            break
        if option == 3:
            get_max_stat(csv_file_path, 2); print(" Completions")
            break
        if option == 4:
            get_max_stat(csv_file_path, 10); print( " Passer Rating")
            break
        else:
            break
    
while True:
    try: 
        main = int(input("Do you want to:\n1) Search 2021 QB Stats?\n2) Search through the most common asked 2021 QB Questions\n3) Quit\n"))
    except ValueError:
        print("INVALID INPUT\n")
        continue
    if main != 1 and main !=2 and main !=3:
        print("INVALID INPUT\n")
        continue
    if main == 1:
        search_qb_stats(csv_file_path)
        continue
    elif main == 2:
        common_qb_questions()
        continue
    else:
        sys.exit()
    
