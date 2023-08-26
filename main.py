import csv
import sys
# Function to read and print the contents of the CSV file
def search_qb_stats(file_path): 
    labels =  ["Team:", "Completions:", "Attempts:", "Yards:", "Touchdowns:", "Interceptions", "Sacked:", "Sacked Yards:", "Longest Pass:", "Passer Rating: ", "Rushing Attempts:", "Rushing Yards:", "Rushing TD's:", "Longest Rush:"]    
    qb_name = input("Enter the name of the Quarterback: ")
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
                 print("\n")
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
        labels = ["Touchdowns", "Yards", "Completions", "Passer Rating"]
        for i, col in enumerate(csvreader):
            if i == max_qb_index:
                label = labels[i]
                name = col[0]
                print(name, col[column_index], f"{label}")
 
csv_file_path = 'nfl_offense_data_2021.csv'
get_max_stat(csv_file_path, 5)
'''
def common_qb_questions(file_path):
    while True:
        try:
            option = int(input("Please enter an option (1-5):\n1) Which QB had the most touchdowns in 2021\n2) Which QB had the most passing yards in 2021\n3) Which QB had the most completions in 2021\n4) Which QB had the highest passer rating in 2021\n5) Quit\n"))
        except ValueError:
            print("INVALID INPUT\n")
            continue
        if option == 1:
            max_value, max_stat = get_max_stat(file_path, 8)
            print(max_value, ": ", max_stat, "Touchdowns")
        break
'''

'''
def common_qb_questions(file_path):
    while True:
        try:
            option = int(input("Please enter an option (1-5):\n1) Which QB had the most touchdowns in 2021\n2) Which QB had the most passing yards in 2021\n3) Which QB had the most completions in 2021\n4) Which QB had the highest passer rating in 2021\n5) Quit\n"))
        except ValueError:
            print("INVALID INPUT\n")
            continue
        with open(file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            if option != 1 and option !=2 and option !=3 and option !=4 and option !=5:
                print("INVALID INPUT\n") 
                continue
            elif option == 1:
             #column data is holding all the data in column 5 which contains the touchdowns 
                column_data = [col[5] for col in csvreader]
                touchdowns = [] # list of touchdowns  to push the coumn data in
                for td in column_data:
                    try:
                        touchdowns.append(int(td))
                    except ValueError:
                        touchdowns.append(0)#any non int in the list will be treated like a 0
                max_touchdowns = max(touchdowns)
                max_index = touchdowns.index(max_touchdowns)
                csvfile.seek(0)
                for i, row in enumerate(csvreader):
                    if i == max_index:
                        max_value = row[0]
                        print(max_value, ": ", max_touchdowns, "Touchdowns\n\n")
                break
            elif option == 2:
                column_data = [col[4] for col in csvreader]
                pass_yards = []
                for yards in column_data:
                    try:
                        pass_yards.append(int(yards))
                    except ValueError:
                        pass_yards.append(0)
                max_pass_yards = max(pass_yards)
                max_index = pass_yards.index(max_pass_yards)
                csvfile.seek(0)
                for i, row in enumerate(csvreader):
                    if i == max_index:
                        max_value = row[0]
                        print(max_value, ": ", max_pass_yards, " Yards\n\n")
                break
            elif option == 3:
                column_data = [col[2] for col in csvreader]
                pass_completions = []
                for completion in column_data:
                    try:
                        pass_completions.append(int(completion))
                    except ValueError:
                        pass_completions.append(0)
                max_pass_completions = max(pass_completions)
                max_index = pass_completions.index(max_pass_completions)
                csvfile.seek(0)
                for i, row in enumerate(csvreader):
                    if i == max_index:
                        max_value = row[0]
                        print(max_value, ": ", max_pass_completions, " Completions\n\n")
                break
            elif option == 4: 
                column_data = [col[10] for col in csvreader]
                pass_ratings = []
                for rating in column_data:
                    try:
                        pass_ratings.append(float(rating))
                    except ValueError:
                        pass_ratings.append(0)
                max_pass_ratings = max(pass_ratings)
                max_index = pass_ratings.index(max_pass_ratings)
                csvfile.seek(0)
                for i, row in enumerate(csvreader):
                    if i == max_index:
                     max_value = row[0]
                     print(max_value, ": ", max_pass_ratings, "Passer Rating\n\n")
                break
            else:
                sys.exit()


while True:
    try: 
        main = int(input("Do you want to:\n1) Search 2021 QB Stats?\n2) Search through the most common asked 2021 QB Questions\n3) Quit\n"))
    except ValueError:
        print("INVALID INPUT\n")
        continue
    if main != 1 and main !=2 and main !=3:
        print("INVALID INPUT\n")
        continue
    csv_file_path = 'nfl_offense_data_2021.csv'
    if main == 1:
        search_qb_stats(csv_file_path)
        continue
    elif main == 2:
        common_qb_questions(csv_file_path)
        continue
    else:
        sys.exit()
    '''
