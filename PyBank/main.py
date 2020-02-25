#import modules
import os
import csv 

#create working directory
csvpath=os.path.join('..','PyBank','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    print(f"Header: {csv_header}")               

#calculate months       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))
#calculate revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

#calculate average change
    x = 0
    for x in range(len(revenue) - 1):
        profit_loss = int(revenue[x+1]) - int(revenue[x])
    #append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    print(monthly_change)
    #print(Total)
    
#calculate greatest increase
    profit_increase = max(revenue_change)
    print(profit_increase)
    y = revenue_change.index(profit_increase)
    month_increase = month[y+1]
    
#calculate greatest decrease
    profit_decrease = min(revenue_change)
    print(profit_decrease)
    z = revenue_change.index(profit_decrease)
    month_decrease = month[z+1]


#print statements

print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')


print("Total Months: " + str(len(month)))

print("Total: $ " + str(total_revenue))
      
print("Average Change: $" + str(round(monthly_change,2)))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

with open('output.txt', 'w+') as file:
    #Triple quotes to enclose multiple lines in print statement is possible; specifics for variables needed to use correctly
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: " + str(len(month))+ '\n')
    file.write("Total Revenue: $" + str(total_revenue)+ '\n')
    file.write("Average Revenue Change: $" + str(monthly_change)+ '\n')
    file.write("Greatest Increase in Revenue: " + str(month_increase) + " ($"+str(profit_increase)+")\n")
    file.write("Greatest Decrease in Revenue: " + str(month_decrease) + " ($"+str(profit_decrease)+")\n")
    file.write("----------------------------\n")
    file.close()