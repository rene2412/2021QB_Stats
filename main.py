import csv
import sys
# Function to read and print the contents of the CSV file
def search_qb_stats(file_path): 
    labels =  ["Team:", "Completions:", "Attempts:", "Yards:", "Touchdowns:", "Interceptions", "Sacked:", "Sacked Yards:", "Longest Pass:", "Passer Rating: ", "Rushing Attempts:", "Rushing Yards:", "Rushing TD's:", "Longest Rush:"]
    #while True:
    qb_name = input("Enter the name of the Quarterback: ")
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
                #else:
                  #  print("Error finding Qb: Please enter a valid name")
                   # break

def common_qb_questions(file_path):
    while True:
        try:
            option = int(input("Please enter an option (1-5):\n1) Which QB had the most touchdowns in 2021\n2) Which QB had the most passing yards in 2021\n3) Which QB had the most completions in 2021\n4) Which QB had the highest passer rating in 2021\n5) Quit\n"))
        except ValueError:
            print("INVALID INPUT")
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
                        print("QB Name: ", max_value, " | Touchdowns: ", max_touchdowns)
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
                        print("QB Name: ", max_value, "| Pass Yards: ", max_pass_yards)
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
                        print("QB Name: ", max_value, "| Pass Completions: ", max_pass_completions)
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
                     print("QB Name: ", max_value, "| Passer Rating: ", max_pass_ratings)
                     break
            else:
                sys.exit()
while True:
    try: 
        main = int(input("Do you want to:\n1) Search 2021 QB Stats?\n2) Search through the most common asked 2021 QB Questions\n3) Quit\n"))
    except ValueError:
        print("INVALID INPUT")
        continue
    if main != 1 and main !=2 and main !=3:
        print("Invalid Input")
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
