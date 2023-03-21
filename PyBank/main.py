import os
import csv
# path to collect file
financial_data=r'C:/Users/klw4b/OneDrive/Documents/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv'

    
    
   
  
#read CSV file
with open(financial_data,"r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    first_line=next(csvreader)
    second_line=next(csvreader)
    #print(csvreader)
    totals=int(first_line[1]) +int(second_line[1])
    prev_month=int(second_line[1])
    tot_variance=int(second_line[1])- int(first_line[1])
    variance=0
    count=2
    greatest_var=int(second_line[1])- int(first_line[1])
    greatest_month=second_line[0]
    small_var=int(second_line[1])- int(first_line[1])
    small_month=second_line[0]
    
    for row in csvreader:
        #sum amounts in column 2
        totals+=int(row[1])
        profit_loss=int(row[1])
        variance=profit_loss - prev_month
        tot_variance+=variance
        prev_month=profit_loss
        count+=1
        if variance>greatest_var:
            greatest_var=variance
            greatest_month=row[0]
        
        if variance<small_var:
            small_var=variance
            small_month=row[0]
    average=tot_variance/(count-1) 
    

    
        
  
print(f"Total months: {count}")
print(f"Total Amount: {totals}")  
print(f"Average change: {average}") 
print(f"Greatest increase in profits: {greatest_var}  {greatest_month}")
print(f"Greatest decrease in profits: {small_var}  {small_month}")
    

output_file=os.path.join("Analysis","budget_results.csv")
with open(output_file,'w') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    
    csvwriter.writerow(["Total months",count])
    csvwriter.writerow(["Total Amount", totals])
    csvwriter.writerow(["Average Change",average])
    csvwriter.writerow(["Greatest Increase in Profits",greatest_var])
    csvwriter.writerow(["Greatest Decrease in Profits",small_var])