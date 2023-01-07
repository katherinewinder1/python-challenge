import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

#set variables
total_months = 0
net_total = 0
profit_losses = []
change = 0
last_val = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
change_list = []

#open file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_months += 1
        net_total = net_total + int(row[1])
        
        change = int(row[1]) - last_val 
        last_val = int(row[1]) 
        if (change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        if (change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

        change_list = change_list + [change]
average_change = (sum(change_list) - change_list[0]) / len(change_list)


print("Financial Analysis")
print("-----------------------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_total)}")
print(f"Average Change: ${str(average_change)}")
print(f"Greatest Increase: {str(greatest_increase)}")
print(f"Greatest Decrease: {str(greatest_decrease)}")

# Export text file
text_file = "output.txt"
with open(text_file,"w") as file:
     
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {str(total_months)}")
    file.write("\n")
    file.write(f"Total: ${str(net_total)}")
    file.write("\n")
    file.write(f"Average Change: {str(average_change)}")
    file.write("\n")
    file.write(f"Greatest Increase: {str(greatest_increase)}")
    file.write("\n")
    file.write(f"Greatest Decrease: {str(greatest_decrease)}")
