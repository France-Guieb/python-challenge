# import os module
import os

# module for reading csv files
import csv

file = os.path.join('Resources', 'budget_data.csv')

months = []
pl = []
total_pl = 0
delta_pl = 0
prev_record = 0
delta_pl_list = []
x = 0

with open(file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    # first row is header
    csv_header = next(csv_reader)

    # read each row of data below the header
    for row in csv_reader:       
        # add months  
        months.append(row[0])

        # add profit
        pl.append(row[1])

        # total profit / loss
        total_pl += int(row[1])

        # average change
        delta_pl = int(row[1]) - prev_record
        prev_record = int(row[1])
        delta_pl_list.append(delta_pl)

    # calculate average change using function with rounded to 2 decimal places
    def average(delta_pl_list):
        delta_pl_list.pop(0)
        return sum(delta_pl_list) /(len(delta_pl_list))

average_change = round(average(delta_pl_list), 2)

delta_pl_list.insert(0, 0)

# zip list together
cleaned_csv = zip(months, pl, delta_pl_list) 

# set variable for output file
output_file = os.path.join("cleaned_data.csv")

#  Open the output file
with open(output_file, "w", newline ='') as datafile:
    csv_writer = csv.writer(datafile, delimiter=",")

    # Write the header row
    csv_writer.writerow(["Date", "Profit/Losses", "Net Change"])

    # Write in zipped rows
    csv_writer.writerows(cleaned_csv)

    #greatest increase in profits (amount) without using max()
    def my_max(delta_pl_list):
        value = delta_pl_list[0]
        for x in delta_pl_list:
            if x > value:
                value = x
        return value
    inc_profit = my_max(delta_pl_list)
    month_inc = months[delta_pl_list.index(inc_profit)]

    # greatest decrease in profits (amount) without using min()
    def my_min(delta_pl_list):
        value = delta_pl_list[0]
        for x in delta_pl_list:
            if x < value:
                value = x
        return value
    dec_profit = my_min(delta_pl_list)
    month_dec = months[delta_pl_list.index(dec_profit)]


# summary / final report
print("Financial Analysis")
print("-----------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${total_pl}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {month_inc} (${inc_profit})')
print(f'Greatest Decrease in Profits: {month_dec} (${dec_profit})')

